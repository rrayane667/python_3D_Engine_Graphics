from cgitb import text
import pygame
import basicMesh
import Graphics
from math import cos, sin

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (80, 80, 80)
griye = (200, 200, 200)
indigo = (75,0,130)
rouge = (255, 0, 0)
grine = (0, 255, 0)
bleu = (0, 0, 255)
norm = 100
tpl=[griye, grey]
axis = [[0, 0, norm], [0, norm, 0], [norm, 0, 0]]
rgb=[rouge, grine, bleu]
sensiTrans = 3
rayon=1
# variable bool pour controler rotation global/local false = local, true = global
gl = False

ROTATION =True
TRANSLATION = False

buttonName = ["cube", "sphere", "cylinder", "torus", "cone", "rotat", "trans"]
WIDTH, HEIGHT = 1275,650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D_Engine')
font = pygame.font.SysFont('opensans.ttc', 25)
text=[]
for i in range(7):    
    text.append(font.render(buttonName[i], True, griye))
# hierarchy : tous les objets de la scene
hierarchy = []
# selection : coordonnées des vertices et indice dans l'hierarchy de l'objet selectionné
selection = []
# transform : position, rotation, scale de tous les objets de la scene
transform = []

running = True
click = False
theta, phi, zeta = 0, 0, 0
x_trans, y_trans, z_trans = 0, 0, 0
ox, oy, oz = 0, 0, 0
oxt, oyt, ozt = 0, 0, 0
cx, cy = 0, 0

k1=400
k2=k1
d=500
#UI
def UI():
    screen.fill(black)
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, WIDTH, 35))
    pygame.draw.rect(screen, white, pygame.Rect(-1, 0, WIDTH + 2, 35), 1)
    return 0

# projection 3D => 2D
def igrec(y, z):
   return(k2*y/(z+d+k1)+HEIGHT/2)
def ix(x, z):
    return(k1*x/(z+d+k1)+WIDTH/2)
#applique la rotation
def mapXY(c):
    x = c[0]
    y = c[1]
    z = c[2]
    Fx=(x*cos(theta)-z*sin(theta))*cos(zeta)-(y*cos(phi)-x*sin(theta)*sin(phi)-z*cos(theta)*sin(phi))*sin(zeta)
    Fy=(x*cos(theta)-z*sin(theta))*sin(zeta)+cos(zeta)*(y*cos(phi)-x*sin(theta)*sin(phi)-z*cos(theta)*sin(phi))
    Fz=y*sin(phi)+x*sin(theta)*cos(phi)+z*cos(phi)*cos(theta)
    return [Fx, Fy, Fz]
def CamRot(v, c):
    x = v[0]
    y = v[1]
    z = c + v[2]
    Fx=(x*cos(theta)-z*sin(theta))*cos(zeta)-(y*cos(phi)-x*sin(theta)*sin(phi)-z*cos(theta)*sin(phi))*sin(zeta)
    Fy=(x*cos(theta)-z*sin(theta))*sin(zeta)+cos(zeta)*(y*cos(phi)-x*sin(theta)*sin(phi)-z*cos(theta)*sin(phi))
    Fz=y*sin(phi)+x*sin(theta)*cos(phi)+z*cos(phi)*cos(theta)
    return [Fx, Fy, Fz]
#applique la translation
def mapTrans(c):

    return [c[0] + x_trans, c[1] - y_trans, c[2] + z_trans]
# réinitialise la rotation et la translation
def NULL():
    global oxt, oyt, ozt, ox, oy, oz, x_trans, y_trans, z_trans, phi, theta, zeta
    oxt, oyt, ozt = 0, 0, 0
    ox, oy, oz = 0, 0, 0
    x_trans, y_trans, z_trans = 0, 0, 0
    phi, theta, zeta = 0, 0, 0
    return 0

