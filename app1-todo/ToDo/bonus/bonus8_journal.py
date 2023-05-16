date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10?\n ")

with open(f'../journal/{date}.txt', 'w') as file:
    thoughts = input("Please share your thoughts for today:\n")
    file.writelines(mood + 2 * "\n")
    file.writelines(thoughts)

