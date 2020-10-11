'''
Function that computes the determinant of a matrix m 

'''
def gettwobytwo(m,a,b):

    return [row[:b] + row[b+1:] for row in (m[:a]+m[a+1:])] # returns  

def getMatrixDeternminant(m):

    ret=0

    if len(m) == 2:
        ret = m[0][0]*m[1][1]-m[0][1]*m[1][0] # Computes determinant of two by two matrix
        return ret

    determinant = 0 

    for i in range(len(m)):
        determinant += ((-1)**i)*m[0][i]*getMatrixDeternminant(gettwobytwo(m,0,i)) # Adds and subtracts the determinant of the 2 by 2 according to iteration
        
    return determinant # Returns determinant 
