def chessBoardCellColor(cell1, cell2):
    black = ['a1','c1','e1','g1','b2','d2','f2','h2','a3','c3','e3','g3','b4','d4','f4','h4''a5','c5','e5','g5','b6','d6','f6','h6','a7','c7','e7','g7','b8','d8','f8','h8']
    white = ['a2','c2','e2','g2','b1','d1','f1','h1','a4','c4','e4','g4','b3','d3','f3','h3''a6','c6','e6','g6','b5','d5','f5','h5','a8','c8','e8','g8','b7','d7','f7','h7']
    
    if (cell1.lower() in black and cell2.lower() in black):
        return True
    elif(cell1.lower() in white and cell2.lower() in white):
        return True
    
    else:
        return False


"not at all good coding standards...focused on finishing the objective"