while running :
    # Mvt de la souris
    mx,my=pygame.mouse.get_pos()
    # user interface
    buttonStyle = {"color" : white, "textFont" : 0, "hoverColor" : white}
    UI()
    # cube button
    xc = WIDTH/2 - 200

    for i in range(7) :
        if pygame.Rect(xc, 5, 70, 25).collidepoint(mx, my) :
            pygame.draw.rect(screen, buttonStyle["color"], pygame.Rect(xc, 5, 70, 25), border_radius=50)
        else :
            pygame.draw.rect(screen, buttonStyle["color"], pygame.Rect(xc, 5, 70, 25), 1, border_radius=50)
        screen.blit(text[i], (xc + 10, 10))
        xc+= 80

    if click and ROTATION:
        phi, theta = (oy+(my-cy)/100), ox+(mx-cx)/100#*cos(phi)
        #zeta = oz+(mx-cx)/100*sin(phi)
    if click and TRANSLATION :
        y_trans, x_trans = oyt-(my-cy)*sensiTrans, oxt+(mx-cx)*sensiTrans

    # projection en 2D et affichage
    if selection:
        crd = [ mapXY(t) for t in selection[0] ]
        hierarchy[selection[1]].center = [x_trans, -y_trans, z_trans]
        hierarchy[selection[1]].coord = crd
        c_axis = [ mapTrans(mapXY(t)) for t in  axis ]

    for k in range(len(hierarchy)) :
        j=hierarchy[k].center
        
        pygame.draw.circle(screen, indigo, (ix(j[0], j[2]), igrec(j[1], j[2])), norm/20)
        #affichage des faces
        #_
        
        for i in hierarchy[k].coord:
            v = mapXY(i)
            pygame.draw.circle( screen, white, [ix(v[0] + j[0],v[2] + j[2]), igrec(v[1] + j[1], v[2] + j[2])], rayon)
        ''' for b in [0, 1]:    
            for C in faces:
                f=[]
                for a in C:
                    f.append((ix(a[0] + j[0], a[2] + j[2]), igrec(a[1]+ j[1], a[2]+ j[2])))
                pygame.draw.polygon( screen, tpl[b], f, width = b)'''
    #affichage des axes
    if selection:
        c=0
        for i in c_axis :
            pygame.draw.aaline(screen, rgb[c], (ix(x_trans, z_trans), igrec(-y_trans, z_trans)), [ix(i[0],i[2]), igrec(i[1],i[2])])
            c+=1
        del c
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            click = True
            cx, cy=pygame.mouse.get_pos()
            # detect click ou spawn objet
            if pygame.Rect(WIDTH/2 - 200, 5, 70, 25).collidepoint(mx, my) :
                mesh = basicMesh.cube(200, [0, 0, 0])
                hierarchy.append(mesh)
                selection = [mesh.coord, len(hierarchy) - 1]
                NULL()
            if pygame.Rect(WIDTH/2 - 120, 5, 70, 25).collidepoint(mx, my) :
                mesh = basicMesh.sphere(200, [0, 0, 0], 20)
                hierarchy.append(mesh)
                selection = [mesh.coord, len(hierarchy) - 1]
                NULL()
            if pygame.Rect(WIDTH/2 - 40, 5, 70, 25).collidepoint(mx, my) :
                mesh = basicMesh.cylinder(200, 100, [0, 0, 0], 15)
                hierarchy.append(mesh)
                selection = [mesh.coord, len(hierarchy) - 1]
                NULL()
            if pygame.Rect(WIDTH/2 + 40, 5, 70, 25).collidepoint(mx, my) :
                mesh = basicMesh.torus(200, 400, [0, 0, 0], 40)
                hierarchy.append(mesh)
                selection = [mesh.coord, len(hierarchy) - 1]
                NULL()
            if pygame.Rect(WIDTH/2 + 120, 5, 70, 25).collidepoint(mx, my) :
                mesh = basicMesh.cone(200, 300, [0, 0, 0], 20)
                hierarchy.append(mesh)
                selection = [mesh.coord, len(hierarchy) - 1]
                NULL()
            if pygame.Rect(WIDTH/2 + 200, 5, 70, 25).collidepoint(mx, my) :
                ROTATION = True
                TRANSLATION = False
            if pygame.Rect(WIDTH/2 + 280, 5, 70, 25).collidepoint(mx, my) :
                ROTATION = False
                TRANSLATION = True
            
            for i in hierarchy:
                n=norm/2
                j=i.center
                if pygame.Rect(ix(j[0], j[2]) - n/2, igrec(j[1], j[2]) - n/2, n, n).collidepoint(mx , my ):
                    selection=[i.coord, hierarchy.index(i)]
                    NULL(); oyt, oxt = -((my-cy)*sensiTrans + j[1]), (mx-cx)*sensiTrans + j[0]
                    if ROTATION : x_trans, y_trans= j[0], -j[1]

        if event.type ==pygame.MOUSEBUTTONUP:
            if event.button==1 and ROTATION:
                click=False
                ox,oy, oz = theta, phi, zeta
                
            if event.button==1 and TRANSLATION:
                click=False
                oxt, oyt, ozt = x_trans, y_trans, z_trans
    pygame.display.update()
pygame.quit() 