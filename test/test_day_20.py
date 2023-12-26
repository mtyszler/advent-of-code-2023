import pytest

from functions_day_20 import *


def test_parse():
    outputs, inputs, types = parse_input_file('../input_files/input_day_20_example_1.txt')


def test_single_pulse():
    outputs, inputs, types = parse_input_file('../input_files/input_day_20_example_1.txt')
    pulses = run_pulses(outputs, inputs, types, n_pulses=1)

    assert (pulses == {'high': 4, 'low': 8})


def test_all_pulse():
    outputs, inputs, types = parse_input_file('../input_files/input_day_20_example_1.txt')
    pulses = run_pulses(outputs, inputs, types, n_pulses=1000)

    assert (pulses == {'high': 4000, 'low': 8000})
    assert (pulses['high'] * pulses['low'] == 32000000)


def test_all_pulse_2():
    outputs, inputs, types = parse_input_file('../input_files/input_day_20_example_2.txt')
    pulses = run_pulses(outputs, inputs, types, n_pulses=1000)

    assert (pulses == {'high': 2750, 'low': 4250})
    assert (pulses['high'] * pulses['low'] == 11687500)
