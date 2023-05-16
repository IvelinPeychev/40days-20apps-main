filename = ['1.doc', '1.report', '1.representation']

filename = [item.replace('.', '-') + '.txt' for item in filename]

print(filename)