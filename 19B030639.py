#pylint: disable=no-member
import pika
import json
import uuid
from threading import Thread
import pygame
import sys
import pymongo
import os
import subprocess
import random
from pathlib import Path
import math
from pygame import mixer
from os import path 
aqtus = (255,255,255)
qaratus = (0,0,0)
grey = (192,192,192)
qyzyl = (200,0,0)
light_qyzyl = (255,0,0)
medqyzyl = (255, 153, 51)
zhasyl = (34,177,76)
light_zhasyl = (0,255,0)
med_zhasyl = (47, 116,127)
sary = (200,200,0)
light_sary = (255,255,0)

pygame.init()

screen = pygame.display.set_mode((800,600))
screenwidth = 800
screenheight = 600
pygame.display.set_caption('Tanks')
smalllfont = pygame.font.SysFont("comicsansms", 25)
meddfont = pygame.font.SysFont("comicsansms", 50)

largefont = pygame.font.SysFont("comicsansms", 85)

def message_t_screen(msg,color,y_displace=0,size="small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = (int(screenwidth/2),int(screenheight/2)+y_displace)
    screen.blit(textSurf, textRect)
def text_objects(text,color,size="small"):
    if size == 'small':
        textSurface = smalllfont.render(text, 1, color)
    if size == "medium":
        textSurface = meddfont.render(text, 1, color)
    if size == "large":
        textSurface = largefont.render(text, 1, color)
    return textSurface, textSurface.get_rect()    
def main_menu():
    menurun = True
    
    while menurun:
        
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            sMode()
                        elif event.key == pygame.K_m:
                            mMode()
                        elif event.key == pygame.K_a: 
                            AIMode()    
        screen.fill(aqtus)
        message_t_screen("Welcome to Tanks!",medqyzyl,-100,size="large")
        message_t_screen("Press S to play single",qaratus,50) 
        message_t_screen("Press M to play multiplayer_mode",qaratus,90)
        message_t_screen("Press A to play multiAI",qaratus,130)
        pygame.display.flip()
        clock.tick(30)
clock = pygame.time.Clock()

def sMode():
    speed = 4
    bulletspeed = 8

    aqtus = (255,255,255)
    qaratus = (0,0,0)
    grey = (192,192,192)
    qyzyl = (200,0,0)
    light_qyzyl = (255,0,0)
    medqyzyl = (255, 153, 51)
    zhasyl = (34,177,76)
    light_zhasyl = (0,255,0)
    med_zhasyl = (47, 116,127)
    sary = (200,200,0)
    light_sary = (255,255,0)

    pygame.init()
    screenwidth = 800
    screenheight = 600
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Tanks')
    smalllfont = pygame.font.SysFont("comicsansms", 25)
    meddfont = pygame.font.SysFont("comicsansms", 50)
    largefont = pygame.font.SysFont("comicsansms", 85)
    pygame.mixer.music.load(path.join('back.mp3'))
    over = mixer.Sound("gameover.wav")
    shoot = mixer.Sound("shoot.wav")
    hate = mixer.Sound("hit.wav")
    playsound = mixer.Sound("play.wav")

    def random_color():
        rgb=[255,0,0]
        random.shuffle(rgb)
        return tuple(rgb)

    def button(text,x,y,width,height,inactive_color,active_color,action=None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < cur[0] < x + width and y < cur[1] < y + height:
            pygame.draw.rect(screen,active_color,(x,y,width,height))
            if click[0] == 1 and action != None:
                if action == "play":               
                    playsound.play()
                    gameloop()
                if action == "controls":
                    game_controls()
                if action == "quit":
                    pygame.quit()
                    quit()
                
        else:
            pygame.draw.rect(screen,inactive_color,(x,y,width,height))
        text_to_button(text,qaratus,x,y,width,height)

    def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight, size="small"):
        textSurf, textRect = text_objects(msg,color,size)
        textRect.center = ((buttonx+int(buttonwidth/2)),buttony+int(buttonheight/2))
        screen.blit(textSurf,textRect)

    def text_objects(text,color,size="small"):
        if size == 'small':
            textSurface = smalllfont.render(text, 1, color)
        if size == "medium":
            textSurface = meddfont.render(text, 1, color)
        if size == "large":
            textSurface = largefont.render(text, 1, color)
        return textSurface, textSurface.get_rect()

    def message_t_screen(msg,color,y_displace=0,size="small"):
        textSurf,textRect = text_objects(msg,color,size)
        textRect.center = (int(screenwidth/2),int(screenheight/2)+y_displace)
        screen.blit(textSurf, textRect)

    def game_controls():
        cont = True
        while cont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.fill(aqtus)
            message_t_screen("Controls",med_zhasyl,-100,size="large")
            message_t_screen("Move Player1: Up,Down,Right and Left arrows",qaratus,-30)
            message_t_screen("Fire: Spacebar",qaratus,10)
            message_t_screen("Move Player2: W,S,D ana A keyboard keys",qaratus,50)
            message_t_screen("Fire: Enter",qaratus,90)
            message_t_screen("Pause: P",qaratus,130)
            
            button("play",150,500,100,50,zhasyl,light_zhasyl,action="play")
            button("quit",550,500,100,50,qyzyl,light_qyzyl,action="quit")

            pygame.display.flip()
            clock.tick(15)

    def game_intro():
        intro = True
        
        while intro:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        intro = False
            screen.fill(aqtus)
            message_t_screen("Welcome to Tanks!",medqyzyl,-100,size="large")
            button("play",150,370,100,50,zhasyl,light_zhasyl,action="play")
            button("controls",350,370,100,50,sary,light_sary,action="controls")
            button("quit",550,370,100,50,qyzyl,light_qyzyl,action="quit")
            pygame.display.flip()
            clock.tick(FPS)

    def intersect(colbox1,colbox2):
        return(colbox2[0] <= colbox1[0]+colbox1[2] and colbox2[1] <= colbox1[1]+colbox1[3]) and (colbox2[0]+colbox2[2] >= colbox1[0] and colbox2[1]+colbox2[3] >= colbox1[1])
    class Direction:
        UP = 1
        DOWN = 2
        LEFT = 3
        RIGHT = 4
    class Bullet:
        def __init__(self, x, y, sx, sy, tank):
            self.x = x
            self.y = y
            self.radius = 9
            self.speedx = sx
            self.speedy = sy
            self.tank = tank
            self.state = False
        def draw(self):
            if self.state == False:
                pygame.draw.circle(screen, self.tank.color, (int(self.x), int(self.y)), int(self.radius))
        
        def move(self):
            self.x += self.speedx
            self.y += self.speedy
            if  0 >= self.x or self.x >= 800:
                self.state=True
            if 0 >= self.y or self.y >= 600:
                self.state=True
            self.draw()

    class Tank:

        def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN):
            self.x = x
            self.y = y
            self.life = 3
            self.color = color
            self.speed = speed
            self.width = 31
            self.direction = random.randint(1, 4)
            self.bounds = (x,y,self.width,self.width) 
            self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                        d_up: Direction.UP, d_down: Direction.DOWN}
            self.state = True
        def draw(self):
            if self.state == True:
                center = (int(self.x + self.width // 2), int(self.y + self.width // 2))
                pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width),3)
                # pygame.draw.circle(screen, self.color, center, int(self.width/2),2)
                # pygame.draw.circle(screen, self.color, center, int(self.width // 1.1),5)

                if self.direction == Direction.RIGHT:
                    pygame.draw.line(screen, self.color, center, (int(self.x + self.width) + int(self.width/3), int(self.y) + int(self.width / 2)), 2)
                if self.direction == Direction.LEFT:
                    pygame.draw.line(screen, self.color, center, (int(self.x) - int(self.width/3), int(self.y) + int(self.width / 2)), 2)
                if self.direction == Direction.UP:
                    pygame.draw.line(screen, self.color, center, (int(self.x) + int(self.width/2), int(self.y) - int(self.width / 3)), 2)
                if self.direction == Direction.DOWN:
                    pygame.draw.line(screen, self.color, center, (int(self.x) + int(self.width/2), int(self.y + self.width) + int(self.width / 3)), 2)
        
        def change_direction(self, direction):
            self.direction = direction
        def random_pos(self):
            self.x = random.randint(200,600)
            self.y = random.randint(200,400)
        def move(self):
            if self.direction == Direction.LEFT:
                self.x -= self.speed
            if self.direction == Direction.RIGHT:
                self.x += self.speed
            if self.direction == Direction.UP:
                self.y -= self.speed
            if self.direction == Direction.DOWN:
                self.y += self.speed

            if self.y < -40:
                self.y = 600
            if self.y > 600:
                self.y = 0
            if self.x < -40:
                self.x = 800
            if self.x > 800:
                self.x = 0
            
            self.draw()
    class Walls:

        def __init__(self,x=random.randint(100, 700),y=random.randint(100, 500)):
            
            self.x = x

            self.y = y

            self.image = pygame.image.load("wall.png")
        def draw(self):     
            screen.blit(self.image, (self.x, self.y))
        def random_pos(self):
            self.x = random.randint(100,600)
            self.y = random.randint(100,400)     
    class Food:

        def __init__(self):

            self.x = random.randint(70, 570)

            self.y = random.randint(70, 306)

        def draw(self):
            
            pygame.draw.circle(screen, random_color(), (self.x, self.y), 6,5)
    
        def eat1(self):
                
                if int(self.x) in range(int(tank1.x), int(tank1.x + 60)) and int(self.y) in range(int(tank1.y), int(tank1.y + 60)):                   
                    self.x = 1000
                    self.y = 1000
                    return True
        def eat2(self):
                if int(self.x) in range(int(tank2.x), int(tank2.x + 60)) and int(self.y) in range(int(tank2.y), int(tank2.y + 60)):
                    self.x = 1000
                    self.y = 1000
                    return True
    food = Food()                

    def Life1(x):
        font = pygame.font.SysFont("comicsansms", 25)
        pnt = font.render("Daulet: " + str(x), True, (35,187,17))
        screen.blit(pnt, (20, 20))

    def Life2(x):
        font = pygame.font.SysFont("comicsansms", 25)
        pnt = font.render("Player2: " + str(x), True, (255,170,35))
        screen.blit(pnt, (650, 20))

                    
    FPS = 30
    clock = pygame.time.Clock()
    walls=[]
    tank1 = Tank(50, 550, 3, (35,187,17))
    tank2 = Tank(750, 550, 3, (255,170,35), pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)
    tanks=[]
    tanks.append(tank1)
    tanks.append(tank2)
    # walls.append(wall1)
    # walls.append(wall2)
    bullets = []
    m=4
    n=5
    plus=0



    def gameloop():
        m=4
        n=5
        plus=0
        for i in range(m):
            x=random.randint(60, 700)
            y=random.randint(60, 500)
            yw=random.randrange(2, 7)
            for j in range(yw):
                ax=random.randint(1, 2)
                if ax==1:
                    x+=31
                else:
                    y+=31
                wall=Walls(x,y)
                a=False
                for wall2 in walls:
                    if wall.x in range(wall2.x, wall2.x + 31) and wall.y in range(wall2.y, wall2.y + 31):
                        a=True
                if a==False:
                    walls.append(wall)
                    plus=31
                else:
                    break
        bulletspeed1=8
        bulletspeed2=8
        start_time = None
        tank1.state=True
        tank2.state=True
        gameExit = False
        gameOver = False
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)
        while not gameExit:    
            if gameOver == True:
                screen.fill(aqtus)
                if tank1.life>0:
                    tank1.speed = 0
                    tank1.draw()
                elif tank2.life>0:
                    tank2.speed = 0
                    tank2.draw()
                if tank1.life <= 0:
                    tank1.state=False
                elif tank2.life <= 0:
                    tank2.state=False
                mixer.music.stop() 
                over.play()             
                message_t_screen("Game Over",qyzyl,-50,size='small')
                message_t_screen("Press C to play again",qaratus,50) 
                message_t_screen("Press M to open the singleMod main menu",qaratus,90)
                message_t_screen("Press Q to go back to the Tanks main menu",qaratus,130)
                pygame.display.update()
                while gameOver == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameExit = True
                            gameOver = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_c:
                                tank1.life = 3
                                tank2.life = 3
                                tank1.speed = tank2.speed = 4
                                tank1.x =50
                                tank1.y =550
                                tank2.x =750
                                tank2.y =550 
                                gameloop()
                            elif event.key == pygame.K_q:
                                gameExit = True
                                gameOver = False
                                main_menu()  
                            elif event.key == pygame.K_m: 
                                game_intro()     
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                    if event.key in tank1.KEY.keys():
                        tank1.change_direction(tank1.KEY[event.key])
                    if event.key in tank2.KEY.keys():
                        tank2.change_direction(tank2.KEY[event.key])
                    if event.key == pygame.K_RETURN:
                        shoot.play()
                        if tank1.direction == Direction.LEFT:
                            bullet = Bullet(tank1.x - 16, tank1.y + 16, -bulletspeed1, 0,tank1)
                        if tank1.direction == Direction.RIGHT:
                            bullet = Bullet(tank1.x + 60, tank1.y + 16, bulletspeed1, 0,tank1)
                        if tank1.direction == Direction.UP:
                            bullet = Bullet(tank1.x + 16, tank1.y - 16, 0, -bulletspeed1,tank1)
                        if tank1.direction == Direction.DOWN:
                            bullet = Bullet(tank1.x + 16, tank1.y + 60, 0, bulletspeed1,tank1)
                        bullets.append(bullet)    
                    if event.key == pygame.K_SPACE:
                        shoot.play()
                        if tank2.direction == Direction.LEFT:
                            bullet = Bullet(tank2.x - 16, tank2.y + 16, -bulletspeed2, 0,tank2)
                        if tank2.direction == Direction.RIGHT:
                            bullet = Bullet(tank2.x + 60, tank2.y + 16, bulletspeed2, 0,tank2)
                        if tank2.direction == Direction.UP:
                            bullet = Bullet(tank2.x + 16, tank2.y - 16, 0, -bulletspeed2,tank2)
                        if tank2.direction == Direction.DOWN:
                            bullet = Bullet(tank2.x + 16, tank2.y + 60, 0, bulletspeed2,tank2)
                        bullets.append(bullet)
            for bu in bullets:
                if bu.x < 0 or bu.x > 800 or bu.y < 0 or bu.y > 600:
                    bullets.pop(0)
                elif bu.x in range(tank2.x, tank2.x + 60) and bu.y in range(tank2.y, tank2.y + 60):
                    if tank2.life>1:
                        hate.play()
                    bullets.pop(0)
                    tank2.random_pos()
                    tank2.life -= 1
                elif bu.x in range(tank1.x, tank1.x + 60) and bu.y in range(tank1.y, tank1.y + 60):
                    if tank1.life>1:
                        hate.play()
                    bullets.pop(0)
                    tank1.random_pos()
                    tank1.life -= 1   
                else:
                    for wall in walls:
                        if bu.x in range(wall.x, wall.x + 32) and bu.y in range(wall.y, wall.y + 32):
                            walls.remove(wall)
                            hate.play()
            for wall in walls:           
                if wall.x in range(tank2.x-30, tank2.x + 30) and wall.y in range(tank2.y-30, tank2.y + 30):
                        if tank2.life>1:
                            hate.play()
                        walls.remove(wall)
                        tank2.random_pos()
                        tank2.life -= 1
                elif wall.x in range(tank1.x-30, tank1.x + 30) and wall.y in range(tank1.y-30, tank1.y + 30):
                        if tank2.life>1:
                            hate.play()
                        walls.remove(wall)
                        tank1.random_pos()
                        tank1.life -= 1  
            # if wall2.x in range(tank1.x-30, tank1.x + 30) and wall2.y in range(tank1.y-30, tank1.y + 30):
            #         if tank2.life>1:
            #             hate.play()
            #         wall2.random_pos()
            #         tank1.random_pos()
            #         tank1.life -= 1 
            # if wall2.x in range(tank2.x-30, tank2.x + 30) and wall2.y in range(tank2.y-30, tank2.y + 30):
            #         if tank2.life>1:
            #             hate.play()
            #         wall2.random_pos()
            #         tank2.random_pos()
            #         tank2.life -= 1 
            screen.fill((255, 255, 255))
            Life1(tank1.life)
            Life2(tank2.life)
            if tank1.life <= 0 or tank2.life <= 0:
                gameOver = True 
            for bullet in bullets:
                bullet.move()
            for tank in tanks:
                tank.draw()
            time_since_enter = 0
            foodinpole = True
            if foodinpole and food.eat1():
                start_time = pygame.time.get_ticks()          
                food.x = 1254
                food.y = 1200
                foodinpole=False
                tank1.speed*=2
                bulletspeed1*=2
            if foodinpole and food.eat2():
                start_time = pygame.time.get_ticks()          
                food.x = 1254
                food.y = 1200
                foodinpole=False
                tank2.speed*=2
                bulletspeed2*=2
            if start_time:
                time_since_enter = pygame.time.get_ticks() - start_time           
            if time_since_enter>5000:
                    tank1.speed=speed
                    bulletspeed1=8
                    tank2.speed=speed
                    bulletspeed2=8
            if time_since_enter>random.randrange(4000,9000,1000):
                    food.x = 100
                    food.y = 200
            tank1.move()
            tank2.move() 
            food.draw() 
            for wall in walls:
                wall.draw()
            pygame.display.flip() 
            
        pygame.quit()
        quit()
        
    game_intro()

