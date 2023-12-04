class ParsingTable:
    def __init__(self):
        self.parse_table = [[0] * 32 for _ in range(22)]
        for i in range(22):
            self.parse_table[i][0] = 0
        for i in range(32):
            self.parse_table[0][i] = 0
#31 x axis
#20 y axis

# a b c d w f + - ( ) * / 1 2 3 4 5 6 7 8 9 $ ; program(res word) var(res word) begin(res word) end(res word) interger (res word) interger(res word) Write(res word) "value=",
#31

#NON TERMS P,I,PI,DL,D,TYPE,SL,S,W,STR,AS,E,Q,T,R,F,N,DIG, DIG',SIGN,LETTER
#21 

#
#prog
            self.parse_table[1][24] = 1 #program

            #identifier
            self.parse_table[2][1] = 21 #LETTER a   
            self.parse_table[2][2] = 22 #LETTER b
            self.parse_table[2][3] = 23 #LETTER c
            self.parse_table[2][4] = 24 #LETTER d
            self.parse_table[2][5] = 25 #LETTER w 
            self.parse_table[2][6] = 26 #LETTER f

            #post identifier
            self.parse_table[3][1] = 31 #LETTER a
            self.parse_table[3][2] = 32 #LETTER b
            self.parse_table[3][3] = 33 #LETTER c
            self.parse_table[3][4] = 34 #LETTER d
            self.parse_table[3][5] = 35 #LETTER w 
            self.parse_table[3][6] = 36 #LETTER f

            self.parse_table[3][13] = 313 #DIG PI
            self.parse_table[3][14] = 314 #DIG PI 
            self.parse_table[3][15] = 315 #DIG PI 
            self.parse_table[3][16] = 316 #DIG PI 
            self.parse_table[3][17] = 317 #DIG PI 
            self.parse_table[3][18] = 318 #DIG PI 
            self.parse_table[3][19] = 319 #DIG PI 
            self.parse_table[3][20] = 320 #DIG PI 
            self.parse_table[3][21] = 321 #DIG PI

            #check if lambda only leads to + - 1 because it leads to <identifier> which also has a-f and 0-9
            #lambda is incremented by an extra 300 just for visibility
            self.parse_table[3][7] = 307 #lambda +
            self.parse_table[3][8] = 308 #lambda -
            self.parse_table[3][11] = 311 #lambda *


            #dec-list
            self.parse_table[4][1] = 41 #LETTER a D
            self.parse_table[4][2] = 42 #LETTER b D
            self.parse_table[4][3] = 43 #LETTER c D
            self.parse_table[4][4] = 44 #LETTER d D
            self.parse_table[4][5] = 45 #LETTER w D
            self.parse_table[4][6] = 46 #LETTER f D

            #dec
            self.parse_table[5][1] = 51 #LETTER a I
            self.parse_table[5][2] = 52 #LETTER b I
            self.parse_table[5][3] = 53 #LETTER c I
            self.parse_table[5][4] = 54 #LETTER d I
            self.parse_table[5][5] = 55 #LETTER w I
            self.parse_table[5][6] = 56 #LETTER f I

            #type
            self.parse_table[6][29] = 6291 #interger(res word)

            #stat-list 
            self.parse_table[7][1] = 71 # S on all letters below
            self.parse_table[7][2] = 72
            self.parse_table[7][3] = 73
            self.parse_table[7][4] = 74
            self.parse_table[7][5] = 75
            self.parse_table[7][6] = 76

            #stat
            self.parse_table[8][1] = 81 #AS on all letters below
            self.parse_table[8][2] = 82
            self.parse_table[8][3] = 83
            self.parse_table[8][4] = 84
            self.parse_table[8][5] = 85
            self.parse_table[8][6] = 86

            #write
            self.parse_table[9][30] = 930 # reserved word for write 

            #str
            #lambda on all letters
            self.parse_table[10][1] = 101 #λ
            self.parse_table[10][2] = 102 #λ
            self.parse_table[10][3] = 103 #λ
            self.parse_table[10][4] = 104 #λ
            self.parse_table[10][5] = 105 #λ
            self.parse_table[10][6] = 106 #λ
            self.parse_table[10][31] = 1031 #value reserved word

            #assign
            self.parse_table[11][1] = 111 #I=E 
            self.parse_table[11][2] = 112 #I=E
            self.parse_table[11][3] = 113 #rest are I=E as well
            self.parse_table[11][4] = 114
            self.parse_table[11][5] = 115
            self.parse_table[11][6] = 116

            #expr
            self.parse_table[12][1] = 121 # TE' or TQ or X Q
            self.parse_table[12][2] = 122
            self.parse_table[12][3] = 123 
            self.parse_table[12][4] = 124
            self.parse_table[12][5] = 125
            self.parse_table[12][6] = 126

            #expr' or Q 
            self.parse_table[13][7] = 137 #+TE on +
            self.parse_table[13][8] =  138 #-TE on -
            self.parse_table[13][23] = 1331 #λ ON ;

            #term
            self.parse_table[14][1] = 141 #FT' on each letter
            self.parse_table[14][2] = 142
            self.parse_table[14][3] = 143
            self.parse_table[14][4] = 144
            self.parse_table[14][5] = 145
            self.parse_table[14][6] = 146

            #term' or R  
            # *FT /FT and lambda at the end 
            self.parse_table[15][11] = 1511 
            self.parse_table[15][12] = 1512
            self.parse_table[15][23] = 1523

            #factor
            #a-f for I or <identifier> 
            self.parse_table[16][1] = 161
            self.parse_table[16][2] = 162
            self.parse_table[16][3] = 163
            self.parse_table[16][4] = 164
            self.parse_table[16][5] = 165
            self.parse_table[16][6] = 166
            #9 is (E) for ( 
            self.parse_table[16][9] = 169

            #number
            #+TE' and -TE'
            self.parse_table[17][7] = 177
            self.parse_table[17][8] = 178
            #λ on ; and Write (res word)
            self.parse_table[17][23] = 1723
            self.parse_table[17][29] = 1729




            #digit
            #1-9 for 1-9 
            self.parse_table[18][1] = 181
            self.parse_table[18][2] = 182
            self.parse_table[18][3] = 183  
            self.parse_table[18][4] = 184
            self.parse_table[18][5] = 185
            self.parse_table[18][6] = 186
            self.parse_table[18][7] = 187
            self.parse_table[18][8] = 188
            self.parse_table[18][9] = 189

            #digit'lambda
            #
            #
            #
            #
            #double check this one 
            self.parse_table[19][23] =  1923 #lambda ??? on 

            #sign
            #lambda on all digits
            #from First of DIG (gets above the first)
            #+ - lambda
            #both + and -
            self.parse_table[20][7] = 207
            self.parse_table[20][8] = 208

            self.parse_table[20][13] = 2013 #lambda
            self.parse_table[20][14] = 2014 # 
            self.parse_table[20][15] = 2015 # 
            self.parse_table[20][16] = 2016 # 
            self.parse_table[20][17] = 2017 # 
            self.parse_table[20][18] = 2018 # 
            self.parse_table[20][19] = 2019 # 
            self.parse_table[20][20] = 2020 # 
            self.parse_table[20][21] = 2021 #

            #letter
            #a-f
            self.parse_table[21][1] = 211
            self.parse_table[21][2] = 212
            self.parse_table[21][3] = 213
            self.parse_table[21][4] = 214
            self.parse_table[21][5] = 215
            self.parse_table[21][6] = 216




