import pygame
class Goal:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.isactiv = False

    def draw(self, win):
        color = (255, 0, 0) if self.isactiv else (0, 255, 0)
        pygame.draw.line(win, color, (self.x1, self.y1), (self.x2, self.y2), 2)
def getGoals():
    goals = []

    goal1 = Goal(0,200,120,200)
    goal2 = Goal(0,100,120,150)
    goal2_5 = Goal(0,0,150,130)
    goal3 = Goal(120,0,170,120)
    goal3_5 = Goal(200,0,200,120)
    goal4 = Goal(270,0,270,110)
    goal4_5 = Goal(350,0,350,110)
    goal5 = Goal(450,0,450,110)
    goal5_5 = Goal(525,0,525,110)
    goal6 = Goal(600,0,550,130)
    goal6_5 = Goal(550,130,700,60)
    goal7 = Goal(550,130,700,130)
    goal7_5 = Goal(550,130,650,200)
    goal8 = Goal(550,130,570,240)
    goal9 = Goal(410,130,430,260)
    goal9_5 = Goal(430,260,300,350)
    goal10 = Goal(430,260,260,260)
    goal10_5 = Goal(430,260,280,180)
    goal11 = Goal(430,260,400,400)
    goal12 = Goal(550,260,570,400)
    goal13 = Goal(750,400,650,200)
    goal14 = Goal(750,400,800,160)
    goal15 = Goal(750,400,950,240)
    goal16 = Goal(750,400,980,440)
    goal17 = Goal(750,400,900,600)
    goal18 = Goal(750,460,750,600)
    goal19 = Goal(670,460,670,600)
    goal19_5 = Goal(590,460,590,600)
    goal20 = Goal(510,460,510,600)
    goal20_5 = Goal(430,460,430,600)
    goal21 = Goal(350,460,350,600)
    goal21_5 = Goal(280,460,278,600)
    goal22 = Goal(210,460,190,600)
    goal22_5 = Goal(80,600,175,440)
    goal23 = Goal(150,420,0,570)
    goal23_5 = Goal(0,450,130,400)
    goal24 = Goal(0,380,130,380)

    goals.extend([goal1, goal2, goal2_5, goal3, goal3_5, goal4, goal4_5, goal5, goal5_5, goal6, goal6_5,
                  goal7, goal7_5, goal8, goal9, goal10, goal10_5, goal9_5, goal11, goal12, goal13, goal14,
                  goal15, goal16, goal17, goal18, goal19, goal19_5, goal20, goal20_5, goal21, goal21_5,
                  goal22, goal22_5, goal23, goal23_5, goal24])

    goals[-1].isactiv = True

    return goals
