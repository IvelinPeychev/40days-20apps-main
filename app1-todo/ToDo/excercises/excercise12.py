def cubic(liters):
    result = liters / 1000
    return result


print(cubic(500))

user_password = input('Enter your password ')

def check_password(password):
    result = {}

    if len(password) >= 8:
        result['lenght'] = True
    else:
        result['lenght'] = False

    upper = False
    for i in password:
        if i.isupper():
            upper = True
    result['upper'] = upper

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result['digit'] = digit
    if all(result.values()):
        print('Your password is strong')
    else:
        print('Your password is weak')


check_password(user_password)