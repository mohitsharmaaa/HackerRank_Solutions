a=[[1,2,3,4],[14,15,16,5],[13,20,17,6],[12,19,18,7],[11,10,9,8]]
r=5
c=4
n=r*c
count=1
x,y=0,-1
i,j=0,0
print(a[i][j],end=" ")
a[i][j]=True
while(count!=n):
    if(i==x):
        if(j>y):
            if(j+1<c and a[i][j+1]!=True):
                y==j
                j+=1
            else:
                y=j
                i+=1
        else:
            if(j-1>-1 and a[i][j-1]!=True):
                y=j
                j-=1
            else:
                y=i
                i-=1
    else:
        if(i>x):
            if(i+1<r and a[i+1][j]!=True):
                x=i
                i+=1
            else:
                x=i
                j-=1
        else:
            if(i-1>-1 and a[i-1][j]!=True):
                x=i
                i-=1
            else:
                x=i
                y=j
                j+=1
    #print("x ="+str(x)+"  y ="+str(y)+"  i ="+str(i)+"  j ="+str(j),end="  ")
    print(a[i][j],end=" ")
    a[i][j]=True
    count+=1              


                                         



