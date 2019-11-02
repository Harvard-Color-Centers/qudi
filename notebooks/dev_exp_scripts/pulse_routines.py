from logic.pulsed.pulse_objects import PulseBlockElement, PulseBlock, PulseBlockEnsemble


def generate_rabi(tau_start, tau_step, n_points, chnl_dict, name='rabi'):

    # chnl_dict['aom_ch'] = 'd_ch0'
    # chnl_dict['ctr_ch'] = 'd_ch1'
    # chnl_dict['mw_ch'] = 'd_ch2'

    # ---------------- init_block ----------------

    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['aom_ch']] = True
    init_block = PulseBlock(
        name='init_block',
        element_list=[
            PulseBlockElement(init_length_s=2e-6, increment_s=0, digital_high=state_dict)
        ]
    )

    # ---------------- rabi_block ----------------

    # Gap before normalization pulse
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['aom_ch']] = True
    gap_before_norm = PulseBlockElement(init_length_s=0.4e-6, increment_s=0, digital_high=state_dict)

    # Normalization window
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['aom_ch']] = True
    state_dict[chnl_dict['ctr_ch']] = True
    norm_window = PulseBlockElement(init_length_s=0.5e-6, increment_s=0, digital_high=state_dict)

    # Gap after normalization
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['aom_ch']] = True
    gap_after_norm = PulseBlockElement(init_length_s=0.1e-6, increment_s=0, digital_high=state_dict)

    # Gap before mw pulse
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    gap_before_mw = PulseBlockElement(init_length_s=0.1e-6, increment_s=0, digital_high=state_dict)

    # MW pulse
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['mw_ch']] = True
    mw_pulse = PulseBlockElement(init_length_s=tau_start, increment_s=tau_step, digital_high=state_dict)

    # Gap after MW pulse
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    gap_after_mw = PulseBlockElement(init_length_s=0.1e-6, increment_s=0, digital_high=state_dict)

    # Gap before readout pulse
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['aom_ch']] = True
    gap_before_readout = PulseBlockElement(init_length_s=0.1e-6, increment_s=0, digital_high=state_dict)

    # Readout window
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['aom_ch']] = True
    state_dict[chnl_dict['ctr_ch']] = True
    readout_window = PulseBlockElement(init_length_s=0.5e-6, increment_s=0, digital_high=state_dict)

    # Gap after readout pulse
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['aom_ch']] = True
    gap_after_readout = PulseBlockElement(init_length_s=0.1e-6, increment_s=0, digital_high=state_dict)

    rabi_block = PulseBlock(
        name='rabi_block',
        element_list=[
            gap_before_norm,
            norm_window,
            gap_after_norm,
            gap_before_mw,
            mw_pulse,
            gap_after_mw,
            gap_before_readout,
            readout_window,
            gap_after_readout
        ]
    )

    # ---------------- finish_block ----------------

    # Gap before/after counter final gate
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    gap_ctr_final = PulseBlockElement(init_length_s=0.5e-6, increment_s=0, digital_high=state_dict)

    # Counter final gate
    state_dict = {
        'd_ch11': False, 'd_ch5': False, 'd_ch30': False, 'd_ch0': False, 'd_ch2': False, 'd_ch26': False,
        'd_ch3': False, 'd_ch15': False, 'd_ch27': False, 'd_ch13': False, 'd_ch6': False, 'd_ch29': False,
        'd_ch19': False, 'd_ch16': False, 'd_ch23': False, 'd_ch1': False, 'd_ch12': False, 'd_ch28': False,
        'd_ch20': False, 'd_ch4': False, 'd_ch14': False, 'd_ch25': False, 'd_ch31': False, 'd_ch21': False,
        'd_ch8': False, 'd_ch7': False, 'd_ch10': False, 'd_ch18': False, 'd_ch22': False, 'd_ch24': False,
        'd_ch9': False, 'd_ch17': False
    }
    state_dict[chnl_dict['ctr_ch']] = True
    ctr_final = PulseBlockElement(init_length_s=0.5e-6, increment_s=0, digital_high=state_dict)

    finish_block = PulseBlock(
        name='finish_block',
        element_list=[
            gap_ctr_final,
            ctr_final,
            gap_ctr_final
        ]
    )

    # ---------------- rabi_ensemble ----------------

    rabi_ensemble = PulseBlockEnsemble(
        name=name,
        block_list=[
            ('init_block', 0),
            ('rabi_block', n_points - 1),
            ('finish_block', 0)
        ]
    )

    return rabi_ensemble, [init_block, rabi_block, finish_block]

