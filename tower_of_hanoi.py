def TOH(n,s,a,d):
    if n==1:
        print("from",s,"to",d)
    else:
        TOH(n-1,s,d,a)
        print("from",s,"to",d)
        TOH(n-1,a,s,d)
TOH(4,"A","B","C")