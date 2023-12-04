from parsing_table import table
column_names = ['a','b','c','d','w','f','+','-','(',')','*','/','1','2','3','4','5','6','7','8','9','$',';','program','var','begin','integer','write','value=']
row_names = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']



print(table[4][0])


def t_response(row,column, table):
    return table[column_names.index(column)][row_names.index(row)]

print(t_response('E','a',table))

def parse(input_tokens, table):
    stack = ['$']  # Initialize the stack with the dollar sign as the bottom marker
    stack.append('A')  # Push the starting symbol onto the stack
    input_index = 0  # Index to track the current input token

    print("Now testing: ",input_tokens)

    while stack:
        top_of_stack = stack[-1]  # Get the top of the stack
        current_input = input_tokens[input_index] if input_index < len(input_tokens) else None

        if top_of_stack in column_names:
            if top_of_stack == current_input:
                print("stack: ",stack)
                stack.pop()  # Matched terminal, pop it from the stack
                input_index += 1
            else:
                print("Error: Mismatch between stack and input")
                return False
        else:
            # Use the parsing table to determine the next action
            action = t_response(top_of_stack, current_input, table)

            if action is None:
                print("Error: No action found in the parsing table")
                return False
            else:
                stack.pop()  # Pop the non-terminal from the stack

                # Push the action's right-hand side onto the stack in reverse order
                for symbol in reversed(action):
                    if symbol != '':  # Skip empty symbols
                        stack.append(symbol)

    if input_index == len(input_tokens):
        print("Input successfully parsed")
        return True
    else:
        print("Error: Not all input tokens were consumed")
        return False

list_of_inputs = ['program f2023 ;','i*(i-i)$','i(i+i)$']

success = parse(list_of_inputs[0], table)
print(success)
#success = parse(list_of_inputs[1], table)
#print(success)
#success = parse(list_of_inputs[2], table)
#print(success)
