import pygame as py
import random
import math
from matplotlib import pyplot

py.init()
WIDTH = 1600
HEIGHT = 1600
screen = py.display.set_mode((WIDTH,HEIGHT))
screen.fill([255,255,255])
py.display.set_caption("Gas Simulation")
FPS = 120
SOLO = False
#버튼으로 켰다 껐다 하기
mass = 2
radius = 10
intensity = 0.99   #it should be more than 0.5, less then 1.0
validrange = 200**2

h_l0 = HEIGHT*0.0
h_l1 = HEIGHT*0.4
h_l2 = HEIGHT*0.6
h_l3 = HEIGHT*1.0
h_r0 = HEIGHT*0.0
h_r1 = HEIGHT*0.4
h_r2 = HEIGHT*0.6
h_r3 = HEIGHT*1.0
p_l = WIDTH*0.33
p_r = WIDTH*0.67
b_w = 10
class Particle():
    def __init__(self, tag, x, y, v_x, v_y, color):
        self.tag = tag
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.a_x = 0.0
        self.a_y = 0.01
        self.m = mass
        self.radius = radius
        self.color = color
    def accelate(self):
        self.v_x += self.a_x
        self.v_y += self.a_y
    def move(self):
        self.x += self.v_x
        self.y += self.v_y
        if SOLO == True:
            if self.tag%5 == 1:
                py.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 0)
        else:
            py.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 0)
    def collide_wall(self):
        if self.y - self.radius <= 0:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -(self.v_y)
        if self.y + self.radius >= HEIGHT:
            if self.v_y >= 0:
                self.v_y = -(self.v_y)
            if self.v_y < 0:    
                self.v_y = self.v_y
        if self.x - self.radius <= 0:
            if self.v_x >= 0:
                self.v_x = self.v_x
            if self.v_x < 0:
                self.v_x = -(self.v_x)
            #self.x = WIDTH - self.radius - 1
        if self.x + self.radius >= WIDTH:
            if self.v_x >= 0:
                self.v_x = -(self.v_x)
            if self.v_x < 0:
                self.v_x = self.v_x
            #self.x = 0 + self.radius + 1
    def collide_barrier_class(self):
        if self.y + self.radius >= h_l0 and self.x >= p_l - b_w and self.x <= p_l + b_w:
            if self.v_y <= 0:
                self.v_y = self.v_y
            if self.v_y > 0:    
                self.v_y = -self.v_y
        if self.y - self.radius <= h_l1 and self.x >= p_l - b_w and self.x <= p_l + b_w:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -self.v_y
        if self.y + self.radius >= h_l2 and self.x >= p_l - b_w and self.x <= p_l + b_w:
            if self.v_y <= 0:
                self.v_y = self.v_y
            if self.v_y > 0:    
                self.v_y = -self.v_y
        if self.y - self.radius <= h_l3 and self.x >= p_l - b_w and self.x <= p_l + b_w:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -self.v_y
        if self.y + self.radius >= h_r0 and self.x >= p_r - b_w and self.x <= p_r + b_w:
            if self.v_y <= 0:
                self.v_y = self.v_y
            if self.v_y > 0:    
                self.v_y = -self.v_y
        if self.y - self.radius <= h_r1 and self.x >= p_r - b_w and self.x <= p_r + b_w:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -self.v_y
        if self.y + self.radius >= h_r2 and self.x >= p_r - b_w and self.x <= p_r + b_w:
            if self.v_y <= 0:
                self.v_y = self.v_y
            if self.v_y > 0:    
                self.v_y = -self.v_y
        if self.y - self.radius <= h_r3 and self.x >= p_r - b_w and self.x <= p_r + b_w:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -self.v_y
        if self.x + self.radius >= p_l - b_w and self.x <= p_l and ((self.y >= h_l0 and self.y <= h_l1) or (self.y >= h_l2 and self.y <= h_l3)):
            if self.v_x <= 0:
                self.v_x = self.v_x
            if self.v_x > 0:    
                self.v_x = -self.v_x
        if self.x - self.radius <= p_l + b_w and self.x >= p_l and ((self.y >= h_l0 and self.y <= h_l1) or (self.y >= h_l2 and self.y <= h_l3)):
            if self.v_x >= 0:
                self.v_x = self.v_x
            if self.v_x < 0:    
                self.v_x = -self.v_x
        if self.x + self.radius >= p_r - b_w and self.x <= p_r and ((self.y >= h_r0 and self.y <= h_r1) or (self.y >= h_r2 and self.y <= h_r3)): 
            if self.v_x <= 0:
                self.v_x = self.v_x
            if self.v_x > 0:    
                self.v_x = -self.v_x
        if self.x - self.radius <= p_r + b_w and self.x >= p_r and ((self.y >= h_r0 and self.y <= h_r1) or (self.y >= h_r2 and self.y <= h_r3)):
            if self.v_x >= 0:
                self.v_x = self.v_x
            if self.v_x < 0:    
                self.v_x = -self.v_x

        
