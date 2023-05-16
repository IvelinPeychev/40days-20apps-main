from functions import *
# import functions  - it is better for readability

while True:
    # Get user input and strip space characters in it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # match user_action:
    #     case 'add':
    if user_action.startswith('add') or user_action.startswith('new'):
        # todo = input("Enter a todo: ") + '\n'
        todo = user_action[4:]

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()

        todos = get_todos()

        todos.append(todo + '\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        # with open('todos.txt', 'w') as file:
        #     todos = file.writelines(todos)

        write_todos(todos)

    # case 'show' | "display":
    elif user_action.startswith('show'):
        # print(todos)
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()

        todos = get_todos()

        # new_todos = []
        #
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        # print(todos)

        for index, item in enumerate(todos):
            item = item.strip('\n')
            # item = item.title()
            print(f'{index + 1}-{item.title()}')
        print(f'the length of the list is {len(todos)}')

    # case 'edit':
    elif user_action.startswith('edit'):
        try:
            # number = int(input("Number of the todo to edit: "))
            number = int(user_action[5:])
            # with open('todos.txt', 'r') as file:
            #     todos = file.readlines()

            todos = get_todos()

            # existing_todo = todos[number - 1]

            new_todo = (input("New todo: "))
            todos[number - 1] = new_todo + '\n'

            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)
            write_todos(todos)
        except ValueError:
            print('Your command is not valid')
            user_action = input("Type add, show, edit, complete, or exit: ")
            user_action = user_action.strip()

    # case 'complete':
    elif 'complete' in user_action:
        # number = int(input("Number of the todo to complete: "))
        number = int(user_action[9:])

        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()

        todos = get_todos()

        index = number - 1
        todo_to_removed = todos[index].strip('\n').title()
        todos.pop(index)

        # with open('todos.txt', 'w') as file:
        #     file.writelines(todos)

        write_todos(todos)

        message = f'Todo {todo_to_removed} was removed from the list'
        print(message)
    # case 'exit':
    elif 'exit' in user_action:
        break
    # case _:
    else:
        print("Hey, you entered unknown command")

print("Bye!")
