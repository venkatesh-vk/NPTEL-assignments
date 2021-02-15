def rainaverage(l):
    a,s,c={},{},{}
    for i in l:
        c[i[0]] = 0
        s[i[0]] = 0
    for i in l:
        c[i[0]]+=1
    for i in l:
        s[i[0]] += i[1]
    for i in c.keys():
        a[i] = s[i]/c[i]
    b=sorted(a.items())
    return b
a=[]
def listtype(l):
  return(type(l) == type([]))
def flatten(l):
    global a
    for i in l:
        if(listtype(i)):
            flatten(i)
        else:
            a.append(i)
    return a
print(rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)]))
        
