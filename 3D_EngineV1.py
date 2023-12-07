
import pygame
from math import cos, sin, asin, acos, pi
from math import exp
from math import sqrt

pygame.init()
res=1
rayon=1.5
c=100
theta = 0
phi=0
zeta=0
face=[]
pf=[[],[],[],[],[],[]]
#kl=[]
click=False
c_click=False
ox, oy=0,0
t=0

k1=2500
k2=k1
d=500

white=(255,255,255)
black=(0,0,0)
WIDTH, HEIGHT = 900*1.4,500*1.4

mx, my=WIDTH/2,HEIGHT/2
cx, cy=0, 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(black)
running = True
x1=[]
y1=[]
z1=[]

#calcul des coordonnées en 3-dimensions
for j in range(0,res+1):
    for i in range(0,res+1):
        for k in range(0,res+1):    
            t1=i/res
            t2=j/res
            t3=k/res
            x=(-c*t1+(1-t1)*c)
            y=(-c*t2+(1-t2)*c)
            z=(-c*t3+(1-t3)*c)
         
            x1.append(x)
            y1.append(y)
            z1.append(z)

def arccos(cosinus,sinus):
    if sinus<=0:
        return -acos(cosinus) 
    else:
        return acos(cosinus)   
def arcsinus(cosinus,sinus):
    if cosinus<=0:
        return pi-asin(sinus) 
    else:
        return asin(cosinus)
     
def igrec(y, z,d1):
   return(k2*y/(z+d1+k1)+HEIGHT/2)

def ix(x, z,d1):
    return(k1*x/(z+d1+k1)+WIDTH/2)

#supp les points à l'intérieur du cube
min_x=min(x1)
max_x=max(x1)

min_y=min(y1)
max_y=max(y1)

min_z=min(z1)
max_z=max(z1)

coord=[]
for i in range(0,len(x1)):
    if min_x==x1[i]:
        coord.append([x1[i],y1[i],z1[i]])  
face.append(coord)
coord=[]
for i in range(0,len(x1)):
    if max_x==x1[i]:
        coord.append([x1[i],y1[i],z1[i]])
face.append(coord)
coord=[]

for i in range(0,len(y1)):
    if min_y==y1[i]:
        coord.append([x1[i],y1[i],z1[i]])
face.append(coord)
coord=[]
for i in range(0,len(y1)):
    if max_y==y1[i]:
        coord.append([x1[i],y1[i],z1[i]])
face.append(coord)
coord=[]

for i in range(0,len(z1)):
    if min_z==z1[i]:
        coord.append([x1[i],y1[i],z1[i]])
face.append(coord)
coord=[]
for i in range(0,len(z1)):
    if max_z==z1[i]:
        coord.append([x1[i],y1[i],z1[i]])
face.append(coord)
coord=[]

while running:
    
    #t=(pygame.time.get_ticks())/1000

           
    if click==True:
        phi=oy+(my-cy)/100

        theta=ox+(mx-cx)/100
    mx,my=pygame.mouse.get_pos()
        
        
    #else:
        #pygame.mouse.set_pos(mx,my)
    #zeta=(-x/100)*sin(phi)
    #if c_click==True:
        #cx, cy=mx, my
        #print(c_click)
        #c_click=False
        

    pygame.display.update()
    screen.fill(black)
    pygame.mouse.get_rel()

    #for k in range(0,2):
    
    #projection du cube sur l'écran
    for j in range(0,6):
        for i in range(0,len(face[j])):
            x=face[j][i][0]
            y=face[j][i][1]
            z=face[j][i][2]
            Fx=(x*cos(theta)-z*sin(theta))*cos(zeta)-(y*cos(phi)-x*sin(theta)*sin(phi)-z*cos(theta)*sin(phi))*sin(zeta)
            Fy=(x*cos(theta)-z*sin(theta))*sin(zeta)+cos(zeta)*(y*cos(phi)-x*sin(theta)*sin(phi)-z*cos(theta)*sin(phi))
            Fz=y*sin(phi)+x*sin(theta)*cos(phi)+z*cos(phi)*cos(theta)

            pf[j].append([ix(Fx, Fz,d),igrec(Fy, Fz,d)])
            #produit scalaire de la normale des faces avec les rayons provenant de la caméra
            dot0=x*(cos(theta)*cos(zeta)-sin(theta)*sin(phi)*sin(zeta))+y*(cos(theta)*sin(zeta)-cos(zeta)*sin(theta)*sin(phi))+(z+d+k1)*sin(theta)*cos(phi)
            dot1=-dot0
            dot2=-x*cos(phi)*sin(zeta)+y*cos(phi)*cos(zeta)+(z+d+k1)*sin(phi)
            dot3=-dot2
            dot4=(-sin(theta)*cos(zeta)+cos(theta)*sin(phi)*sin(zeta))*x+(-sin(theta)*sin(zeta)-cos(zeta)*cos(theta)*sin(phi))*y+(z+d+k1)*cos(phi)*cos(theta)
            dot5=-dot4
            dot=[dot0,dot1,dot2,dot3,dot4,dot5]

            #pygame.draw.circle(screen,white,(ix(Fx, Fz),igrec(Fy, Fz)),rayon)
        k=dot[j]
        #if 255<k:
            #k=255
        #kl.append(k)
        if 0<k :
            #print(255*k/3101.9)
            if k<400:
                k=900
            if 255<255*k/3101.9:
                k=3101.9
            b=pf[j][2]
            pf[j][2]=pf[j][3]
            pf[j][3]=b
            pygame.draw.polygon(screen,(255*k/3101.9,255*k/3101.9,255*k/3101.9),pf[j])
            pygame.draw.polygon(screen,white,pf[j],2)

        
        #pygame.draw.polygon(screen,(0,255,0),pf[j],1)

        dx=x
        dy=y
    pf=[[],[],[],[],[],[]]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button==1:
                click=True
                cx, cy=pygame.mouse.get_pos()
                mx, my=pygame.mouse.get_pos()
            if event.button==4:
                d-=300

            if event.button==5:
                d+=300
                #bas
            

        if event.type ==pygame.MOUSEBUTTONUP:
            click=False
            ox,oy=theta,phi

#print(max(kl))
pygame.quit() 


