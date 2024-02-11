from math import cos, sin, pi
class quad:
    def __init__(self, dim, center, name="Quad", scale=[1,1,0], rotation=[0,0,0], res=2):
        self.name = name
        self.dim = dim
        self.center = center
        name = "Quad"from math import cos, sin, pi
class quad:
    def __init__(self, dim, center, name="Quad", scale=[1,1,0], rotation=[0,0,0], res=2):
        self.name = name
        self.dim = dim
        self.center = center
        name = "Quad"
        coord=[]
        for i in range(res):
            for j in range(res):
                coord.append((i*dim/res - (1-i)*dim/res + center[0], j*dim/res - (1-j)*dim/res + center[1], center[2]))
        self.coord = coord
class cube :
    def __init__(self, dim, center=[0,0,0], name= "cube", scale = [1, 1, 1], rotation = [0, 0, 0],res=2) :
        self.name = name
        self.dim = dim
        self.res = res
        self.center = center
        name = "cube"
        coord = []
        #generation des vertices
        for i in range(res):
            for j in range(res):
                for k in range(res):
                    x = i*dim/2 - (1-i)*dim/2 + center[0]
                    y = j*dim/2 - (1-j)*dim/2 + center[1]
                    z = k*dim/2 - (1-k)*dim/2 + center[2]
                    coord.append([x,y,z])
        self.coord = coord
        l1, l2 = coord[:4], coord[4:]
        l1[2], l1[3] = l1[3], l1[2]; l2[2], l2[3] = l2[3], l2[2]
        self.faces = [l1] +[l2] +[[l1[i], l1[(i+1)%4], l2[(i+1)%4], l2[i]] for i in range(4)]
class sphere :
    def __init__(self, radius, center, res, name = "sphere", scale = [1, 1, 1], rotation = [0, 0, 0]):
        self.radius = radius
        self.center = center
        self.res = res
        coord = []
        #generation des vertices
        for i in range(res):
            for j in range(res):
                x = radius*cos(2*pi*j/res)*sin(2*pi*i/res) + center[0]
                y = radius*sin(2*pi*j/res)*sin(2*pi*i/res) + center[1]
                z = radius*cos(2*pi*i/res) + center[2]
                coord.append([x,y,z])
        self.coord = coord
class cylinder:
    def __init__(self, hauteur, radius, center, res, name = "cylinder", scale = [1, 1, 1], rotation = [0, 0, 0]):
        self.center = center
        self.hauteur = hauteur
        self.radius = radius
        self.res = res
        coord = []
        #generation des vertices
        for i in range(res):
            for j in range(res):
                x = radius*cos(2*pi*j/res)
                y = -i/res*hauteur/2 + (1-i/res)*hauteur
                z = radius*sin(2*pi*j/res)
                coord.append([x, y ,z])
        self.coord = coord
class torus :
    def __init__(self, innerRadius, outerRadius, center, res, name = "torus", scale = [1, 1, 1], rotation = [0, 0, 0]):
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.center = center
        self.res = res
        coord =[]
        #generation des vertices
        for i in range(res):
            for j in range(res):
                x = (outerRadius + innerRadius*cos(2*pi*j/res))*cos(2*pi*i/res) + center[0]
                y = innerRadius*sin(2*pi*j/res) + center[2]
                z = (outerRadius + innerRadius*cos(2*pi*j/res))*sin(2*pi*i/res) + center[1]
                coord.append([x,y,z])
        self.coord = coord
class cone:
    def __init__(self, radius, hauteur, center, res, name = "cone", scale = [1, 1, 1], rotation = [0, 0, 0]):
        self.radius = radius
        self.hauteur = hauteur
        self.center = center
        self.res = res
        coord = []
        #generation des vertices
        for i in range(res):
            for j in range(res):
                x = ((1-i/res)*radius)*cos(2*pi*j/res)
                y = -hauteur/2*i/res + hauteur/2*(1-i/res)
                z = ((1-i/res)*radius)*sin(2*pi*j/res)
                coord.append([x, y, z])
        self.coord = coord



        coord=[]
        for i in range(res):
            for j in range(res):
                coord.append((i*dim/res - (1-i)*dim/res + center[0], j*dim/res - (1-j)*dim/res + center[1], center[2]))
        self.coord = coord
class cube :
    def __init__(self, dim, center=[0,0,0], name= "cube", scale = [1, 1, 1], rotation = [0, 0, 0],res=2) :
        self.name = name
        self.dim = dim
        self.res = res
        self.center = center
        name = "cube"
        coord = []
        #generation des vertices
        for i in range(res):
            for j in range(res):
                for k in range(res):
                    x = i*dim/2 - (1-i)*dim/2 + center[0]
                    y = j*dim/2 - (1-j)*dim/2 + center[1]
                    z = k*dim/2 - (1-k)*dim/2 + center[2]
                    coord.append([x,y,z])
        self.coord = coord
        l1, l2 = coord[:4], coord[4:]
        l1[2], l1[3] = l1[3], l1[2]; l2[2], l2[3] = l2[3], l2[2]
        self.faces = [l1] +[l2] +[[l1[i], l1[(i+1)%4], l2[(i+1)%4], l2[i]] for i in range(4)]
class sphere :
    def __init__(self, radius, center, res, name = "sphere", scale = [1, 1, 1], rotation = [0, 0, 0]):
        self.radius = radius
        self.center = center
        self.res = res
        coord = []
        #generation des vertices
        for i in range(res):
            for j in range(res):
                x = radius*cos(2*pi*j/res)*sin(2*pi*i/res) + center[0]
                y = radius*sin(2*pi*j/res)*sin(2*pi*i/res) + center[1]
                z = radius*cos(2*pi*i/res) + center[2]
                coord.append([x,y,z])
        self.coord = coord
class cylinder:
    def __init__(self, hauteur, radius, center, res, name = "cylinder", scale = [1, 1, 1], rotation = [0, 0, 0]):
        self.center = center
        self.hauteur = hauteur
        self.radius = radius
        self.res = res
        coord = []
        #generation des vertices
        for i in range(res):
            for j in range(res):
                x = radius*cos(2*pi*j/res)
                y = -i/res*hauteur/2 + (1-i/res)*hauteur
                z = radius*sin(2*pi*j/res)
                coord.append([x, y ,z])
        self.coord = coord
class torus :
    def __init__(self, innerRadius, outerRadius, center, res, name = "torus", scale = [1, 1, 1], rotation = [0, 0, 0]):
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.center = center
        self.res = res
        coord =[]
        #generation des vertices
        for i in range(res):
            for j in range(res):
                x = (outerRadius + innerRadius*cos(2*pi*j/res))*cos(2*pi*i/res) + center[0]
                y = innerRadius*sin(2*pi*j/res) + center[2]
                z = (outerRadius + innerRadius*cos(2*pi*j/res))*sin(2*pi*i/res) + center[1]
                coord.append([x,y,z])
        self.coord = coord
class cone:
    def __init__(self, radius, hauteur, center, res, name = "cone", scale = [1, 1, 1], rotation = [0, 0, 0]):
        self.radius = radius
        self.hauteur = hauteur
        self.center = center
        self.res = res
        coord = []
        #generation des vertices
        for i in range(res):
            for j in range(res):
                x = ((1-i/res)*radius)*cos(2*pi*j/res)
                y = -hauteur/2*i/res + hauteur/2*(1-i/res)
                z = ((1-i/res)*radius)*sin(2*pi*j/res)
                coord.append([x, y, z])
        self.coord = coord


