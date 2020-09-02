def ekok(x, y):
    b=1
    a=0
    if (x>=y):
        k=x
        while(b==1):
            if(k%y==0):
                print("dur")
                print("döngü sayısı:", a)
                break
            else:
                k=((k/y)+1)*x
                a=a+1
ekok(32, 20)

