import matrix as m

def test():

    m1 = m.Matrix([
        [1,2,3],
        [4,5,6]
        ])

    m2 = m.Matrix([
        [7,-2],
        [-3,-5],
        [4,1]
        ])

    m1_x_m2 = m.Matrix([
        [ 13,  -9],
        [ 37, -27]])

    assert equal(m1 * m2, m1_x_m2), "Error in your __mul__ function"

def equal(m1, m2):
    if len(m1.g) != len(m2.g): return False
    if len(m1.g[0]) != len(m2.g[0]): return False
    for r1, r2 in zip(m1.g, m2.g):
        for v1, v2 in zip(r1, r2):
            if abs(v1 - v2) > 0.0001:
                return False
    return True   
    
test()
