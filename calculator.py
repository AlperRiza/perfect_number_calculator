c=0 
x=2
a=1
while x<10000:
    while x/2>=a:
        if x%a==0:
            c=c+a
            a+=1
        else:
            a+=1
    if x==c:
        print(x)
        x+=2
        c=0
        a=1
    else:
        x+=2
        c=0
        a=1
