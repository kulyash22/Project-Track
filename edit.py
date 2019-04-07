import pygame
import random
import math
global_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
temp1_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
win=pygame.display.set_mode((655,655))

clock = pygame.time.Clock()

pygame.display.set_caption("4X4 2048 by kulyash")

def hint():

    global global_arr
    temp2_arr=global_arr
    #print("temp is",temp_arr)
    #print(temp2_arr)   #remove
    print("temp",temp2_arr) #rem
    right_swipe()
    print("temp",temp2_arr) #rem
    a=max(map(max,global_arr))
    print("temp",temp2_arr) #rem
    countmax1=0
    print("temp",temp2_arr) #rem
    for i in range(0,4,1):
        for j in range(0,4,1):
            if global_arr[i][j]==max(map(max,global_arr)) and ((i==0 and j==0) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==0)):
                countmax1=10
                print("temp",temp2_arr) #rem
    count1=0
    print("temp",temp2_arr) #rem
    for i in range(0,4,1):
        for j in range(0,4,1):
            if global_arr[i][j]!=0:
                count1+=1
                print("temp",temp2_arr) #rem
    count1=16-count1
    print("temp",temp2_arr) #rem
    global_arr = temp2_arr
    print("orig", global_arr)           #remoes
    left_swipe()
    b=max(map(max,global_arr))
    countmax2=0
    for i in range(0,4,1):
        for j in range(0,4,1):
            if global_arr[i][j]==max(map(max,global_arr)) and ((i==0 and j==0) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==0)):
                countmax2=10
    count2=0
    for i in range(0,4,1):
        for j in range(0,4,1):
            if global_arr[i][j]!=0:
                count2+=1
    count2=16-count2
    global_arr=temp2_arr
    up_swipe()
    c=max(map(max,global_arr))
    countmax3=0
    for i in range(0,4,1):
        for j in range(0,4,1):
            if global_arr[i][j]==max(map(max,global_arr)) and ((i==0 and j==0) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==0)):
                countmax3=10
    count3=0
    for i in range(0,4,1):
        for j in range(0,4,1):
            if global_arr[i][j]!=0:
                count3+=1
    count3=16-count3
    global_arr=temp2_arr
    down_swipe()
    d=max(map(max,global_arr))
    countmax4=0
    for i in range(0,4,1):
        for j in range(0,4,1):
            if global_arr[i][j]==max(map(max,global_arr)) and ((i==0 and j==0) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==0)):
                countmax4=10
    count4=0
    for i in range(0,4,1):
        for j in range(0,4,1):
            if global_arr[i][j]!=0:
                count4+=1
    count4=16-count4
    global_arr=temp2_arr

    score = [0,0,0,0]
    score[0]=math.log(a,2)+count1+countmax1
    score[1]=math.log(b,2)+count2+countmax2
    score[2]=math.log(c,2)+count3+countmax3
    score[3]=math.log(d,2)+count4+countmax4
    if max(score)==score[0]:
        print("D")
    elif max(score)==score[1]:
        print("A")
    elif max(score)==score[2]:
        print("W")
    elif max(score)==score[3]:
        print("S")

