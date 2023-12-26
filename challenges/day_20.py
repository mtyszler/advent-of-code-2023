from functions_day_20 import *
import time

# challenge 1
print("challenge 1")

outputs, inputs, types = parse_input_file('../input_files/input_day_20.txt')
pulses = run_pulses(outputs, inputs, types, n_pulses=1000)

print(pulses['high'] * pulses['low'])

print()
print("challenge 2")
outputs, inputs, types = parse_input_file('../input_files/input_day_20.txt')
target_module = 'rx'
print('inputs of', target_module)
inputs_of_target = inputs[target_module]
print(inputs_of_target)
print([types[x] for x in inputs_of_target])
print("needs to get a high pulse to ", inputs_of_target)
while len(inputs_of_target) == 1:
    print()
    print('inputs of', inputs_of_target)
    inputs_of_target = inputs[inputs_of_target[0]]
    print(inputs_of_target)
    print([types[x] for x in inputs_of_target])
    print("needs to get a high pulse to ", inputs_of_target)


pulses = run_pulses(outputs, inputs, types, n_pulses=5000, target_module='xn', target_pulse='high')
print()
print("results is the product:")
print(3769 * 3847 * 3877 * 4057)



