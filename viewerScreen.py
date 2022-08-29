import sys, pygame,random

class GameRun():

    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 1000,700
        self.speed = 20
        self.score=0
        self.white = 255,255,255
        self.green=0,200,0
        self.completeMove=0,0
        pygame.display.set_caption("Ant Game")
        self.safezonemeasures=self.safeW,self.safeH=750,700
        self.screen = pygame.display.set_mode(self.size)
        self.resetGame()

    def resetGame(self):
        self.score = 0
        self.completeMove = 0, 0
        # initalise ant Sprite
        self.ant = pygame.image.load("assets/ant.png")
        self.ant = pygame.transform.scale(self.ant, (40, 60))
        self.antRect = self.ant.get_rect()
        # Initalise Food Sprite
        self.food = pygame.image.load("assets/potato.png")
        self.food = pygame.transform.scale(self.food, (40, 40))
        self.foodRect = self.food.get_rect()

        self.placeFood()
        self.updateUI()
        self.frameIter=0


    def boundaryCheck(self):
        '''Boundary check to keep ant within screen bounds'''
        if self.antRect.left < 0:
            self.antRect = self.antRect.move(self.speed, 0)
        if self.antRect.right > self.width:
            self.antRect = self.antRect.move(-self.speed, 0)
        if self.antRect.top < 0:
            self.antRect = self.antRect.move(0, self.speed)
        if self.antRect.bottom > self.height:
            self.antRect = self.antRect.move(0, -self.speed)

    def updateUI(self):
        '''Updates the Ui and draws to screen'''
        self.screen.fill(self.white)
        pygame.draw.rect(self.screen, self.green, pygame.Rect(self.safeW, 0, 250, self.safeH), 2)
        self.checkFoodCollision()
        self.screen.blit(self.ant, self.antRect)
        self.screen.blit(self.food,self.foodRect)
        pygame.display.flip()

    def placeFood(self):
        xPlace = random.randint(0,self.width-40)
        yPlace=random.randint(0,self.height-40)
        self.foodRect.x,self.foodRect.y=xPlace,yPlace

    def checkFoodCollision(self):
        collision=self.antRect.colliderect(self.foodRect)
        if collision:
            self.score+=1
            self.placeFood()

    def _move(self,direction):
        if direction=="left":
            self.completeMove = (-self.speed, 0)
        if direction=="right":
            self.completeMove = self.speed, 0
        if direction=="up":
            self.completeMove = 0, -self.speed
        if direction=="down":
            self.completeMove = 0, self.speed

    def initalizeStep(self):
        self.frameIter+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"{self.score} was the final score")
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self._move("left")
                if event.key==pygame.K_RIGHT:
                    self._move("right")
                if event.key==pygame.K_DOWN:
                    self._move("down")
                if event.key==pygame.K_UP:
                    self._move("up")
                self.antRect = self.antRect.move(self.completeMove) # move the ant
                self.boundaryCheck()
                self.updateUI()