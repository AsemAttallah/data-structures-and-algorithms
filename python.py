y=[2,5,9,8,78]


def reverseArray(x):
    g=[]
    for i in range(len(x)):
        g.append(x[len(x)-1-i])
    return g
    
print(reverseArray(y))