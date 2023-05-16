# ---------------------------------1

def get_age(year_of_birth, current_year=2023):
    result = current_year - year_of_birth
    return result


print(get_age(1996))

# ----------------------------------2

user_year_of_birth = int(input('What is your year of birth? '))
age = get_age(user_year_of_birth)
print(age)

# -------------------------------------3

if age >= 120:
    print('You are very old')
else:
    print(age)


# -----------------------------------------4

def number_of_names(names):
    # Option 1
    # commas = names.count(',')
    # return commas + 1
    number = names.split(",")
    return len(number)


user_input = input('Enter names separated by commas (no spaces): ')
names = number_of_names(user_input)
print(names)
