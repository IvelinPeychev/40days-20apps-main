import random

number_1 = int(input("Enter lower bound: "))
number_2 = int(input("Enter higher bound: "))

# random_number = int(random.uniform(number_1, number_2))
random_number = random.randint(number_1, number_2)

print(random_number)
