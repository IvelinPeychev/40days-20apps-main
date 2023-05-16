# 1
filenames = ['document', 'report', 'presentation']

for index, name in enumerate(filenames):
    print(f'{index}-{name.title()}.txt')

# 2
ips = ['100.122.133.105', '100.122.133.111']
user_input = int(input("Enter the index of the IP address you want: "))
print(f'You choose {ips[user_input]}')