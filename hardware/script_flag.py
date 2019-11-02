from core.module import Base, ConfigOption

import random


class ScriptFlag(Base):

    """Random Number Generator quasi-instrument.
    Every time get_random_value() method is called, it takes self.mean and self.noise
    and returns the following random number (a list of samples_number random numbers):
        mean + noise*( random.random()-0.5 )
    """
    _modclass = 'ScriptFlag'
    _modtype = 'hardware'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_running = False

    def on_activate(self):
        """ Initialisation performed during activation of the module.
        """
        self.is_running = False
        pass

    def on_deactivate(self):
        """ Deinitialisation performed during deactivation of the module.
        """
        pass

