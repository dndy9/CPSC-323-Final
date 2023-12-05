from parsing_table import *
from read_final23 import get_final23
column_names = ['a','b','c','d','w','f','+','-','(',')','*','/','0','1','2','3','4','5','6','7','8','9','$',';','program','var','begin','integer','write','value=']
row_names = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']


def t_response(row, column, table):
    try:
        print("row index: ",row_names.index(row))
        print("column index: ",column)
        row_index = row_names.index(row)
        column_index = column_names.index(column)
        return table[row_index][column_index]
    except ValueError:
        print(f"Error: Row '{row}' or Column '{column}' not found in the table.")
        return None



input_string = get_final23()
input_list = input_string.split()

keywords = ['program', '“value=”', 'write', 'var', 'integer', 'begin', 'end.']

result_list = []

for item in input_list:
    if item in keywords:
        result_list.append(item)
    else:
        result_list.extend(list(item))

#print("Original List:")
#print(input_list)

#print("\nSeparated List:")
#print(result_list)


def parse(input_tokens, table):
    stack = ['$']  # Initialize the stack with the dollar sign as the bottom marker
    stack.append('A')  # Push the starting symbol onto the stack
    input_index = 0  # Index to track the current input token

    print("Now testing: ",input_tokens)

    while stack:
        top_of_stack = stack[-1]  # Get the top of the stack
        print("stack: ",stack)
        print("top of stack: ",top_of_stack)
        current_input = input_tokens[input_index]
        print("current input: ",current_input)

        #If the top of the stack is a terminal, check for a match with the current input
        if top_of_stack in column_names:
            #If there is a match, consume the input and pop the terminal from the stack
            if top_of_stack == current_input:
                print("Input Matched! stack: ",stack)
                stack.pop()  # Matched terminal, pop it from the stack
                input_index += 1
            #If there is no match, the input is not valid
            else:
                print("Error: Mismatch between stack and input. When top of stack is terminal, it must match input token.")
                return False
        #If the top of the stack is a non-terminal, look up the next action in the parsing table
        else:
            # Use the parsing table to determine the next action
            print("Searching the parsing table for the next action")
            action = t_response(top_of_stack, current_input, table)
            print("Action found at intersection of '" +top_of_stack +"' and '"+ current_input+ "':",action)

            # If the parsing table contains an error, the input is not valid
            if action is None:
                print("Error: No action found in the parsing table. Input is invalid")
                return False
            else:
                print("Action found in the parsing table. Popping stack ",action)
                stack.pop()  # Pop the non-terminal from the stack

                # Push the action's right-hand side onto the stack in reverse order
                print("Pushing the action onto the stack in reverse order")

                keyword_bool = False
                for keyword in keywords:
                    if keyword in action:
                        action = action.replace(keyword, '')
                        for symbol in reversed(action):
                            print("symbol:",symbol)
                            if symbol != '':
                                stack.append(symbol)
                        keyword_bool = True
                        stack.append(keyword)

                if not keyword_bool:
                    print("action:",action)
                    for symbol in reversed(action):
                        print("symbol:",symbol)
                        if symbol != '':  # Skip empty symbols
                            stack.append(symbol)

    if input_index == len(input_tokens):
        print("Input successfully parsed")
        return True
    else:
        print("Error: Not all input tokens were consumed")
        return False



success = parse(result_list, table)
print(success)

#success = parse(list_of_inputs[1], table)
#print(success)
#success = parse(list_of_inputs[2], table)
#print(success)
