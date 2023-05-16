contents = ['Something long for doc.txt', 'Something long for report.txt', 'Something long for presentation.txt']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    open(fr'C:\Users\peych\PycharmProjects\pythonMegaCourse40Days20Apps\ToDo\files\{filename}', 'w').writelines(content)