#        self.parse_table[1][1] = 1 #S -> a=E = 1 
    
#        self.parse_table[2][2] = 21 # E -> TQ 
#        self.parse_table[2][3] = 22 # E-> TQ 
#        self.parse_table[2][8] = 23 # E -> TQ


#        self.parse_table[3][4] = 31 # Q -> +tq 
#        self.parse_table[3][5] = 32 # Q -> -tq 
#        self.parse_table[3][9] = 100 # q -> ^lambda
#        self.parse_table[3][10] = 101 # q -> ^lambda


#        self.parse_table[4][2] = 41 # T ->FR 
#        self.parse_table[4][3] = 42 #T -> *FR 
#        self.parse_table[4][8] = 43 # -> ^ lambda 


#        self.parse_table[5][4] = 102 #R -> *FR
#        self.parse_table[5][5] = 103 #R -> /FR 
#        self.parse_table[5][6] = 51 #R -> ^ lambda
#        self.parse_table[5][7] = 52 #R -> ^ lambda
#        self.parse_table[5][9] = 104 #R -> ^ lambda
#        self.parse_table[5][10] = 105 #R -> ^ lambda


        
#        self.parse_table[6][2] = 200 #F -> a
 #       self.parse_table[6][3] = 201 #F -> b 
  #      self.parse_table[6][8] = 202 #F->(E)

def get(self, row, col):
        return self.parse_table[row][col]

#
#def convert_to_row(c):
#    if c == 'S':
#        return 1
#    elif c == 'E':
#        return 2
#    elif c == 'Q':
#        return 3
#    elif c == 'T':
#        return 4
#    elif c == 'R':
#        return 5
#    elif c == 'F':
#        return 6
#    else:
#        return 0

def convert_to_row(c):
    if c == 'P':
        return 1
    elif c == 'I':
        return 2
    elif c == 'PI':
        return 3
    elif c == 'DL':
        return 4
    elif c == 'D':
        return 5
    elif c == 'TYPE':
        return 6
    elif c == 'SL':
        return 7
    elif c == 'S':
        return 8
    elif c == 'W':
        return 9
    elif c == 'STR':
        return 10
    elif c == 'AS':
        return 11
    elif c == 'E':
        return 12
    elif c == 'Q':
        return 13
    elif c == 'T':
        return 14
    elif c == 'R':
        return 15
    elif c == 'F':
        return 16
    elif c == 'N':
        return 17
    elif c == 'DIG':
        return 18
    elif c == 'S':
        return 19
    elif c == 'E':
        return 20
    elif c == 'Q':
        return 21

    else:
        return 0


