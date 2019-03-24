import pygame
import random

global_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

win=pygame.display.set_mode((655,655))

clock = pygame.time.Clock()

pygame.display.set_caption("4X4 2048 by kulyash")

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
    #kul=0
    if right_swipe.counter%2==0:
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
                    right_swipe.kul+=1
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
        #print(max(map(max,global_arr)))
def main():
    #pygame.event.pump()
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

        if max(map(max,global_arr))==2048:
            print("YOU WON")
            k=False

main()
