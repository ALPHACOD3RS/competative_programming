def mySol(n):
    y = []
    b= ''
    for i in range(1, n+1 ):
        y.append(i)
    b = ''.join([str(x) for x in y])
    
    print(b)
    

if __name__ == '__main__':
    n = int(input())
    mySol(n)

