def table(n):
    l=[]
    for x in range(0,n):
        tmp=[]
        for y in range(0,n):
            tmp.append(x*y%n)
        l.append(tmp)

    return l

def inverse(n,m):
    lt=[]
    l=table(n)
    
    for x in l[m]:
        if x==0:
            return l.index(l[m])


def divis_pos(n):
    l=[]
    for x in range(1,n):
        if n%x == 0:
            l.append(x)

    return l

def pgcd(a,b):
    la=divis_pos(a)
    lb=divis_pos(b)

    lc=[]
    for x in la:
        for y in lb:
            if x==y:
                lc.append(x)

    return max(lc)
