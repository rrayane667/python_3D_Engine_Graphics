import basicMesh
import Graphics
import pygame
from math import cos, sin, pi

white = (255, 255, 255)
black = (0, 0, 0)
indigo = (75,0,130)

theta, zeta, phi = 0, 0, 0

k1=400
k2=k1
d=500
WIDTH, HEIGHT = 1275,650
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



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D_Engine')

t=0

while running :
    
    screen.fill(black)
    
    t+=0.5  
    
    mx,my=pygame.mouse.get_pos()
    
    if select:
        #v=list(map(CamRot,select[0].coord))
        grph_pip.rendering(-mx*sensi, my*sensi, t)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button==1:
                
                quad = basicMesh.quad(600, [400, 0, 0], [-100,0,0])
                hierarchie.append(quad)
                grph_pip = Graphics.graphics_pipeline(quad.coord, 0, 0, proj, 300, (lambda l : pygame.draw.polygon(screen, l[1], l[0])), 0, 80, 0.1, 0.1, 0.2, quad.center)
                select = [quad]
                
    
    pygame.display.update()
pygame.quit() 
