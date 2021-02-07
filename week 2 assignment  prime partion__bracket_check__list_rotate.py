def isP(n):
    if n==2:
        return True
    if n%2==0:
        return False
    return all(n%x>0 for x in range(3, int(n**0.5)+1, 2))
 
def genP(n):
    p = [2]
    p.extend([x for x in range(3, n+1, 2) if isP(x)])
    return p
def primepartition(n):
    p = genP(n)
    for i in range(0,len(p)):
        for j in range(0,len(p)):
            if p[i]+p[j]==n:
                return True
    return False
def matched(s):
    t=0
    x=0
    for i in s:
        if(i=='('):
            t+=1
            x=1
        if(i==')'):
            t-=1
            if(x==0):
                break
    if(t==0):
        return True
    else:
        return False

def rotatelist(l,k):
    a=l[:]
    while k>0:
        t=a.pop(0)
        a.append(t)
        k-=1
    else:
        return(a)