def convert_to_col(c):
    if c == '@':
        return 1
    elif c == 'a':
        return 2
    elif c == 'b':
        return 3
    elif c == 'c':
        return 4
    elif c == 'd':
        return 5
    elif c == 'w':
        return 6
    elif c == 'f':
        return 7
    elif c == '+':
        return 8
    elif c == '-':
        return 9
    elif c == '(':
        return 10
    elif c == ')':
        return 11
    elif c == '*':
        return 12
    elif c == '/':
        return 13
    elif c == '1':
        return 14
    elif c == '2':
        return 15
    elif c == '3':
        return 16
    elif c == '4':
        return 17
    elif c == '5':
        return 18
    elif c == '6':
        return 19
    elif c == '7':
        return 20
    elif c == '8':
        return 21
    elif c == '9':
        return 22
    elif c == '$':
        return 23
    elif c == ';':
        return 24
    elif c == 'program':
        return 25
    elif c == 'var':
        return 26
    elif c == 'begin':
        return 27
    elif c == 'end':
        return 28
    elif c == 'interger':
        return 29
    elif c == 'write':
        return 30
    elif c == '"value=",':
        return 31

    else:
        return 0



def push_back_to_stack(st, x):
    if x == 0:
        return False
    # checks for the a = E and pushes onto stack returns true to continue
    if x == 1:
        print("Pushing a=E onto the stack.")
        st.append('E')
        st.append('@')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    # checks for the TQ and pushes onto stack true to continue
    elif x == 21 or x == 22 or x == 23:
        print("Pushing TQ onto the stack.")
        st.append('Q')
        st.append('T')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()

        return True
    elif x == 31:
        print("Pushing +TQ onto the stack.")
        st.append('Q')
        st.append('T')
        st.append('+')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    elif x == 32:
        print("Pushing -TQ onto the stack.")
        st.append('Q')
        st.append('T')
        st.append('-')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    elif x == 100 or x == 101 or x == 102 or x == 103 or x == 104 or x == 105:
        print("Pushing ^ (Lambda) onto the stack.")
        st.append('^')  # ^ -> lambda
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    elif x == 41 or x == 42 or x == 43:
        print("Pushing FR onto the stack.")
        st.append('R')
        st.append('F')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    elif x == 51:
        print("Pushing *FR onto the stack.")
        st.append('R')
        st.append('F')
        st.append('*')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    elif x == 52:
        print("Pushing /FR onto the stack.")
        st.append('R')
        st.append('F')
        st.append('/')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    elif x == 200:
        print("Pushing 'a' onto the stack.")
        st.append('a')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    elif x == 201:
        print("Pushing b onto the stack.")
        st.append('b')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    elif x == 202:
        print("Pushing (E) onto the stack.")
        st.append(')')
        st.append('E')
        st.append('(')
        print("Current stack:", end=' ')
        for item in st:
            print(item, end=' ')
        print()
        return True
    else:
        return False


def main():
    parse_table = ParsingTable()
    #
    #
    #     1. read from final23.txt
    #
    #     2. update logic 
    #       
    #


    input_string = input("Enter string: ")

    # char to hold position
    state = ''

    # check to see if input is valid
    accepted = True

    # initalized list to start off on
    st = ['$', 'S']

    # gets input
    print("Input string:", input_string)
    while len(st) > 0:
        state = st[-1]

        # read the input and puts the next character
        input_char = input_string[0]

        next_char = input_string[1] if len(input_string) > 1 else ''
        if next_char == '=':
            input_char = '@'

        # pop from stack if lambda
        if state == '^':
            print("Popping ^ (Lambda) from the stack.")
            st.pop()
            print("Current stack:", end=' ')
            for item in st:
                print(item, end=' ')
            print()

        # checks everything else that isnt $ and pops, also checks input_char to see if it needs to be rejected or accepted
        elif state in '@abcdwf+()$-*/123456789;':
            if state == input_char:
                if state == '@':
                    # pop to check for @
                    print("Popping from stack: @(a=)")
                    st.pop()
                    input_string = input_string[2:]
                else:
                    print("Popping from stack:", st[-1])
                    st.pop()
                    input_string = input_string[1:]
                print("Input:", input_string)
            else:
                print("Rejected.")
                accepted = False
                break

        # If state is non-terminal  then retrieve the states from the parsing table.

        # If state is non-term then pop and push
        elif state in 'SETQFR':
            row = convert_to_row(state)
            col = convert_to_col(input_char)
            new_state = parse_table.get(row, col)
            print("Popping from stack:", st[-1])
            st.pop()
            print("Current stack:", end=' ')
            for item in st:
                print(item, end=' ')
            print()
            if not push_back_to_stack(st, new_state):
                accepted = False
                break

    if accepted:
        print("accepted")
    else:
        print("rejected")


if __name__ == '__main__':
    main()