def mMode():
    over = mixer.Sound("gameover.wav")
    hit = mixer.Sound("hit.wav")
    shoot = mixer.Sound("shoot.wav")
    pygame.mixer.music.load(path.join('back.mp3'))
    roomID = 22
    pygame.init()
    qaratus = (0,0,0)
    aqtus = (255, 255, 255)
    screen = pygame.display.set_mode((1200, 600))
    screenwidth = 1050
    screenheight = 600
    IP = '34.254.177.17'
    PORT = 5672
    VIRTUAL_HOST = 'dar-tanks'
    USER = 'dar-tanks'
    PASSWORD = '5orPLExUYnyVYZg48caMpX'
    tank_id = ''
    def sortScore(score):
        return score['score']

    class TankRpcClient():
        
        def __init__(self):
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host = IP,
                    port = PORT,
                    virtual_host = VIRTUAL_HOST,
                    credentials=pika.PlainCredentials(
                        username = USER,
                        password = PASSWORD
                    )
                )
            )
            self.channel = self.connection.channel()
            queue = self.channel.queue_declare(queue='',auto_delete=True,exclusive=True)
            self.callback_queue = queue.method.queue
            self.channel.queue_bind(
                exchange='X:routing.topic',
                queue = self.callback_queue)

            self.channel.basic_consume(
                queue=self.callback_queue,
                on_message_callback=self.on_response,
                auto_ack=True
            )

            self.response = None
            self.corr_id = None
            self.token = None
            self.tank_id = None
            self.room_id = None

        def on_response(self, ch, method, props, body):
            if self.corr_id == props.correlation_id:
                self.response = json.loads(body)
                print(self.response)
    

        def call(self, key, message={}):
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(
                exchange='X:routing.topic',
                routing_key=key,
                properties=pika.BasicProperties(
                    reply_to=self.callback_queue,
                    correlation_id=self.corr_id,
                ),
                body=json.dumps(message)
                )
            while self.response is None:
                self.connection.process_data_events()
        
        def check_server_status(self):
            self.call('tank.request.healthcheck')
            return self.response['status'] == '200'
        
        def obtain_token(self, room_id):
            
            message = {
                'roomId': room_id
            }
            self.call('tank.request.register', message)
            if 'token' in self.response:
                self.token = self.response['token']
                self.tank_id = self.response['tankId']
                if self.tank_id == myclient.tank_id:
                    return 1
                else : return 0
                self.room_id = self.response['roomId']
                return True
            return False


        def turn_tank(self, token, direction):
            message = {
                'token': token,
                'direction': direction
            }
            self.call('tank.request.turn', message)

        def fire_bullet(self, token):
            message = {
                'token': token
            }
            self.call('tank.request.fire', message)


    def handle_register_response(obj):

        state = json.loads(obj)

        print(str(obj))

        global token

        token = state["token"]

        global tank

        tank = state["tankId"]


    class TankConsumerClient(Thread):
        def __init__(self, room_id):
            super().__init__()
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host = IP,
                    port = PORT,
                    virtual_host = VIRTUAL_HOST,
                    credentials=pika.PlainCredentials(
                        username = USER,
                        password = PASSWORD
                    )
                )
            )
            self.channel = self.connection.channel()
            queue = self.channel.queue_declare(queue='',auto_delete=True,exclusive=True)

            event_listener = queue.method.queue
            self.channel.queue_bind(exchange='X:routing.topic', queue=event_listener, routing_key='event.state.'+room_id)

            self.channel.basic_consume(
                queue=event_listener,
                on_message_callback=self.on_response,
                auto_ack=True
            )
            self.response = None
        def on_response(self, ch, method, props, body):
            self.response = json.loads(body)
        def run(self):
            self.channel.start_consuming()
        def close(self):
            self.connection.close()
        
        

    UP = 'UP'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'

    MOVE_KEYS = {
        pygame.K_UP: UP,
        pygame.K_DOWN: DOWN,
        pygame.K_RIGHT: RIGHT,
        pygame.K_LEFT: LEFT
    }
    #playerim = pygame.image.load('t1_up.png')

    def dtank(x, y, width, height, direction, health, score, color):
            tx = (x + int(width / 2), y + int(width / 2))
            pygame.draw.rect(screen, color,(x, y, width, height), 2)
            pygame.draw.circle(screen, color, tx, width // 2)                   
    def dbullet(x, y, width, height, direction, color ):
            pygame.draw.rect(screen, color, (x, y, width, height))

    # def hit_t(source, destination):
    #     hit_t.destination = destination
    #     if destination == client.tank_id:
    #         tank['health'] -= 1
    # '''all_sprites = pygame.sprite.Group()
    # player = Player(100, 300, 31)
    # all_sprites.add(player)'''Arial
    def best_tank(tankId,score):
        font = pygame.font.SysFont('comicsansms', 35)
        back=pygame.image.load('tt.jpg')
        text_score = font.render('SCORE: {}'.format(score), True, (255, 255, 255))
        text = font.render('YOU ARE WINNER', True, (255, 255, 255))
        text2 = font.render('Press R to restart the game', True, (255, 255, 255))
        ww=True
        while ww:
            mixer.music.stop() 
            over.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        font = pygame.font.SysFont('comicsansms', 35)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        mMode()
            screen.fill((0,0,0)) 
            screen.blit(back,(0,0))
            screen.blit(text, (150, 100))
            screen.blit(text_score, (350, 470))
            screen.blit(text2,(150,200))
            pygame.display.flip()
    def gg_tank(tankId,score):
        font = pygame.font.SysFont('comicsansms', 35)
        back=pygame.image.load('tt.jpg')
        text_score = font.render('SCORE: {}'.format(score), True, (255, 255, 255))
        text = font.render('YOU ARE LOSER', True, (255, 255, 255))
        text2 = font.render('Press R to restart the game', True, (255, 255, 255))
        ll=True
        while ll:
            mixer.music.stop() 
            over.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        font = pygame.font.SysFont('comicsansms', 35)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        mMode()
            screen.fill((0,0,0)) 
            screen.blit(back,(0,0))
            screen.blit(text, (150, 100))
            screen.blit(text_score, (350, 470))
            screen.blit(text2,(150,200))
            pygame.display.flip()
        
    def kick_tank(tankId,score):
        font = pygame.font.SysFont('comicsansms', 35)
        back=pygame.image.load('tt.jpg')
        text_score = font.render('SCORE: {}'.format(score), True, (255, 255, 255))
        text = font.render('YOU ARE KICKED', True, (255, 255, 255))
        text2 = font.render('Press R to restart the game', True, (255, 255, 255))
        kk=True
        while kk:
            mixer.music.stop() 
            over.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        font = pygame.font.SysFont('comicsansms', 35)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        mMode()
            screen.fill((0,0,0))
            screen.blit(back,(0,0))
            screen.blit(text, (150, 100))
            screen.blit(text_score, (350, 470))
            screen.blit(text2,(150,200))
            pygame.display.flip()
        

    def game_over():
        font = pygame.font.SysFont('comicsansms', 35)
        back=pygame.image.load('tt.jpg')
        text = font.render('GAME OVER', True, (255, 255, 255))
        text2 = font.render('Press R to restart the game', True, (255, 255, 255))
        kk=True
        while kk:
            mixer.music.stop() 
            over.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        font = pygame.font.SysFont('comicsansms', 35)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        mMode()
            screen.fill((0,0,0))
            screen.blit(back,(0,0))
            screen.blit(text, (150, 100))
            screen.blit(text2,(150,200))
            pygame.display.flip()
        

    def game():
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)
        running = True
        gameOver = False
        font = pygame.font.SysFont('comicsansms', 35)
        font1 = pygame.font.SysFont('comicsansms', 15)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    myclient.connection.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        myclient.connection.close()
                    if event.key in MOVE_KEYS:
                        myclient.turn_tank(myclient.token, MOVE_KEYS[event.key])
                    if event.key == pygame.K_SPACE:
                        shoot.play()
                        myclient.fire_bullet(myclient.token)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        mMode()
            try:
                remaining_time = event_client.response['remainingTime']
                text = font.render('Remaining Time: {}'.format(remaining_time), True, medqyzyl) 
                screen.blit(text, (300, 100))
                tanks = event_client.response['gameField']['tanks']
                bullets = event_client.response['gameField']['bullets']
                kickeds=event_client.response['kicked']
                winners=event_client.response['winners']
                losers=event_client.response['losers'] 
                    # if tank['id'] == client.tank_id:
                    #     dtank(tank_x, tank_y, tank_width, tank_height, tank_direction, tank_health, tank_score, (0, 255, 0))
                    #     text1 = font1.render("health: {}".format(int(tank['id'][5:]))+"   {}".format(tank['health']), True, (255, 0, 0))
                    #     screen.blit(text1, (830, 50))
                    #     text2 = font1.render("score: {}".format(int(tank['id'][5:]))+"   {}".format(tank['score']) , True, (255, 0, 0))
                    #     screen.blit(text2, (834, 70))
                    # else:
                    #     plus = 40
                        
                    #     dtank(tank_x, tank_y, tank_width, tank_height, tank_direction, tank_health, tank_score, (0, 0, 255))
                    #     for i in range(1, len(tanks)):
                    #         text3 = font1.render("health: {}".format(int(tank['id'][5:]))+"   {}".format(tank['health']), True, (255, 255, 255))
                    #         screen.blit(text3, (830, tab_coordinates))
                    #         text4 = font1.render("score: {}".format(int(tank['id'][5:]))+"  {}".format(tank['score']), True, (255, 255, 255))
                    #         screen.blit(text4, (834, tab_coordinates+20))
                    #         tab_coordinates += plus
                # tanks = sorted(tanks, key=lambda k: k['score'], reverse=True)
                tanks.sort(key=sortScore,reverse=True)
                y_cor = 110
                plus = 20
                for tank in tanks:
                    tank_x = tank['x']
                    tank_y = tank['y']
                    tank_width = tank['width']
                    tank_height = tank['height']
                    tank_direction = tank['direction']
                    tank_health = tank['health']
                    tank_score = tank['score']
                    if tank['id'] == myclient.tank_id:
                        dtank(tank_x, tank_y, tank_width, tank_height, tank_direction, tank_health, tank_score, (35,187,17))
                        text=font1.render("Your states:",True, (35,187,17))
                        screen.blit(text,(850,50))
                        text1 = font1.render("ID:{} ".format(int(tank['id'][5:]))+" health: {} ".format(tank['health'])+" score: "+" {}".format(tank['score']), True,(35,187,17))
                        screen.blit(text1, (850, 70))
                        text2 = font1.render('Opponents states:', True, (255,170,35))
                        screen.blit(text2, (850, 90))
                    else:
                        dtank(tank_x, tank_y, tank_width, tank_height, tank_direction, tank_health, tank_score, (255,170,35))               
                        text1 = font1.render("ID:{} ".format(int(tank['id'][5:]))+" health: {} ".format(tank['health'])+" score: "+" {}".format(tank['score']), True, (255, 170, 35))
                        screen.blit(text1, (850, y_cor))
                        y_cor += plus
                for bullet in bullets:                  
                    bullet_x = bullet['x']
                    bullet_y = bullet['y']
                    bullet_width = bullet['width']
                    bullet_height = bullet['height']
                    bullet_direction = bullet['direction']
                    if bullet['owner'] == myclient.tank_id:
                        dbullet(bullet_x, bullet_y, bullet_width, bullet_height, bullet_direction, (35,187,17) )
                    else:
                        dbullet(bullet_x, bullet_y, bullet_width, bullet_height, bullet_direction, (255,170,35) ) 
                        # if bullet_x >
                pygame.draw.line(screen, (34,177,76), (800,0), (800, 600), 2)
                for best in winners:
                    best_score = best['score']
                    best_id = best['tankId']            
                    if best_id == myclient.tank_id:
                        print(0)
                        best_tank(best_id,best_score)  
                for loser in losers:
                    loser_score = loser['score']
                    loser_id = loser['tankId']
                    if loser_id == myclient.tank_id:
                        print(1)
                        ggtank(loser_id,loser_score)
                if remaining_time == 0:
                    game_over()
                for kicked in kickeds:
                    kicked_id = kicked['tankId']
                    kicked_score = kicked['score']
                    if kicked_id == myclient.tank_id:
                        print(21)
                        kick_tank(kicked_id,kicked_score)
                hits = event_client.response['hits']
                for hit in hits:
                    hit.play()
            except:
                pass
            
            pygame.display.update()
            pygame.display.flip()
            screen.fill(aqtus)
        myclient.connection.close()
        

    myclient = TankRpcClient()
    myclient.check_server_status()
    myclient.obtain_token('room-'+str(roomID))
    event_client = TankConsumerClient('room-'+str(roomID))
    event_client.start()
    game()
