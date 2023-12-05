table = [
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'programBDG',None,None,None,None,None,None],#A program
        ['TC','TC','TC','TC','TC','TC',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #B Identifier
        ['TC','TC','TC','TC','TC','TC','','',None,None,'',None,'SC','SC','SC','SC','SC','SC','SC','SC','SC',None,None,None,None,None,None,None,None,None], #C Post Identifier
        ['E','E','E','E','E','E',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #D dec-list
        ['B','B','B','B','B','B',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #E dec
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'integer',None,None], #F type
        ['H','H','H','H','H','H',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #G stat-list
        ['K','K','K','K','K','K',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #H stat
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'write',None], #I write
        ['','','','','','',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'"value="'], #J string
        ['B=L','B=L','B=L','B=L','B=L','B=L',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #K assign
        ['NM','NM','NM','NM','NM','NM',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #Lexpression
        [None,None,None,None,None,None,'+NM','-NM',None,None,None,None,None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,None], #M expression'
        ['PO','PO','PO','PO','PO','PO',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #N term
        [None,None,None,None,None,None,None,None,None,None,'*PO','/PO',None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,''], #O term'
        ['I','I','I','I','I','I',None,None,"(L)",None,None,None,'Q','Q','Q','Q','Q','Q','Q','Q','Q',None,None,None,None,None,None,None,None,None], #P factor
        [None,None,None,None,None,None,'R','R',None,None,None,None,None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,''], #Q number
        [None,None,None,None,None,None,'+','-',None,None,None,None,'','','','','','','','','',None,None,None,None,None,None,None,None,None], #R sign
        [None,None,None,None,None,None,None,None,None,None,None,None,'1','2','3','4','5','6','7','8','9',None,None,None,None,None,None,None,None,None], #S digit
        ['a','b','c','d','w','f',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #T letter
        ]

h7_column_names = ['i','+','-','*','/','(',')','$']
h7_row_names = ['E','Q','T','R','F']

h7_table = [ 
        ["TQ",None,None,None,None,"TQ",None,None],
        [None,"+TQ","-TQ",None,None,None,"",""],
        ["FR",None,None,None,None,"FR",None,None],
        [None,"","" ,"*FR","/FR",None,"",""],
        ["i",None,None,None,None,"(E)",None,None]
]