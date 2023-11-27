file_path = 'finalv1.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

with open("finalv1.txt", "r") as input_file:
    lines = input_file.readlines()

modified_lines = []

for line in lines:
    # remove comments
    line = line.split("(*")[0].strip()

    # remove extra spaces
    line = " ".join(line.split())

    # skip blank lines
    if line != "":
        modified_lines.append(line)

with open("final23.txt", "w") as output_file:
    output_file.write("\n".join(modified_lines))
