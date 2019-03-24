import random
global_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def right_swipe():
    
    global global_arr
    temp_arr=global_arr
    temp1_arr=global_arr
    for i in range(0,4,1):
        count=3;
        for j in range (3,-1,-1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[i][count]
                temp_arr[i][count]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1
    if right_swipe.counter%2==0:
        for i in range(0,4,1):
            for j in range (3,0,-1):
                if temp_arr[i][j]==temp_arr[i][j-1]:
                    temp_arr[i][j]+=temp_arr[i][j]
                    temp_arr[i][j-1]=0
        global_arr=temp_arr
        right_swipe.counter+=1
        right_swipe()
    elif right_swipe.counter%2==1: #and temp_arr!=temp1_arr:
    #if global_arr!=temp1_arr:
        x=random.randint(0,3)
        y=random.randint(0,3)
        while global_arr[x][y]!=0:
            x=random.randint(0,3)
            y=random.randint(0,3)
        z=random.randint(1,10)
        if z==10:
            global_arr[x][y]=4
        else:
            global_arr[x][y]=2
        right_swipe.counter-=1
        print(max(map(max,global_arr)))

def left_swipe():
    
    global global_arr
    temp_arr=global_arr
    temp1_arr=global_arr
    for i in range(0,4,1):
        count=3;
        for j in range (0,4,1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[i][3-count]
                temp_arr[i][3-count]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1
    if left_swipe.counter%2==0:
        for i in range(0,4,1):
            for j in range (0,3,1):
                if temp_arr[i][j]==temp_arr[i][j+1]:
                    temp_arr[i][j]+=temp_arr[i][j]
                    temp_arr[i][j+1]=0
        global_arr=temp_arr
        left_swipe.counter+=1
        left_swipe()
    else:
    #if global_arr!=temp1_arr:
        x=random.randint(0,3)
        y=random.randint(0,3)
        while global_arr[x][y]!=0:
            x=random.randint(0,3)
            y=random.randint(0,3)
        z=random.randint(1,10)
        if z==10:
            global_arr[x][y]=4
        else:
            global_arr[x][y]=2
        left_swipe.counter-=1
        print(max(map(max,global_arr)))

def up_swipe():
    
    global global_arr
    temp_arr=global_arr
    temp1_arr=global_arr
    for j in range(0,4,1):
        count=3;
        for i in range (0,4,1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[3-count][j]
                temp_arr[3-count][j]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1
    if up_swipe.counter%2==0:
        for j in range(0,4,1):
            for i in range (0,3,1):
                if temp_arr[i+1][j]==temp_arr[i][j]:
                    temp_arr[i][j]+=temp_arr[i][j]
                    temp_arr[i+1][j]=0
        global_arr=temp_arr
        up_swipe.counter+=1
        up_swipe()
    else:
    #if global_arr!=temp1_arr:
        x=random.randint(0,3)
        y=random.randint(0,3)
        while global_arr[x][y]!=0:
            x=random.randint(0,3)
            y=random.randint(0,3)
        z=random.randint(1,10)
        if z==10:
            global_arr[x][y]=4
        else:
            global_arr[x][y]=2
        up_swipe.counter-=1
        print(max(map(max,global_arr)))

def down_swipe():
    
    global global_arr
    temp_arr=global_arr
    temp1_arr=global_arr
    for j in range(0,4,1):
        count=3;
        for i in range (3,-1,-1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[count][j]
                temp_arr[count][j]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1
    if down_swipe.counter%2==0:
        for j in range(0,4,1):
            for i in range (3,-1,-1):
                if temp_arr[i-1][j]==temp_arr[i][j]:
                    temp_arr[i][j]+=temp_arr[i][j]
                    temp_arr[i-1][j]=0
        global_arr=temp_arr
        down_swipe.counter+=1
        down_swipe()
    else:
    #if global_arr!=temp1_arr:
        x=random.randint(0,3)
        y=random.randint(0,3)
        while global_arr[x][y]!=0:
            x=random.randint(0,3)
            y=random.randint(0,3)
        z=random.randint(1,10)
        if z==10:
            global_arr[x][y]=4
        else:
            global_arr[x][y]=2
        down_swipe.counter-=1
        print(max(map(max,global_arr)))
        
right_swipe.counter=0
left_swipe.counter=0
up_swipe.counter=0
down_swipe.counter=0
for i in range(0,2,1):
    xco=random.randint(0,3)
    yco=random.randint(0,3)
    if global_arr[xco][yco]!=0:
        i=0;
    else:
        val=random.randint(1,10)
        if val==10:
            global_arr[xco][yco]=4
        else:
            global_arr[xco][yco]=2;
 
for r in global_arr:
        for c in r:
            print(c,end = " ")
        print()
max_element=max(map(max,global_arr))
while max_element!=2048:
    swipe=input("Enter A/S/D/W")
    if swipe=='D':
        right_swipe()
    elif swipe=='A':
        left_swipe()
    elif swipe=='S':
        down_swipe()
    elif swipe=='W':
        up_swipe()
    for r in global_arr:
        for c in r:
            print(c,end = " ")
        print()
if max_element==2014:
    print("YOU WON")
        
        
    
    
