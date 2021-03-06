import pygame
import random
import math

pygame.init()

pts = 0
moves = 0
pre_pts = 0
global_arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
redo_arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

win = pygame.display.set_mode((655,695))

clock = pygame.time.Clock()

pygame.display.set_caption("4X4 2048 by kulyash")

def equalise(a,b):
    for i in range(0,4):
        for j in range(0,4):
            a[i][j] = b[i][j]

def toprint():
    global global_arr
    global moves
    global pts

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
    pygame.draw.rect(win,(0,0,0),(0,655,655,40))

    a = pygame.font.SysFont("ARIAL",25)
    with open('High_score.txt','r') as file:
        data = file.read()
        move = str(moves)
        sco = str(pts)
        print(sco)
        text = a.render("SCORE: " + sco + "   HIGH SCORE: " + data + "   MOVES: " + move, 0, (255, 255, 255))
        win.blit(text, (35, 650))
        pygame.display.update()

def right_swipe():
    global pts
    global global_arr
    temp_arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    temp_arr=global_arr

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
                    pts+=temp_arr[i][j]
                    temp_arr[i][j-1]=0

        right_swipe.counter+=1

        equalise(global_arr,temp_arr)
        right_swipe()
    elif right_swipe.counter%2==1:
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

def left_swipe():
    global pts
    global global_arr
    temp_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    temp_arr=global_arr
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
                    pts+=temp_arr[i][j]
                    temp_arr[i][j+1]=0
        equalise(global_arr,temp_arr)
        left_swipe.counter+=1
        left_swipe()
    else:
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

def up_swipe():
    global pts
    global global_arr
    temp_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    temp_arr=global_arr
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
                    pts+=temp_arr[i][j]
                    temp_arr[i+1][j]=0

        equalise(global_arr,temp_arr)
        up_swipe.counter+=1
        up_swipe()
    else:
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

def down_swipe():

    global pts
    global global_arr
    temp_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    temp_arr=global_arr
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
                    pts+=temp_arr[i][j]
                    temp_arr[i-1][j]=0
        equalise(global_arr,temp_arr)
        down_swipe.counter+=1
        down_swipe()
    else:
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