class Heat():
    def __init__(self, x, y, v_x, v_y):
        self.first_x = x
        self.first_y = y
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.a_x = 0
        self.a_y = 0
        self.m = mass
        self.radius = radius
        self.lifespan = FPS #Lifespan
    def aging(self):
        self.lifespan -= 1        
    def accelate(self):
        self.v_x += self.a_x
        self.v_y += self.a_y
    def move(self):
        self.x += self.v_x
        self.y += self.v_y
        py.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius, 0)
    def collide_wall(self):
        if self.y - self.radius <= 0:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -(self.v_y)
        if self.y + self.radius >= HEIGHT:
            if self.v_y >= 0:
                self.v_y = -(self.v_y)
            if self.v_y < 0:    
                self.v_y = self.v_y
        if self.x - self.radius <= 0:
            if self.v_x >= 0:
                self.v_x = self.v_x
            if self.v_x < 0:
                self.v_x = -(self.v_x)
            #self.x = WIDTH - self.radius - 1
        if self.x + self.radius >= WIDTH:
            if self.v_x >= 0:
                self.v_x = -(self.v_x)
            if self.v_x < 0:
                self.v_x = self.v_x
            #self.x = 0 + self.radius + 1
    def collide_barrier_class(self):
        if self.y + self.radius >= h_l0 and self.x >= p_l - b_w and self.x <= p_l + b_w:
            if self.v_y <= 0:
                self.v_y = self.v_y
            if self.v_y > 0:    
                self.v_y = -self.v_y
        if self.y - self.radius <= h_l1 and self.x >= p_l - b_w and self.x <= p_l + b_w:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -self.v_y
        if self.y + self.radius >= h_l2 and self.x >= p_l - b_w and self.x <= p_l + b_w:
            if self.v_y <= 0:
                self.v_y = self.v_y
            if self.v_y > 0:    
                self.v_y = -self.v_y
        if self.y - self.radius <= h_l3 and self.x >= p_l - b_w and self.x <= p_l + b_w:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -self.v_y
        if self.y + self.radius >= h_r0 and self.x >= p_r - b_w and self.x <= p_r + b_w:
            if self.v_y <= 0:
                self.v_y = self.v_y
            if self.v_y > 0:    
                self.v_y = -self.v_y
        if self.y - self.radius <= h_r1 and self.x >= p_r - b_w and self.x <= p_r + b_w:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -self.v_y
        if self.y + self.radius >= h_r2 and self.x >= p_r - b_w and self.x <= p_r + b_w:
            if self.v_y <= 0:
                self.v_y = self.v_y
            if self.v_y > 0:    
                self.v_y = -self.v_y
        if self.y - self.radius <= h_r3 and self.x >= p_r - b_w and self.x <= p_r + b_w:
            if self.v_y >= 0:
                self.v_y = self.v_y
            if self.v_y < 0:    
                self.v_y = -self.v_y
        if self.x + self.radius >= p_l - b_w and self.x <= p_l and ((self.y >= h_l0 and self.y <= h_l1) or (self.y >= h_l2 and self.y <= h_l3)):
            if self.v_x <= 0:
                self.v_x = self.v_x
            if self.v_x > 0:    
                self.v_x = -self.v_x
        if self.x - self.radius <= p_l + b_w and self.x >= p_l and ((self.y >= h_l0 and self.y <= h_l1) or (self.y >= h_l2 and self.y <= h_l3)):
            if self.v_x >= 0:
                self.v_x = self.v_x
            if self.v_x < 0:    
                self.v_x = -self.v_x
        if self.x + self.radius >= p_r - b_w and self.x <= p_r and ((self.y >= h_r0 and self.y <= h_r1) or (self.y >= h_r2 and self.y <= h_r3)): 
            if self.v_x <= 0:
                self.v_x = self.v_x
            if self.v_x > 0:    
                self.v_x = -self.v_x
        if self.x - self.radius <= p_r + b_w and self.x >= p_r and ((self.y >= h_r0 and self.y <= h_r1) or (self.y >= h_r2 and self.y <= h_r3)):
            if self.v_x >= 0:
                self.v_x = self.v_x
            if self.v_x < 0:    
                self.v_x = -self.v_x

    
