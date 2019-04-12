from core.module import Connector, ConfigOption
from logic.generic_logic import GenericLogic
import numpy as np
import copy


class FluorescenceReadoutLogic(GenericLogic):

    _modclass = 'FluorescenceReadoutLogic'
    _modtype = 'logic'

    _cfg_scheme_str = ConfigOption(name='readout_scheme', missing='error')

    _counter_connector = Connector(interface='GatedCounterInterface')

    def __init__(self, config, **kwargs):
        super().__init__(config=config, **kwargs)

        # Since actual activation of the module will be performed in
        # on_activate(), here one only needs to declare all instance variables

        # Reference to counting hardware module
        self._counter = None

        # Number of readouts to perform in one go
        # (given by above-lying logic in init_readout())
        self._n_points = 0

        # Name of the readout scheme
        self._scheme_str = ''

        # number of counter bins, used to calculate single state point
        self._bins_per_point = 0

        # all currently implemented schemes
        self._implemented_scheme_list = [
            'state_norm'
        ]

    def on_activate(self):

        # Get reference to GatedCounter hardware module
        self._counter = self._counter_connector()

        # Init all variables with default values - actual initialization
        # of readout will be performed in init_readout().
        self.set_readout_scheme(new_scheme_str=self._cfg_scheme_str)

    def on_deactivate(self):
        self.close_readout()

    # ------------- Interface methods ----------------

    def init_readout(self, n_points):

        # Try initializing counter
        op_status = self._counter.init_counter(
            bin_number = n_points*self._bins_per_point
        )
        if op_status == 0:
            self.log.info('init_readout(): successfully initialized counting hardware')

            # Save requested state array length
            self._n_points = n_points

            return 0
        else:
            self.log.error('init_readout(): initialization of counter failed')
            self._n_points = 0

            return -1

    def close_readout(self):

        op_status = self._counter.close_counter()

        if op_status < 0:
            self.log.error('close_readout(): closing counter failed. Quit anyways.')
            return -1

        self._counter = None
        self._n_points = 0
        self._scheme_str = ''
        self._bins_per_point = 0

        return 0

    def start_readout(self):
        op_status = self._counter.start_counting()

        if op_status < 0:
            self.log.error('start_readout(): starting counter failed')
            return -1

        return 0

    def terminate_readout(self):
        op_status = self._counter.terminate_counting()

        if op_status < 0:
            self.log.error('terminate_readout(): attempt to terminate counter failed')
            return -1

        return 0

    def get_status(self):
        """
        Returns status of readout logic

        -1 - "void" readout crashed or was not initialized.
             It has to be (re)initialized by calling init_readout()

         0 - "idle" - readout is ready to be started by calling start_readout().
             There is no state data to read, if readout module is "idle".

             If readout process was started before and readout appears
             to be "idle", process was terminated before completion and
             all accumulated data was deleted.

         1 - "in_progress" - readout is accumulating _state_array right now.
             Module will transit to "finished" state once it acquires complete
             _state_array.

             No data can be read out until this process is finished
             If get_state_array() is called in this state, it will be blocked and
             will return only after array accumulation is complete.

             Readout can be interrupted/closed by calling terminate_readout() or
             close_readout() to bring it to "idle" or "void" state respectively.

         2 - "finished" - readout has finished accumulating _state_array.
             Now get_count_array() will return accumulated array immediately.

        :return: (int) counter status code
        """

        return self._counter.get_status()

    def get_state_array(self, timeout=-1):

        # Try getting count_array from the counter
        raw_array = self._counter.get_count_array(timeout=timeout)

        # If counter returned non-trivial array,
        # process raw counts according to the chosen scheme
        if len(raw_array) > 0:

            if self.get_readout_scheme() == 'state_norm':
                # First bin contains state-dependent counts,
                # second - normalization

                # Sanity check
                expected_len = self._n_points * self._bins_per_point
                if len(raw_array) != expected_len:
                    self.log.error('get_state_array(): length {} of the array, returned by counter, '
                                   'does not match expected value of {}.'
                                   ''.format(len(raw_array), expected_len))
                    return []

                # Array to store calculate calculated states
                state_array = np.zeros(self._n_points, dtype=np.float32)

                for i in range(self._n_points):
                    try:
                        state_array[i] = raw_array[i] / raw_array[i+1]
                    except ZeroDivisionError:
                        self.log.warn('get_state_array(): normalization bin #{} is zero, cannot calculate state')
                        state_array[i] = None

        # counter returned empty array
        else:
            return []

    def get_readout_scheme(self):
        return copy.deepcopy(self._scheme_str)

    def set_readout_scheme(self, new_scheme_str):

        # Sanity check: ensure that new_scheme_str is implemented
        if new_scheme_str not in self._implemented_scheme_list:
            self.log.error('set_readout_scheme(): scheme {} is not implemented'
                           ''.format(new_scheme_str))
            return self.get_readout_scheme()

        # Set new readout parameters
        # -- scheme name
        self._scheme_str = new_scheme_str

        # -- number of counter bins, used to determine state
        if new_scheme_str == 'state_norm':
            # one main pulse - "state" and
            # one normalization pulse - "norm"
            self._bins_per_point = 2

        return self.get_readout_scheme()


