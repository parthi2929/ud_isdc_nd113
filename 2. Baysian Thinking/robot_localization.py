#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.

p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
factors = [pMiss, pHit, pHit, pMiss, pMiss]

for each_index in range(len(p)):
    p[each_index] = p[each_index]*factors[each_index]
#print(p)


p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red','green']
pHit = 0.6
pMiss = 0.2
def sense(p, Z):
    """
    p = initial probability distribution list
    Z = each measurement
    q = new normalized distribution list
    """
    q = []
    for each_index in range(len(p)):
        if (world[each_index] == Z):
            q.append(p[each_index]*pHit)
        else:
            q.append(p[each_index]*pMiss)
    total = sum(q)
    q = [ x/total for x in q]
    return q

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
def move(p, U):
    """
    p = given probability distribution list
    U = amount of steps robot has moved to right (assumed as right for now)
    """
    
    #q = np.roll(p,U)   #hav to find a way without using numpy
    # EXACT MOTION
    # q = [ x for x in p ]
    # for i in range(U):
    #     temp = q[-1]
    #     q[1:]= q[:-1]
    #     q[0]=temp
    # return q

    # INEXACT MOTION
    q = [ 0 for _ in p ]
    temp = [pUndershoot, pExact, pOvershoot]

    # q[1] = p[0]*temp[0] + q[1]
    # q[2] = p[0]*temp[1] + q[2]
    # q[3] = p[0]*temp[2] + q[3]   

    # q[2] = p[1]*temp[0] + q[2]
    # q[3] = p[1]*temp[1] + q[3]
    # q[4] = p[1]*temp[2] + q[4]

    # q[3] = p[2]*temp[0] + q[3]
    # q[4] = p[2]*temp[1] + q[4]
    # q[0] = p[2]*temp[2] + q[0]

    # q[4] = p[3]*temp[0] + q[4]
    # q[0] = p[3]*temp[1] + q[0]
    # q[1] = p[3]*temp[2] + q[1]

    # q[0] = p[4]*temp[0] + q[0]
    # q[1] = p[4]*temp[1] + q[1]
    # q[2] = p[4]*temp[2] + q[2]

    for i in range(len(p)):

        undershoot_index    = (i + (U-1)) % len(p)
        exact_index         = (i + (U)) % len(p)
        overshoot_index     = (i + (U+1)) % len(p)

        #print(i , undershoot_index , exact_index, overshoot_index, q)

        q[ undershoot_index ]   = p[i]*temp[0] + q[ undershoot_index ]
        q[ exact_index ]        = p[i]*temp[1] + q[ exact_index ]
        q[ overshoot_index ]    = p[i]*temp[2] + q[ overshoot_index ]
    return q

for each_index in range(len(measurements)):
    p = sense(p, measurements[each_index])

p=[1, 0, 0, 0, 0]

print(move(p,2))

# uniform distribution eventuality test in case of inexact move, Try different U
for i in range(1000):
    p = move(p,1)
print(p)