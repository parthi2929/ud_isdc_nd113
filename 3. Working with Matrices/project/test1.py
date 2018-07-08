import matrix as m

def test():

    m1_x_m2 = m.Matrix([
        [ 13,  -9],
        [ 37, -27]])
    m1_m2_inv = m.Matrix([
        [1.5, -0.5],
        [2.0555556, -0.722222222]
        ])
    #assert (   4*m.identity(5)).trace() == 20 , "Error in your trace function" 
    #assert (4*m.identity(5)).trace() == 20 , "Error in your trace function" 
    #assert equal(m1_x_m2.inverse(), m1_m2_inv), """Error in your inverse function for the 1 x 1 case"""
    for i in range(1,-1,-1):
        for j in range(1,-1,-1):
            print(i,j)

def equal(m1, m2):
    if len(m1.g) != len(m2.g): return False
    if len(m1.g[0]) != len(m2.g[0]): return False
    for r1, r2 in zip(m1.g, m2.g):
        for v1, v2 in zip(r1, r2):
            if abs(v1 - v2) > 0.0001:
                return False
    return True

test()
