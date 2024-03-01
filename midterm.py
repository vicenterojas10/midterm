import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
    # Continue by removing the numbers greater than 50
    # from the list and replacing the other numbers with "XX" print the list at the end

for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = "XX"
    else:
        continue
print(random_numbers)

