password = input('Enter new password: ')

# result = []
result = {}

# if len(password) >= 8:
#     result.append(True)
# else:
#     result.append(False)

if len(password) >= 8:
    result['Length'] = True
else:
    result['Length'] = False



digit = False
for i in password:
    if i.isdigit():
        digit = True

# result.append(digit)
result['Digit'] = digit

upper = False

for i in password:
    if i.isupper():
        upper = True

# result.append(upper)
result['Upper'] = upper


print(all(result))
print(result)
print(result.values())

# if all(result):
#     print('Strong password')
# else:
#     print('Weak password')

if all(result.values()):
    print('Strong password')
else:
    print('Weak password')
