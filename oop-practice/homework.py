# Task 1

class User:
    def get_name(self):
        pass

    def age(self, current_year):
        pass


# Task 2

class User2:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        pass

    def age(self, current_year):
        pass

# Task 3 + 5
class User3:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.upper()

    def age(self, current_year):
        age = current_year - self.birthyear
        return age


# Task 4

user = User3('john', 1999)
print(user.age(2023))
print(user.get_name())
