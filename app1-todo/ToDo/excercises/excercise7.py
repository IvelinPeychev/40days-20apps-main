# 1
names = ["john smith", "jay santi", "eva kuki"]

names = [name.title() for name in names]

print(names)

# 2
usernames = ["john 1990", "alberta1970", "magnola2000"]

usernames_length = [len(name) for name in usernames]

print(usernames_length)

# 3
user_entries = ['10', '19.1', '20']
user_entries = [float(entry) for entry in user_entries]

print(user_entries)

# 4 !!!
user_entries2 = ['10', '19.1', '20']
user_entries2 = [float(entry) for entry in user_entries]
print(sum(user_entries2))
