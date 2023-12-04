table = [
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'program',None,None,None,None,None,None],#program
        ['TC','TC','TC','TC','TC','TC',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #Identifier
        ['TC','TC','TC','TC','TC','TC','','',None,None,'',None,'SC','SC','SC','SC','SC','SC','SC','SC','SC',None,None,None,None,None,None,None,None,None], #Post Identifier
        ['E','E','E','E','E','E',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #dec-list
        ['B','B','B','B','B','B',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #dec
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'integer',None,None], #type
        ['H','H','H','H','H','H',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #stat-list
        ['K','K','K','K','K','K',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #stat
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'write',None], #write
        ['','','','','','',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'"value="'], #string
        ['B=L','B=L','B=L','B=L','B=L','B=L',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #assign
        ['NM','NM','NM','NM','NM','NM',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #expression
        [None,None,None,None,None,None,'+NM','-NM',None,None,None,None,None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,None], #expression'
        ['PO','PO','PO','PO','PO','PO',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #term
        [None,None,None,None,None,None,None,None,None,None,'*PO','/PO',None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,''], #term'
        ['I','I','I','I','I','I',None,None,"(L)",None,None,None,'Q','Q','Q','Q','Q','Q','Q','Q','Q',None,None,None,None,None,None,None,None,None], #factor
        [None,None,None,None,None,None,'R','R',None,None,None,None,None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,''], #number
        [None,None,None,None,None,None,'+','-',None,None,None,None,'','','','','','','','','',None,None,None,None,None,None,None,None,None], #sign
        [None,None,None,None,None,None,None,None,None,None,None,None,'1','2','3','4','5','6','7','8','9',None,None,None,None,None,None,None,None,None], #digit
        ['a','b','c','d','w','f',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #letter
        ]
