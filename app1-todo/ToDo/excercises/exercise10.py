try:
    total_value = int(input('Enter total value: '))
    value = int(input('Value: '))
    result = (value/total_value)*100
    print(f'That is {result}%')
except ValueError:
    print(f'You need to enter a number. Run the program again')
except ZeroDivisionError:
    print(f'Your total value cannot be zero.')
