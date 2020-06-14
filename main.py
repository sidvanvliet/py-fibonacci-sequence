times = int(input('Enter the sequence amount (e.x.: 19): '))
print("Writing out " + str(times) + " Fibonacci sequences:\n- - -")

previous_y = 1
previous_z = 2

for time in range(times):
    seq_answer = (previous_y + previous_z)

    previous_y = previous_z
    previous_z = seq_answer

    print(str(seq_answer))
