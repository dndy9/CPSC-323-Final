with open('final23.txt', "r", encoding = 'utf-8') as input_file:
    lines = input_file.read()

line = lines.replace('\n', '')
print(lines)
