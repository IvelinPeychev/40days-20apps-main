#1
file = open(r'C:\Users\peych\PycharmProjects\pythonMegaCourse40Days20Apps\essay.txt', 'r').read()

print(file)

#2
file2 = open(r'C:\Users\peych\PycharmProjects\pythonMegaCourse40Days20Apps\essay.txt', 'r').read()
print(len(file2))


#3
new_member = input('Add a new member: ')

file3 = open(r'C:\Users\peych\PycharmProjects\pythonMegaCourse40Days20Apps\members.txt', 'r')
all_members = file3.readlines()
file3.close()

all_members.append(new_member + "\n")

file3 = open(r'C:\Users\peych\PycharmProjects\pythonMegaCourse40Days20Apps\members.txt', 'w')
file3.writelines(all_members)
file3.close()

#4
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for item in filenames:
    file = open(item, 'w')
    file.write('Hello')
    file.close()

#5
# number1 = open(r'C:\Users\peych\PycharmProjects\pythonMegaCourse40Days20Apps\a.txt', 'r').read()
# number2 = open(r'C:\Users\peych\PycharmProjects\pythonMegaCourse40Days20Apps\b.txt', 'r').read()
# number3 = open(r'C:\Users\peych\PycharmProjects\pythonMegaCourse40Days20Apps\c.txt', 'r').read()
# print(number1 + '\n'+number2+'\n'+number3)
filenames = [r'..\..\a.txt', r'..\..\b.txt', r'..\..\c.txt']
for item in filenames:
    file = open(item, 'r').read()
    print(file)
    file.close()
