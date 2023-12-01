file_path = 'finalv1.txt'

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
