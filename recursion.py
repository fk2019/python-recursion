def move(f,t):
    print(f' Move from {f} to {t}')

# move('A','B')
def moveVia(f,v,t):
    move(f,v)
    move(v,t)

moveVia('A','B','C')
