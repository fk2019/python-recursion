def move(f,t):
    print(f' Move from {f} to {t}')

# move('A','B')
def hanoi(n,f,v,t):
    if n==0:
        pass
    else:
        hanoi(n-1,f,t,v)
        move(f,t)
        hanoi(n-1,v,f,t)


hanoi(3,'A','B','C')