file_path = 'finalv1.txt'

with open(file_path, "r") as input_file:
    lines = input_file.readlines()

modified_lines = []
#bool to check if code is in a multi lined comment
in_comment_block = False

for line in lines:
    #added if lines to check for other comments as well
    if "(*" in line:
        in_comment_block = True
    # remove comments
        line = line.split("(*", 1)[0]
    # checks comment 
    if "*)" in line and in_comment_block:
        in_comment_block = False

    #accesses the second element of the list 
        line = line.split("*)", 1)[1]
    
    if not in_comment_block:
        line = line.split("(*")[0]
    
    # replace := with = 
    # : is always being input instead of = 
    # added check for := 
    line = line.replace(":=", "=")
    
    # replace single quotes with double " "
    line = line.replace("'", "\"")

    # remove extra spaces
    line = " ".join(line.split())

    # skip blank lines
    if line != "":
        modified_lines.append(line)

with open("final23.txt", "w") as output_file:
    output_file.write("\n".join(modified_lines))