def toprint():
    global global_arr
    #pygame.display.flip()
    for j in range(0,4,1):
        for k in range(0,4,1):
            if global_arr[j][k]==2:
                p1=pygame.image.load("2.png")
                win.blit(p1,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==4:
                p2=pygame.image.load("4.png")
                win.blit(p2,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==8:
                p3=pygame.image.load("8.png")
                win.blit(p3,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==16:
                p4=pygame.image.load("16.png")
                win.blit(p4,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==32:
                p5=pygame.image.load("32.png")
                win.blit(p5,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==64:
                p6=pygame.image.load("64.png")
                win.blit(p6,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==128:
                p7=pygame.image.load("128.png")
                win.blit(p7,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==256:
                p8=pygame.image.load("256.png")
                win.blit(p8,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==512:
                p9=pygame.image.load("512.png")
                win.blit(p9,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==1024:
                p10=pygame.image.load("1024.png")
                win.blit(p10,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==2048:
                p11=pygame.image.load("2048.png")
                win.blit(p11,(20+k*155,20+j*155))
                pygame.display.update()
            elif global_arr[j][k]==0:
                pygame.draw.rect(win,(255,205,210),(20+k*155,20+j*155,150,150))
                pygame.display.update()

def right_swipe():

    global global_arr
    global temp1_arr
    temp_arr=global_arr

    for i in range(0,4,1):
        count=3;
        for j in range (3,-1,-1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[i][count]
                temp_arr[i][count]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1

    #kul=0
    if right_swipe.counter%2==0:
        temp1_arr=global_arr
        for i in range(0,4,1):
            for j in range (3,0,-1):
                if temp_arr[i][j]==temp_arr[i][j-1]:
                    temp_arr[i][j]+=temp_arr[i][j]
                    temp_arr[i][j-1]=0

        right_swipe.counter+=1

        #kul=0
        for m in range(0,4,1):
            for n in range(0,4,1):
                if temp1_arr[m][n]!=temp_arr[m][n]:
                    right_swipe.kul=1

        global_arr=temp_arr
        right_swipe()
    elif right_swipe.counter%2==1: #and right_swipe.kul!=0:
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
        right_swipe.kul=0
        #print(max(map(max,global_arr)))
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
        for m in range(0,4,1):
            for n in range(0,4,1):
                if temp1_arr[m][n]!=temp_arr[m][n]:
                    left_swipe.kul=1
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
        left_swipe.kul=0
        #print(max(map(max,global_arr)))
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
        for m in range(0,4,1):
            for n in range(0,4,1):
                if temp1_arr[m][n]!=temp_arr[m][n]:
                    up_swipe.kul=1
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
        up_swipe.kul=0
        #print(max(map(max,global_arr)))
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
        for m in range(0,4,1):
            for n in range(0,4,1):
                if temp1_arr[m][n]!=temp_arr[m][n]:
                    down_swipe.kul=1
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
        down_swipe.kul=0
        #print(max(map(max,global_arr)))
def main():
    #pygame.event.pump()
    global global_arr
    pygame.draw.rect(win,(255,205,210),(20,20,615,615))
    pygame.draw.rect(win,(0,0,0),(170,20,5,615))
    pygame.draw.rect(win,(0,0,0),(325,20,5,615))
    pygame.draw.rect(win,(0,0,0),(480,20,5,615))
    pygame.draw.rect(win,(0,0,0),(20,170,615,5))
    pygame.draw.rect(win,(0,0,0),(20,325,615,5))
    pygame.draw.rect(win,(0,0,0),(20,480,615,5))
    pygame.display.update()
    right_swipe.counter=0
    left_swipe.counter=0
    up_swipe.counter=0
    down_swipe.counter=0
    right_swipe.kul=0
    left_swipe.kul=0
    down_swipe.kul=0
    up_swipe.kul=0
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
    toprint()
    k=True
    while k:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                k = False
        #hint()
        clock.tick(10)

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left_swipe()
            toprint()
        elif keys[pygame.K_RIGHT]:
            right_swipe()
            toprint()
        elif keys[pygame.K_UP]:
            up_swipe()
            toprint()
        elif keys[pygame.K_DOWN]:
            down_swipe()
            toprint()
        empt=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]==0:
                    empt+=1
        if empt==0:
            adj=0
            for i in range(0,4,1):
                for j in range(0,3,1):
                    if global_arr[i][j]==global_arr[i][j+1]:
                        adj+=1
            for j in range(0,4,1):
                for i in range(0,s,1):
                    if global_arr[i][j]==global_arr[i+1][j]:
                        adj+=1
            if adj==0:
                print("GAME OVER")

        if max(map(max,global_arr))==2048:
            print("YOU WON")
            k=False
        #print(global_arr)

main()
