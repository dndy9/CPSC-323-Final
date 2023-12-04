def get_final23():
    with open('final23.txt', "r", encoding = 'utf-8') as input_file:
        lines = input_file.read()

    lines = lines.replace('\n', '').replace('\r', '')
    return lines