def right_possible():
    global global_arr
    temp_arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    equalise(temp_arr,global_arr)
    for i in range(0,4,1):
        count=3;
        for j in range (3,-1,-1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[i][count]
                temp_arr[i][count]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1

    if temp_arr!=global_arr:
        return 1
    else:
        equals=0
        for i in range(0,4,1):
            for j in range(0,3,1):
                if temp_arr[i][j]==temp_arr[i][j+1] and temp_arr[i][j]!=0:
                    equals=1
                    return 1
        if equals==0:
            return 0

def left_possible():
    global global_arr
    temp_arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    equalise(temp_arr,global_arr)
    for i in range(0,4,1):
        count=3;
        for j in range (0,4,1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[i][3-count]
                temp_arr[i][3-count]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1
    if temp_arr!=global_arr:
        return 1
    else:
        equals=0
        for i in range(0,4,1):
            for j in range(0,3,1):
                if temp_arr[i][j]==temp_arr[i][j+1] and temp_arr[i][j]!=0:
                    equals=1
                    return 1
        if equals==0:
            return 0

def up_possible():
    global global_arr
    temp_arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    equalise(temp_arr,global_arr)
    for j in range(0,4,1):
        count=3;
        for i in range (0,4,1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[3-count][j]
                temp_arr[3-count][j]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1
    if temp_arr!=global_arr:
        return 1
    else:
        equals=0
        for j in range(0,4,1):
            for i in range(0,3,1):
                if temp_arr[i][j]==temp_arr[i+1][j] and temp_arr[i][j]!=0:
                    equals=1
                    return 1
        if equals==0:
            return 0

def down_possible():
    global global_arr
    temp_arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    equalise(temp_arr,global_arr)
    for j in range(0,4,1):
        count=3;
        for i in range (3,-1,-1):
            if temp_arr[i][j]!=0:
                temp_var=temp_arr[count][j]
                temp_arr[count][j]=temp_arr[i][j]
                temp_arr[i][j]=temp_var
                count=count-1
    if temp_arr!=global_arr:
        return 1
    else:
        equals=0
        for j in range(0,4,1):
            for i in range(0,3,1):
                if temp_arr[i][j]==temp_arr[i+1][j] and temp_arr[i][j]!=0:
                    equals=1
                    return 1
        if equals==0:
            return 0

def hint():

    global global_arr
    global pts
    temp_score=pts
    temp2_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    equalise(temp2_arr,global_arr)
    score = [0,0,0,0]
    if right_possible():
        right_swipe()
        a=max(map(max,global_arr))
        countmax1=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]==max(map(max,global_arr)) and ((i==0 and j==0) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==0)):
                    countmax1=10
                elif global_arr[i][j]==max(map(max,global_arr)) and (i==0 or j==0 or i==3 or j==3):
                    countmax1=5
        count1=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]!=0:
                    count1+=1
        count1=16-count1
        equalise(global_arr,temp2_arr)
        pts=temp_score
        score[0]=a/20+count1+countmax1
        for i in range(1,3,1):
            for j in range(1,3,1):
                if global_arr[i][j]==2 and global_arr[i-1][j]>=4 and global_arr[i][j-1]>=4 and global_arr[i][j+1]>=4 and global_arr[i+1][j]>=4:
                    score[0]-=a/21
                elif global_arr[i][j]==4 and global_arr[i-1][j]>=8 and global_arr[i][j-1]>=8 and global_arr[i][j+1]>=8 and global_arr[i+1][j]>=8:
                    score[0]-=a/22
        if a>=64:
            temp_var1=a
            for i in range(0,4,1):
                for j in range(0,3,1):
                    while a>=2:
                        if global_arr[i][j]==a and global_arr[i][j]==global_arr[i][j+1]:
                            score[0]+=2*math.log(a,2)
                        a/=2

            a=temp_var1
            for j in range(0,4,1):
                for i in range(0,3,1):
                    while a>=2:
                        if global_arr[i][j]==a and global_arr[i][j]==global_arr[i][j+1]:
                            score[0]+=a/20
                        a/=2

    if left_possible():
        left_swipe()
        b=max(map(max,global_arr))
        countmax2=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]==max(map(max,global_arr)) and ((i==0 and j==0) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==0)):
                    countmax2=10
                elif global_arr[i][j]==max(map(max,global_arr)) and (i==0 or j==0 or i==3 or j==3):
                    countmax2=5
        count2=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]!=0:
                    count2+=1
        count2=16-count2
        equalise(global_arr,temp2_arr)
        pts=temp_score
        score[1]=b/20+count2+countmax2
        if b>=64:
            temp_var1=b
            for i in range(0,4,1):
                for j in range(0,3,1):
                    while b>=2:
                        if global_arr[i][j]==b and global_arr[i][j]==global_arr[i][j+1]:
                            score[0]+=2*math.log(b,2)
                        b/=2

            b=temp_var1
            for j in range(0,4,1):
                for i in range(0,3,1):
                    while b>=16:
                        if global_arr[i][j]==b and global_arr[i][j]==global_arr[i][j+1]:
                            score[0]+=b/20
                        b/=2

        for i in range(1,3,1):
            for j in range(1,3,1):

                if global_arr[i][j]==2 and global_arr[i-1][j]>=4 and global_arr[i][j-1]>=4 and global_arr[i][j+1]>=4 and global_arr[i+1][j]>=4:
                    score[1]-=b/21
                elif global_arr[i][j]==4 and global_arr[i-1][j]>=8 and global_arr[i][j-1]>=8 and global_arr[i][j+1]>=8 and global_arr[i+1][j]>=8:
                    score[1]-=b/22
    if up_possible():
        up_swipe()
        c=max(map(max,global_arr))
        countmax3=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]==max(map(max,global_arr)) and ((i==0 and j==0) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==0)):
                    countmax3=10
                elif global_arr[i][j]==max(map(max,global_arr)) and (i==0 or j==0 or i==3 or j==3):
                    countmax3=5
        count3=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]!=0:
                    count3+=1
        count3=16-count3
        equalise(global_arr,temp2_arr)
        pts=temp_score
        score[2]=c/20+count3+countmax3
        if c>=64:
            temp_var1=c
            for i in range(0,4,1):
                for j in range(0,3,1):
                    while c>=2:
                        if global_arr[i][j]==c and global_arr[i][j]==global_arr[i][j+1]:
                            score[0]+=2*math.log(c,2)
                        c/=2

            c=temp_var1
            for j in range(0,4,1):
                for i in range(0,3,1):
                    while c>=2:
                        if global_arr[i][j]==c and global_arr[i][j]==global_arr[i][j+1]:
                            score[0]+=c/20
                        c/=2
        for i in range(1,3,1):
            for j in range(1,3,1):

                if global_arr[i][j]==2 and global_arr[i-1][j]>=4 and  global_arr[i][j-1]>=4 and global_arr[i][j+1]>=4 and global_arr[i+1][j]>=4:
                    score[2]-=c/21
                elif global_arr[i][j]==4 and global_arr[i-1][j]>=8 and  global_arr[i][j-1]>=8 and global_arr[i][j+1]>=8 and global_arr[i+1][j]>=8:
                    score[2]-=c/22

    if down_possible():
        down_swipe()
        d=max(map(max,global_arr))
        countmax4=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]==max(map(max,global_arr)) and ((i==0 and j==0) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==0)):
                    countmax4=10
                elif global_arr[i][j]==max(map(max,global_arr)) and (i==0 or j==0 or i==3 or j==3):
                    countmax4=5
        count4=0
        for i in range(0,4,1):
            for j in range(0,4,1):
                if global_arr[i][j]!=0:
                    count4+=1
        count4=16-count4
        equalise(global_arr,temp2_arr)
        pts=temp_score
        score[3]=d/20+count4+countmax4
        if d>=64:
            temp_var1=d
            for i in range(0,4,1):
                for j in range(0,3,1):
                    while d>=2:
                        if global_arr[i][j]==d and global_arr[i][j]==global_arr[i][j+1]:
                            score[0]+=2*math.log(d,2)
                        d/=2

            d=temp_var1
            for j in range(0,4,1):
                for i in range(0,3,1):
                    while d>=2:
                        if global_arr[i][j]==d and global_arr[i][j]==global_arr[i][j+1]:
                            score[0]+=d/20
                        d/=2
        for i in range(1,3,1):
            for j in range(1,3,1):
                # if global_arr[i][j]==d and (global_arr[i-1][j-1]==d/2 or global_arr[i-1][j]==d/2 or global_arr[i][j-1]==d/2 or global_arr[i][j+1]==d/2 or global_arr[i+1][j+1]==d/2 or global_arr[i+1][j]==d/2 or global_arr[i-1][j+1]==d/2 or global_arr[i+1][j-1]==d/2 ):
                #     score[3]+=10
                if global_arr[i][j]==2 and global_arr[i-1][j]>=4 and global_arr[i][j-1]>=4 and global_arr[i][j+1]>=4 and global_arr[i+1][j]>=4:
                    score[3]-=d/21
                if global_arr[i][j]==4 and global_arr[i-1][j]>=8 and  global_arr[i][j-1]>=8 and global_arr[i][j+1]>=8 and global_arr[i+1][j]>=8:
                    score[3]-=d/22


    if max(score)==score[0]:
        print("D")
        right_swipe()
        toprint()
    elif max(score)==score[1]:
        print("A")
        left_swipe()
        toprint()
    elif max(score)==score[2]:
        print("W")
        up_swipe()
        toprint()
    elif max(score)==score[3]:
        print("S")
        down_swipe()
        toprint()