particlenumber = 200
countingnumber = 0
balllist_go = []
pad = 0

for i in range(particlenumber):
    countingnumber += 1
    if countingnumber%5 == 1:
        balllist_go.append(Particle(countingnumber, random.randint(0+pad, WIDTH-pad), random.randint(0+pad, HEIGHT-pad), random.randint(-1, 1), random.randint(-1, 1), (0, 0, 255)))
    else:
        balllist_go.append(Particle(countingnumber, random.randint(0+pad, WIDTH-pad), random.randint(0+pad, HEIGHT-pad), random.randint(-1, 1), random.randint(-1, 1), (0, 255, 0)))

heatamount = 5
balllist_temporary = []
heatstartrange = 50
def heat(x, y):
    for i in range(heatamount):
        balllist_temporary.append(Heat(random.randint(int(x) - heatstartrange, int(x) + heatstartrange), random.randint(int(y) - heatstartrange, int(y) + heatstartrange), random.randint(-10, 10), random.randint(-10, 10)))
# 특정 범위 밖 넘어가면 삭제
# 마우스 클릭한 지점 주변에서 생성되도록 하기
def thermometer_whole(x):
    add_temp = 0
    for i in x:
        add_temp += 0.5*(i.m)*((i.v_x)**2 + (i.v_y)**2)
    add_temp = add_temp / particlenumber
    return add_temp
def thermometer_1(x):
    add_temp = 0
    particlenum1 = 0
    for i in x:
        if i.x >= 0 and i.x <= p_l:
            particlenum1 += 1
            add_temp += 0.5*(i.m)*((i.v_x)**2 + (i.v_y)**2)
    add_temp = add_temp / (particlenum1 + 0.001)
    return add_temp
def thermometer_2(x):
    add_temp = 0
    particlenum2 = 0
    for i in x:
        if i.x >= p_l and i.x <= p_r:
            particlenum2 += 1
            add_temp += 0.5*(i.m)*((i.v_x)**2 + (i.v_y)**2)
    add_temp = add_temp / (particlenum2 + 0.001)
    return add_temp
def thermometer_3(x):
    add_temp = 0
    particlenum3 = 0
    for i in x:
        if i.x >= p_r and i.x <= WIDTH:
            particlenum3 += 1
            add_temp += 0.5*(i.m)*((i.v_x)**2 + (i.v_y)**2)
    add_temp = add_temp / (particlenum3 + 0.001)
    return add_temp
def countparticle_1(x):
    particlenum4 = 0
    for i in x:
        if i.x >= 0 and i.x <= p_l:
            particlenum4 += 1
    return particlenum4
def countparticle_2(x):
    particlenum5 = 0
    for i in x:
        if i.x >= p_l and i.x <= p_r:
            particlenum5 += 1
    return particlenum5
def countparticle_3(x):
    particlenum6 = 0
    for i in x:
        if i.x >= p_r and i.x <= WIDTH:
            particlenum6 += 1
    return particlenum6
def draw_walls():
    py.draw.rect(screen, (100, 100, 100), py.Rect(p_l - b_w, h_l0, b_w*2, h_l1 - h_l0))
    py.draw.rect(screen, (100, 100, 100), py.Rect(p_l - b_w, h_l2, b_w*2, h_l3 - h_l2))
    py.draw.rect(screen, (100, 100, 100), py.Rect(p_r - b_w, h_r0, b_w*2, h_r1 - h_r0))
    py.draw.rect(screen, (100, 100, 100), py.Rect(p_r - b_w, h_r2, b_w*2, h_r3 - h_r2))
def collide_particle():
    global balllist_go, balllist_temporary
    List = balllist_go + balllist_temporary
    for i in range(0, len(List)-1):
        for j in range(i+1, len(List)):
            a1 = List[i]
            a2 = List[j]
            distance = math.sqrt((a1.x-a2.x)**2+(a1.y-a2.y)**2)
            if distance < 2*radius:
                impulse_x = a2.v_x - a1.v_x
                impulse_y = a2.v_y - a1.v_y
                impulse_x *= intensity
                impulse_y *= intensity
                a1.v_x += impulse_x 
                a2.v_x -= impulse_x 
                a1.v_y += impulse_y 
                a2.v_y -= impulse_y 
            List[i] = a1
            List[j] = a2
    balllist_go = List[:particlenumber]
    balllist_temporary = List[particlenumber:]
