from functions_day_20 import *
import time

# challenge 1
print("challenge 1")

outputs, inputs, types = parse_input_file('../input_files/input_day_20.txt')
pulses = run_pulses(outputs, inputs, types, n_pulses=1000)

print(pulses['high'] * pulses['low'])


print("challenge 2")
outputs, inputs, types = parse_input_file('../input_files/input_day_20.txt')
presses = retrace_steps(outputs, inputs, types, 'rx')

print(pulses['high'] * pulses['low'])
