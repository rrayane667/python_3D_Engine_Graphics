import basicMesh
import Graphics
import Illumination
import pygame
from math import cos, sin, pi, sqrtimport basicMesh
import Graphics
import Illumination
import pygame
from math import cos, sin, pi, sqrt

white = (255, 255, 255)
black = (0, 0, 0)
indigo = (75,0,130)


theta, zeta, phi = 0, 0, 0

k1=400
k2=k1
d=500
WIDTH, HEIGHT = 1275, 650
running = True
sensi = 0.01

hierarchie = []
select = []


#fonction projection 3D->2D
def igrec(y, z):
   return(k2*y/(z+d+k1)+HEIGHT/2)
def ix(x, z):
    return(k1*x/(z+d+k1)+WIDTH/2)

def proj(L):
    return [k1*L[0]/(L[2]+d+k1)+WIDTH/2, k1*L[1]/(L[2]+d+k1)+HEIGHT/2]
def norm(u):
    return sqrt(u[0]**2 + u[1]**2 + u[2]**2)
def diffVect(u, v):
    return [u[0]-v[0], u[1]-v[1], u[2]-v[2]]
def disc(x, y):
    return (x,y,20*sin(0.01*x + 0.02*y))
    #return [x, y, 0]
def grad(x, y):
    return [-20*0.02*cos(0.01*x + 0.02*y ), 0, 20*0.01*cos(0.01*x + 0.02*y )]
    #return [0,0,0]


screen = pygame.display.set_mode((WIDTH, HEIGHT))

class light:
    def __init__(self, lightType, lightIntensity, lightPosition, innerRadiusAngle, outerRadiusAngle):
        self.lightType = lightType # lightType = 0 -
        self.lightIntensity = lightIntensity
        self.lightPosition = lightPosition
        self.innerRadiusAngle = innerRadiusAngle
        self.outerRadiusAngle = outerRadiusAngle

spotLight = light(0, 0.8, [0, 0, -400], 0.8, 0.6)
    

    

t=0

while running :
    
    screen.fill(black)
    
    t+=0.5  
    
    mx,my=pygame.mouse.get_pos()
    pygame.display.set_caption(f'3D_Engine mx:{mx*sensi},my: {my*sensi}')

    
    if select:
        for i in range(len(triangles)):
            pygame.draw.circle(screen, indigo, proj(spotLight.lightPosition), 5)
            pygame.draw.polygon(screen, colors[i], (triangles[i][0], triangles[i][1], triangles[i][2]))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button==1:
                quad = basicMesh.quad(600, [400, 0, 0], [-100,0,0])
                hierarchie.append(quad)
                grph_pip = Graphics.graphics_pipeline( 0, proj, 400, 400, (lambda l : pygame.draw.polygon(screen, l[1], l[0])), 0, 128, quad.center, disc, grad)
                select = [quad]
                grph_pip.rendering()
                triangles = grph_pip.triangles
                lum = Illumination.illuminationPipeline(grph_pip.normales, [0,0,-1300], grph_pip.vertex_position, spotLight, grph_pip.vertex_color)
                lum.rendering()
                colors = lum.vertex_color
                
    
    pygame.display.update()
pygame.quit() 

white = (255, 255, 255)
black = (0, 0, 0)
indigo = (75,0,130)
light = [0, 0, -500]

theta, zeta, phi = 0, 0, 0

k1=400
k2=k1
d=500
WIDTH, HEIGHT = 1275, 650
running = True
sensi = 0.01

hierarchie = []
select = []


#fonction projection 3D->2D
def igrec(y, z):
   return(k2*y/(z+d+k1)+HEIGHT/2)
def ix(x, z):
    return(k1*x/(z+d+k1)+WIDTH/2)

def proj(L):
    return [k1*L[0]/(L[2]+d+k1)+WIDTH/2, k1*L[1]/(L[2]+d+k1)+HEIGHT/2]
def norm(u):
    return sqrt(u[0]**2 + u[1]**2 + u[2]**2)
def diffVect(u, v):
    return [u[0]-v[0], u[1]-v[1], u[2]-v[2]]
def disc(x, y):
    return (x,y,20*sin(0.1*x + 0.2*y))
def grad(x, y):
    return [-20*0.2*cos(0.1*x + 0.2*y ), 0, 20*0.1*cos(0.1*x + 0.2*y )]


screen = pygame.display.set_mode((WIDTH, HEIGHT))


t=0

while running :
    
    screen.fill(black)
    
    t+=0.5  
    
    mx,my=pygame.mouse.get_pos()
    pygame.display.set_caption(f'3D_Engine mx:{mx*sensi},my: {my*sensi}')

    
    if select:
        for i in range(len(triangles)):
            pygame.draw.circle(screen, white, proj(light), 5)
            pygame.draw.polygon(screen, colors[i], (triangles[i][0], triangles[i][1], triangles[i][2]))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button==1:
                quad = basicMesh.quad(600, [400, 0, 0], [-100,0,0])
                hierarchie.append(quad)
                grph_pip = Graphics.graphics_pipeline( 0, proj, 300, 300, (lambda l : pygame.draw.polygon(screen, l[1], l[0])), 0, 16, quad.center, disc, grad)
                select = [quad]
                grph_pip.rendering()
                triangles = grph_pip.triangles
                lum = Illumination.illuminationPipeline(grph_pip.normales, [0,0,-1300], grph_pip.vertex_position, [-500, -500, -500], grph_pip.vertex_color)
                lum.rendering()
                colors = lum.vertex_color
                
    
    pygame.display.update()
pygame.quit() 
