

password = 'pass'
print(len(password))

if len(password) > 3:
    print('Password is strong')
elif len(password) == 4:
    print('Password is medium')
else:
    print('Password is weak')

