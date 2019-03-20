import pygame
import time
import random


pygame.init()


white=(250,250,250)
black=(0,0,0)
red=(250,0,0)
green=(0,250,0)
blue=(0,0,250)
yellow=(250,250,0)



game=pygame.display.set_mode((560,560))


pygame.display.set_caption("MAZY")


clock=pygame.time.Clock



pygame.mixer.music.load("world-m.ogg")

crash_sound=pygame.mixer.Sound("lose-m.wav")







def win():
    
    font=pygame.font.SysFont(None,70)
    text=font.render("YOU WON",True,black)
    game.blit(text,(100,200))

    pygame.mixer.music.stop()

    pygame.mixer.Sound.play(crash_sound)

    pygame.display.update()
    time.sleep(2)
    gameloop()

        




def menu():

    while True:
        game.fill(white)

        
















def gameloop():

    pygame.mixer.music.play(-1)

    b=[0,70,140,210,280,350,420,490]


    c=[]
    d=[]
    i=0



    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1







    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1









    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1










    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1











    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1











    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1









    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1








    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1







    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1







    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1









    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1









    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1






    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1








    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1








    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1








    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1







    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1








    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1









    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1






    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1








    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1








    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1










    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1










    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1










    instagram_x=random.choice(b)
    instagram_y=random.choice(b)

    #pygame.draw.rect(game,red,[instagram_x,instagram_y,65,65])

    c.insert(i,instagram_x)
    d.insert(i,instagram_y)
    i+=1








































    bug_x=0
    bug_y=0


    s=0

    p=0

    go=True


    while True:

        game.fill(white)


        for k in range(0,i,1):
            pygame.draw.rect(game,red,[c[k],d[k],65,65])

        

        pygame.draw.rect(game,yellow,[490,490,65,65])





        p=0
        for j in range(0,i,1):
            if bug_x==c[j] and bug_y==d[j]:
                p+=1

        
        


        print(p)
        if p==0:
            go=True



        if go==False:
            if s==1:
                bug_x-=70
                go=True
            
            if s==-1:
                bug_x+=70
                go=True

            if s==2:
                bug_y-=70
                go=True

            if s==-2:
                bug_y+=70
                go=True




        if bug_x==560:
            if go==True:
                bug_x=0
                go=False


        if bug_x==-70:
            if go==True:
                bug_x=490
                go=False



        if bug_y==560:
            if go==True:
                bug_y=0
                go=False


        if bug_y==-70:
            if go==True:
                bug_y=490
                go=False







        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    if go==True:
                        bug_x+=70
                        s=1
                        go=False

                if event.key==pygame.K_LEFT:
                    if go==True:
                        bug_x-=70
                        s=-1
                        go=False

                if event.key==pygame.K_DOWN:
                    if go==True:
                        bug_y+=70
                        s=2
                        go=False

                if event.key==pygame.K_UP:
                    if go==True:
                        bug_y-=70
                        s=-2
                        go=False


            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    bug_x+=0

                if event.key==pygame.K_LEFT:
                    bug_x-=0

                if event.key==pygame.K_DOWN:
                    bug_y+=0

                if event.key==pygame.K_UP:
                    bug_y-=0
            

        



        







        pygame.draw.line(game,green,(70,0),(70,560),5)

        pygame.draw.line(game,green,(140,0),(140,560),5)

        pygame.draw.line(game,green,(210,0),(210,560),5)

        pygame.draw.line(game,green,(280,0),(280,560),5)

        pygame.draw.line(game,green,(350,0),(350,560),5)

        pygame.draw.line(game,green,(420,0),(420,560),5)

        pygame.draw.line(game,green,(490,0),(490,560),5)






        pygame.draw.line(game,green,(0,70),(560,70),5)

        pygame.draw.line(game,green,(0,140),(560,140),5)

        pygame.draw.line(game,green,(0,210),(560,210),5)

        pygame.draw.line(game,green,(0,280),(560,280),5)

        pygame.draw.line(game,green,(0,350),(560,350),5)

        pygame.draw.line(game,green,(0,420),(560,420),5)

        pygame.draw.line(game,green,(0,490),(560,490),5)




        


        

        game.blit(pygame.image.load("Bug.png"),(bug_x,bug_y))

        


        if bug_x==490 and bug_y==490:
            bug_x=500
            bug_y=500
            win()









        pygame.display.update()








gameloop()

pygame.quit()
quit()

