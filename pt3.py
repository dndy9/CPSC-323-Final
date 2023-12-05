# Open the file in read mode and read its content into a list of lines
with open('final23.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Find the line with "program" and replace it with "int main()"
indent = False
for i, line in enumerate(lines):
    if 'begin' in line:
        lines[i] = line.replace('begin','int main() {')
        indent = True
    if 'end.' in line:
        lines[i] = line.replace('end.','}')
        indent = False
    if 'var' in line:
        lines[i] = line.replace('var','')
    if 'program' in line:
        lines[i] = '#include <iostream>\nusing namespace std;\n'
    if ': integer' in line:
        lines[i] = line.replace(': integer ','')
        lines[i] = "int " + lines[i] 
    if 'write' in line:
        lines[i] = line.replace('write','cout << ')
        lines[i] = lines[i].replace (',','<<')
        lines[i] = lines[i].replace('“','"')
        lines[i] = lines[i].replace('”','"')
        lines[i] = lines[i].replace('( ','')
        lines[i] = lines[i].replace(' )',' << endl')

    if indent and 'begin' not in line:
        lines[i] = '\t' + lines[i]

# Print the modified lines before joining them

# Join the modified lines into a single string
cpp_code = ''.join(lines)

# Display the resulting C++ code (optional)
print(cpp_code)

# Save the modified C++ code to a new file
with open('output_cpp_file_modified.cpp', 'w', encoding='utf-8') as cpp_file:
    cpp_file.write(cpp_code)
