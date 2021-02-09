import copy
def remdup(l):
    a=[]
    l.reverse()
    for i in l:
        if i not in a:
            a.append(i)
    a.reverse()
    return (a)

def splitsum(l):
    s=0
    c=0
    for i in l:
        if(i>=0):
            s=s+(i**2)
        else:
            c+=(i**3)
    return([s,c])

def matrixflip(m,d):
    a=copy.deepcopy(m)
    if(d in ['h','v']):
        if(d=='h'):
            for i in a:
                i.reverse()
            return(a)
        else:
            a.reverse()
            return(a)
    else:
        return(m)