def collide_particle2():
    global balllist_go, balllist_temporary
    List = balllist_go + balllist_temporary
    for i in range(0, len(List)-1):
        for j in range(i+1, len(List)):
            a1 = List[i]
            a2 = List[j]
            distance = math.sqrt((a1.x-a2.x)**2+(a1.y-a2.y)**2)
            if distance < 2*radius:
                dir_x = a2.x - a1.x 
                dir_y = a2.y - a1.y
                reg = math.sqrt((dir_x)**2 + (dir_y)**2)
                dir_x /= reg
                dir_y /= reg
                dot1 = dir_x * a1.v_x + dir_y * a1.v_y
                dot2 = -(dir_x * a2.v_x) - (dir_y * a2.v_y)
                v11x = dot1 * dir_x
                v11y = dot1 * dir_y
                v21x = -dot2 * dir_x
                v21y = -dot2 * dir_y
                v12x = a1.v_x - v11x
                v12y = a1.v_y - v11y
                v22x = a2.v_x - v21x
                v22y = a2.v_y - v21y
                impulse_x = v21x - v11x
                impulse_y = v21y - v11y
                impulse_x *= intensity
                impulse_y *= intensity
                v11x += impulse_x
                v21x -= impulse_x
                v11y += impulse_y
                v21y -= impulse_y
                a1.v_x = v11x + v12x
                a1.v_y = v11y + v12y
                a2.v_x = v21x + v22x
                a2.v_y = v21y + v22y
            List[i] = a1
            List[j] = a2
    balllist_go = List[:particlenumber]
    balllist_temporary = List[particlenumber:]
    
temperature_whole_list = []
temperature_1_list = []
temperature_2_list = []
temperature_3_list = []
xlist1, xlist2, xlist3, xlist4, ylist1, ylist2, ylist3, ylist4 = [], [], [], [], [], [], [], []
slitescapes1 = []
slitescapes2 = []
slitescapes3 = []
clock = py.time.Clock()
timetick = 0
py.display.flip()
running = True
while running:
    timetick += 1
    if timetick > FPS*20:
        pass
        #running = False
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.MOUSEBUTTONUP:
            point_x, point_y = event.pos
            heat(point_x, point_y)
        if event.type == py.KEYDOWN:
            if event.key == py.K_o:
                SOLO = True
            if event.key == py.K_p:
                SOLO = False
    if timetick % 60 == 0:
        heat(WIDTH/2, HEIGHT*(5/6))
        heat(WIDTH*(1/4), HEIGHT*(5/6))
        heat(WIDTH*(3/4), HEIGHT*(5/6))
    screen.fill((255,255,255))
    #draw_walls()
    collide_particle()
    for a in balllist_go:
        a.accelate()
        a.move()
        a.collide_wall()
        #a.collide_barrier_class()
    for b in balllist_temporary:
        b.aging()
        if b.lifespan <= 0:
            balllist_temporary.remove(b)
        if (b.x - b.first_x)**2 + (b.y - b.first_y)**2 > validrange:
            balllist_temporary.remove(b)
        b.accelate()
        b.move()
        b.collide_wall()
        #b.collide_barrier_class()
    xlist1.append(timetick)
    xlist2.append(timetick)
    xlist3.append(timetick)
    xlist4.append(timetick)
    ylist1.append(thermometer_whole(balllist_go))
    ylist2.append(thermometer_1(balllist_go))
    ylist3.append(thermometer_2(balllist_go))
    ylist4.append(thermometer_3(balllist_go))
    slitescapes1.append(countparticle_1(balllist_go))
    slitescapes2.append(countparticle_2(balllist_go))
    slitescapes3.append(countparticle_3(balllist_go))
    py.display.update()
    clock.tick(FPS)
py.quit()
pyplot.figure(figsize=(20,10))
pyplot.plot(xlist1, ylist1)
#pyplot.plot(xlist2, ylist2)
#pyplot.plot(xlist3, ylist3)
#pyplot.plot(xlist4, ylist4)
pyplot.xlabel('timetick')
pyplot.ylabel('temperature')
pyplot.title('Thermometer')
#pyplot.legend(['Whole','1','2','3'])
pyplot.show()    

pyplot.figure(figsize=(10,10))
pyplot.plot(xlist1, slitescapes1)
pyplot.plot(xlist1, slitescapes2)
pyplot.plot(xlist1, slitescapes3)
pyplot.xlabel('timetick')
pyplot.ylabel('particlenumber')
pyplot.title('countingparticles')
pyplot.legend(['1','2','3'])
pyplot.show()