def main():
    global moves
    global global_arr
    global pts
    global prev_pts
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    k=False
                elif event.key == pygame.K_LEFT and left_possible():
                    moves+=1
                    equalise(redo_arr,global_arr)
                    prev_pts=pts
                    left_swipe()
                    toprint()
                    print(pts,end = "")


                elif event.key == pygame.K_RIGHT and right_possible():
                    moves+=1
                    equalise(redo_arr,global_arr)
                    prev_pts=pts
                    right_swipe()
                    toprint()
                    print(pts,end = "")

                elif event.key == pygame.K_UP and up_possible():
                    moves+=1
                    equalise(redo_arr,global_arr)
                    prev_pts=pts
                    up_swipe()
                    toprint()
                    print(pts,end = "")

                elif event.key == pygame.K_DOWN and down_possible():
                    moves+=1
                    equalise(redo_arr,global_arr)
                    prev_pts=pts
                    down_swipe()
                    toprint()
                    print(pts,end = "")

                elif event.key == pygame.K_h:
                    moves+=1
                    hint()

                elif event.key == pygame.K_b:
                    equalise(global_arr,redo_arr)
                    pts=prev_pts
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
                for i in range(0,3,1):
                    if global_arr[i][j]==global_arr[i+1][j]:
                        adj+=1

            if adj==0:
                pygame.time.delay(3000)
                p12=pygame.image.load("game over.png")
                win.blit(p12,(20,20))
                pygame.display.update()
                with open('High_score.txt','r+') as file:
                    data_str=file.read()
                    data=int(data_str)
                    if pts>data:
                        file.seek(0)
                        file.write(str(pts))

                for gameover in pygame.event.get():
                    if event.type == pygame.QUIT:
                        k = False
                    if gameover.type==pygame.KEYDOWN:
                        if gameover.key==pygame.K_r:
                            global_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                            pts=0
                            moves=0
                            main()
                        elif gameover.key==pygame.K_b:
                            equalise(global_arr,redo_arr)
                            main()
                            toprint()
                        elif gameover.key==pygame.K_ESCAPE:
                            k=False

        if max(map(max,global_arr))==2048:
            p13=pygame.image.load("winner.png")
            win.blit(p13,(20,20))
            pygame.display.update()
            for winner in pygame.event.get():
                if event.type == pygame.QUIT:
                    k = False
                if winner.type==pygame.KEYDOWN:
                    if winner.key==pygame.K_r:
                        global_arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                        pts=0
                        moves=0
                        main()
                    elif winner.key==pygame.K_ESCAPE:
                        k=False

p14=pygame.image.load("welcome.jpg")
win.blit(p14,(20,20))
pygame.display.update()
pygame.time.delay(5000)
main()