def AIMode():
    over = mixer.Sound("gameover.wav")
    pygame.mixer.music.load(path.join('back.mp3'))
    hit = mixer.Sound("hit.wav")
    roomID = 22
    pygame.init()
    qaratus = (0,0,0)
    aqtus = (255, 255, 255)
    screen = pygame.display.set_mode((1200, 600))
    screenwidth = 1050
    screenheight = 600
    IP = '34.254.177.17'
    PORT = 5672
    VIRTUAL_HOST = 'dar-tanks'
    USER = 'dar-tanks'
    PASSWORD = '5orPLExUYnyVYZg48caMpX'
    tank_id = ''

    def sortScore(score):
        return score['score']

    class TankRpcClient():
        
        def __init__(self):
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host = IP,
                    port = PORT,
                    virtual_host = VIRTUAL_HOST,
                    credentials=pika.PlainCredentials(
                        username = USER,
                        password = PASSWORD
                    )
                )
            )
            self.channel = self.connection.channel()
            queue = self.channel.queue_declare(queue='',auto_delete=True,exclusive=True)
            self.callback_queue = queue.method.queue
            self.channel.queue_bind(
                exchange='X:routing.topic',
                queue = self.callback_queue)

            self.channel.basic_consume(
                queue=self.callback_queue,
                on_message_callback=self.on_response,
                auto_ack=True
            )

            self.response = None
            self.corr_id = None
            self.token = None
            self.tank_id = None
            self.room_id = None

        def on_response(self, ch, method, props, body):
            if self.corr_id == props.correlation_id:
                self.response = json.loads(body)
                print(self.response)
    

        def call(self, key, message={}):
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(
                exchange='X:routing.topic',
                routing_key=key,
                properties=pika.BasicProperties(
                    reply_to=self.callback_queue,
                    correlation_id=self.corr_id,
                ),
                body=json.dumps(message)
                )
            while self.response is None:
                self.connection.process_data_events()
        
        def check_server_status(self):
            self.call('tank.request.healthcheck')
            return self.response['status'] == '200'
        
        def obtain_token(self, room_id):
            
            message = {
                'roomId': room_id
            }
            self.call('tank.request.register', message)
            if 'token' in self.response:
                self.token = self.response['token']
                self.tank_id = self.response['tankId']
                if self.tank_id == myclient.tank_id:
                    return 1
                else : return 0
                self.room_id = self.response['roomId']
                return True
            return False


        def turn_tank(self, token, direction):
            message = {
                'token': token,
                'direction': direction
            }
            self.call('tank.request.turn', message)

        def fire_bullet(self, token):
            message = {
                'token': token
            }
            self.call('tank.request.fire', message)

    class TankConsumerClient(Thread):
        def __init__(self, room_id):
            super().__init__()
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host = IP,
                    port = PORT,
                    virtual_host = VIRTUAL_HOST,
                    credentials=pika.PlainCredentials(
                        username = USER,
                        password = PASSWORD
                    )
                )
            )
            self.channel = self.connection.channel()
            queue = self.channel.queue_declare(queue='',auto_delete=True,exclusive=True)

            event_listener = queue.method.queue
            self.channel.queue_bind(exchange='X:routing.topic', queue=event_listener, routing_key='event.state.'+room_id)

            self.channel.basic_consume(
                queue=event_listener,
                on_message_callback=self.on_response,
                auto_ack=True
            )
            self.response = None
        def on_response(self, ch, method, props, body):
            self.response = json.loads(body)
        def run(self):
            self.channel.start_consuming()
        def close(self):
            self.connection.close()

    UP = 'UP'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'

    MOVE_KEYS = {
        pygame.K_UP: UP,
        pygame.K_DOWN: DOWN,
        pygame.K_RIGHT: RIGHT,
        pygame.K_LEFT: LEFT
    }
    #playerim = pygame.image.load('t1_up.png')

    def dtank(x, y, width, height, direction, health, score, color):
            tx = (x + int(width / 2), y + int(width / 2))
            pygame.draw.rect(screen, color,(x, y, width, height), 2)
            pygame.draw.circle(screen, color, tx, width // 2)                   
    def dbullet(x, y, width, height, direction, color ):
            pygame.draw.rect(screen, color, (x, y, width, height))

    # def hit_t(source, destination):
    #     hit_t.destination = destination
    #     if destination == client.tank_id:
    #         tank['health'] -= 1
    # '''all_sprites = pygame.sprite.Group()
    # player = Player(100, 300, 31)
    # all_sprites.add(player)'''
    def best_tank(tankId,score):
        mixer.music.stop() 
        over.play()
        font = pygame.font.SysFont('comicsansms', 35)
        back=pygame.image.load('tt.jpg')
        text_score = font.render('SCORE: {}'.format(score), True, (255, 255, 255))
        text = font.render('YOU ARE WINNER', True, (255, 255, 255))
        text2 = font.render('Press R to restart the game', True, (255, 255, 255))
        ww=True
        while ww:
            mixer.music.stop() 
            over.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        font = pygame.font.SysFont('comicsansms', 35)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        AIMode()
            screen.fill((0,0,0)) 
            screen.blit(back,(0,0))
            screen.blit(text, (150, 100))
            screen.blit(text_score, (350, 470))
            screen.blit(text2,(150,200))
            pygame.display.flip()
    def ggtank(tankId,score):
        font = pygame.font.SysFont('comicsansms', 35)
        back=pygame.image.load('tt.jpg')
        text_score = font.render('SCORE: {}'.format(score), True, (255, 255, 255))
        text = font.render('YOU ARE LOSER', True, (255, 255, 255))
        text2 = font.render('Press R to restart the game', True, (255, 255, 255))
        
        ll=True
        while ll:
            mixer.music.stop() 
            over.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        font = pygame.font.SysFont('comicsansms', 35)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        AIMode()
            screen.fill((0,0,0)) 
            screen.blit(back,(0,0))
            screen.blit(text, (150, 100))
            screen.blit(text_score, (350, 470))
            screen.blit(text2,(150,200))
            pygame.display.flip()
        
    def kick_tank(tankId,score):
        over.play()
        font = pygame.font.SysFont('comicsansms', 35)
        back=pygame.image.load('tt.jpg')
        text_score = font.render('SCORE: {}'.format(score), True, (255, 255, 255))
        text = font.render('YOU ARE KICKED', True, (255, 255, 255))
        text2 = font.render('Press R to restart the game', True, (255, 255, 255))
        kk=True
        while kk:
            mixer.music.stop() 
            over.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        font = pygame.font.SysFont('comicsansms', 35)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        AIMode()
            screen.fill((0,0,0))
            screen.blit(back,(0,0))
            screen.blit(text, (150, 100))
            screen.blit(text_score, (350, 470))
            screen.blit(text2,(150,200))
            pygame.display.flip()
        

    def game_over():
        font = pygame.font.SysFont('comicsansms', 35)
        back=pygame.image.load('tt.jpg')
        text = font.render('GAME OVER', True, (255, 255, 255))
        text2 = font.render('Press R to restart the game', True, (255, 255, 255))
        kk=True
        while kk:
            mixer.music.stop() 
            over.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        font = pygame.font.SysFont('comicsansms', 35)
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        mMode()
            screen.fill((0,0,0))
            screen.blit(back,(0,0))
            screen.blit(text, (150, 100))
            screen.blit(text2,(150,200))
            pygame.display.flip()

    def game():
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)
        backg=pygame.image.load('flash.jpg')
        running = True
        gameOver = False
        font = pygame.font.SysFont('comicsansms', 30)
        font1 = pygame.font.SysFont('comicsansms', 15)
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    myclient.connection.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        myclient.connection.close()
                    if event.key == pygame.K_r:
                        event_client.channel.stop_consuming()
                        # pygame.quit()
                        # subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                        AIMode()    
            try:
                remaining_time = event_client.response['remainingTime']
                text = font.render('Remaining Time: {}'.format(remaining_time), True, medqyzyl) 
                screen.blit(text, (300, 100))
                tanks = event_client.response['gameField']['tanks'] 
                tanks2 = event_client.response['gameField']['tanks']  
                winners = event_client.response['winners']  
                ggs = event_client.response['losers']
                kickeds = event_client.response['kicked']
                    # if tank['id'] == client.tank_id:
                    #     dtank(tank_x, tank_y, tank_width, tank_height, tank_direction, tank_health, tank_score, (0, 255, 0))
                    #     text1 = font1.render("health: {}".format(int(tank['id'][5:]))+"   {}".format(tank['health']), True, (255, 0, 0))
                    #     screen.blit(text1, (830, 50))
                    #     text2 = font1.render("score: {}".format(int(tank['id'][5:]))+"   {}".format(tank['score']) , True, (255, 0, 0))
                    #     screen.blit(text2, (834, 70))
                    # else:
                    #     plus = 40
                        
                    #     dtank(tank_x, tank_y, tank_width, tank_height, tank_direction, tank_health, tank_score, (0, 0, 255))
                    #     for i in range(1, len(tanks)):
                    #         text3 = font1.render("health: {}".format(int(tank['id'][5:]))+"   {}".format(tank['health']), True, (255, 255, 255))
                    #         screen.blit(text3, (830, tab_coordinates))
                    #         text4 = font1.render("score: {}".format(int(tank['id'][5:]))+"  {}".format(tank['score']), True, (255, 255, 255))
                    #         screen.blit(text4, (834, tab_coordinates+20))
                    #         tab_coordinates += plus
                bullets = event_client.response['gameField']['bullets']
                tanks.sort(key=sortScore,reverse=True)
                y_cor = 110
                plus = 20
                for tank in tanks:
                    tank_x = tank['x']
                    tank_y = tank['y']
                    tank_width = tank['width']
                    tank_height = tank['height']
                    tank_direction = tank['direction']
                    tank_health = tank['health']
                    tank_score = tank['score']
                    if tank['id'] == myclient.tank_id:
                        mytankx=tank['x']
                        mytanky=tank['y']
                        dtank(tank_x, tank_y, tank_width, tank_height, tank_direction, tank_health, tank_score, (35,187,17))
                        text=font1.render("Your states:",True, (35,187,17))
                        screen.blit(text,(850,50))
                        text1 = font1.render("ID:{} ".format(int(tank['id'][5:]))+" health: {} ".format(tank['health'])+" score: "+" {}".format(tank['score']), True, (35,187,17))
                        screen.blit(text1, (850, 70))
                        text2 = font1.render('Opponents states:', True, (255,170,35))
                        screen.blit(text2, (850, 90))
                    else:
                        dtank(tank_x, tank_y, tank_width, tank_height, tank_direction, tank_health, tank_score, (255,170,35))               
                        text1 = font1.render("ID:{} ".format(int(tank['id'][5:]))+" health: {} ".format(tank['health'])+" score: "+" {}".format(tank['score']), True, (255, 170, 35))
                        screen.blit(text1, (850, y_cor))
                        y_cor += plus
                for tank in tanks:
                    tank_x = tank['x']
                    tank_y = tank['y']
                    tank_width = tank['width']
                    tank_height = tank['height']
                    tank_direction = tank['direction']
                    tank_health = tank['health']
                    tank_score = tank['score']
                    if tank['id'] == myclient.tank_id:
                        for oinaubilmeitinder in tanks2:
                            oinaubilmeitinder_x = oinaubilmeitinder['x']
                            oinaubilmeitinder_y = oinaubilmeitinder['y']
                            oinaubilmeitinder_direction = oinaubilmeitinder['direction']
                            if oinaubilmeitinder['id'] != myclient.tank_id:
                                if oinaubilmeitinder_x>tank['x'] and oinaubilmeitinder_x-tank['x']>120:
                                    myclient.turn_tank(myclient.token, RIGHT)
                                elif oinaubilmeitinder_x<tank['x'] and tank['x']-oinaubilmeitinder_x>120:
                                    myclient.turn_tank(myclient.token, LEFT)
                                elif  oinaubilmeitinder_y>tank['y'] and oinaubilmeitinder_y-tank['y']>120:
                                    myclient.turn_tank(myclient.token, DOWN)
                                elif oinaubilmeitinder_y<tank['y'] and tank['y']-oinaubilmeitinder_y>120:
                                    myclient.turn_tank(myclient.token, UP)
                                if oinaubilmeitinder_x in range (tank['x']-21,tank['x']+21) and abs(oinaubilmeitinder_y-tank['y'])>90:
                                    if oinaubilmeitinder_y>tank['y']:
                                        myclient.turn_tank(myclient.token, DOWN)
                                        myclient.fire_bullet(myclient.token)
                                        myclient.turn_tank(myclient.token,LEFT)
                                    elif oinaubilmeitinder_y<tank['y']:
                                        myclient.turn_tank(myclient.token, UP)
                                        myclient.fire_bullet(myclient.token)
                                        myclient.turn_tank(myclient.token,LEFT)
                                if oinaubilmeitinder_y in range (tank['y']-21,tank['y']+21) and abs(oinaubilmeitinder_x-tank['x'])>90:
                                    if oinaubilmeitinder_x>tank['x']:
                                        myclient.turn_tank(myclient.token, RIGHT)
                                        myclient.fire_bullet(myclient.token)
                                        myclient.turn_tank(myclient.token,UP)
                                    elif oinaubilmeitinder_x<tank['x']:
                                        myclient.turn_tank(myclient.token, LEFT)
                                        myclient.fire_bullet(myclient.token)
                                        myclient.turn_tank(myclient.token,UP)
                                if abs(oinaubilmeitinder_y-tank['y'])<64 and tank['x'] in range(oinaubilmeitinder_x,oinaubilmeitinder_x+32):
                                    if oinaubilmeitinder_y-tank['y']>0:
                                        myclient.turn_tank(myclient.token, UP)
                                    elif oinaubilmeitinder_y-tank['y']<0:
                                        myclient.turn_tank(myclient.token, DOWN)
                                if abs(oinaubilmeitinder_x-tank['x'])<64 and tank['y'] in range(oinaubilmeitinder_y,oinaubilmeitinder_y+32):
                                    if oinaubilmeitinder_x-tank['x']>0:
                                        myclient.turn_tank(myclient.token, LEFT)
                                    elif oinaubilmeitinder_x-tank['x']<0:
                                        myclient.turn_tank(myclient.token, RIGHT)

                for bullet in bullets:
                    bullet_x = bullet['x']
                    bullet_y = bullet['y']
                    bullet_width = bullet['width']
                    bullet_height = bullet['height']
                    bullet_direction = bullet['direction']
                    if bullet['owner'] == myclient.tank_id:
                        dbullet(bullet_x, bullet_y, bullet_width, bullet_height, bullet_direction, (35,187,17) )
                    else:
                        dbullet(bullet_x, bullet_y, bullet_width, bullet_height, bullet_direction, (255,170,35) )  
                for bullet in bullets:
                    bullet_x = bullet['x']
                    bullet_y = bullet['y']
                    bullet_width = bullet['width']
                    bullet_height = bullet['height']
                    bullet_direction = bullet['direction']
                    if bullet['owner'] != myclient.tank_id:
                        if (bullet['direction'] == RIGHT) or (bullet['direction'] == LEFT):
                            if bullet_y in range (mytanky,mytanky+int(16.5)):
                                myclient.turn_tank(myclient.token, DOWN)
                            if bullet_y in range (mytanky+int(16.5),mytanky+31):
                                myclient.turn_tank(myclient.token, UP)
                        if (bullet['direction'] == DOWN) or (bullet['direction'] == UP):
                            if bullet_x in range (mytankx,mytankx+int(16.5)):
                                myclient.turn_tank(myclient.token, RIGHT)
                            if bullet_x in range (mytankx+int(16.5),mytankx+31):
                                myclient.turn_tank(myclient.token, LEFT)
                        if abs(mytanky-bullet_y)<61 and ((mytanky-bullet_y<0 and bullet['direction'] == UP) or (mytanky-bullet_y>0 and bullet['direction'] == DOWN)):
                            if bullet_x in range (mytankx,mytankx+int(16.5)):
                                myclient.turn_tank(myclient.token, LEFT)
                            if bullet_x in range (mytankx+int(16.5),mytankx+31):
                                myclient.turn_tank(myclient.token, RIGHT)     
                        if abs(mytankx-bullet_x)<61 and((mytankx-bullet_x<0 and bullet['direction'] == LEFT) or (mytankx-bullet_x>0 and bullet['direction'] == RIGHT)):
                            if bullet_y in range (mytanky,mytanky+int(16.5)):
                                myclient.turn_tank(myclient.token, LEFT)
                            if bullet_y in range (mytanky+int(16.5),mytanky+31):
                                myclient.turn_tank(myclient.token, RIGHT)        
                pygame.draw.line(screen, (34,177,76), (800,0), (800, 600), 2)
                if len(tanks)==1:
                    myclient.turn_tank(myclient.token, random.choice([UP , DOWN, LEFT, RIGHT]))
                for best in winners:
                    best_score = best['score']
                    best_id = best['tankId']            
                    if best_id == myclient.tank_id:
                        print(0)
                        best_tank(best_id,best_score)
                
                for gg in ggs:
                    gg_score = gg['score']
                    gg_id = gg['tankId']
                    if loser_id == myclient.tank_id:
                        print(1)
                        ggtank(gg_id,gg_score)
                
                for kick in kickeds:
                    kick_id = kick['tankId']
                    kick_score = kick['score']
                    if kick_id == myclient.tank_id:
                        print(21)
                        kick_tank(kicked_id,kicked_score)
                hates = event_client.response['hits']
                for hate in hates:
                    hit.play()
                if remaining_time == 1:
                    game_over()
            except:
                pass
            pygame.display.update()
            pygame.display.flip()
            
            screen.fill(aqtus)
        myclient.connection.close()
    myclient = TankRpcClient()
    myclient.check_server_status()
    myclient.obtain_token('room-'+str(roomID))
    event_client = TankConsumerClient('room-'+str(roomID))
    event_client.start()
    game()


main_menu()