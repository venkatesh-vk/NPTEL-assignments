def primepartition(m):
    a=[]
    x=0
    for j in range(m+1):
        if j>1:
            for i in range(2,j):
                if(j%i==0):
                    break
            else:
                a.append(j)
    for i in range(len(a)):
        t=m-a[i]
        if(t in a):
                x=1
                return True
    if(x==0):
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
