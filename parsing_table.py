table = [

#         a   b    c     d   w    f    +    -     (    )    *   /    0     1    2   3    4     5   6    7     8    9     $   ;    prog     var  beg  end   int  wri "value="                
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'program',None,None,None,None,None,None],#program = A
        ['TC','TC','TC','TC','TC','TC',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #Identifier = B
        ['TC','TC','TC','TC','TC','TC','','',None,None,'',None,'SC','SC','SC','SC','SC','SC','SC','SC','SC','SC',None,None,None,None,None,None,None,None,None], #Post Identifier = C 
        ['E','E','E','E','E','E',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #dec-list = D
        ['B','B','B','B','B','B',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #dec = E
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'integer',None,None], #type = F
        ['H','H','H','H','H','H',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #stat-list = G
        ['K','K','K','K','K','K',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #stat = H 
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'write',None], #write = I 
        ['','','','','','',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'"value="'], #string = J
        ['B=L','B=L','B=L','B=L','B=L','B=L',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #assign = K 
        ['NM','NM','NM','NM','NM','NM',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #expression = L 
        [None,None,None,None,None,None,'+NM','-NM',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,None], #expression' = M 
        ['PO','PO','PO','PO','PO','PO',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #term= N
        [None,None,None,None,None,None,None,None,None,None,'*PO','/PO',None,None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,''], #term' = O
        ['I','I','I','I','I','I',None,None,"(L)",None,None,None,'Q''Q','Q','Q','Q','Q','Q','Q','Q','Q',None,None,None,None,None,None,None,None,None], #factor = P 
        [None,None,None,None,None,None,'R','R',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'',None,None,None,None,None,None,''], #number = Q
        [None,None,None,None,None,None,'+','-',None,None,None,None,'','','','','','','','','','',None,None,None,None,None,None,None,None,None], #sign 
        [None,None,None,None,None,None,None,None,None,None,None,None,'0','1','2','3','4','5','6','7','8','9',None,None,None,None,None,None,None,None,None], #digit
        ['a','b','c','d','w','f',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #letter
        ]
