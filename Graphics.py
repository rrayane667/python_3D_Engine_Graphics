from math import sin, cos, sqrt, floor
class graphics_pipeline :
    def __init__(self, vertex_position, vertex_color, ordre, proj, dim, draw, t, res, a, b, c, center):
        self.vertex_position = vertex_position
        self.vertex_color = vertex_color
        self.ordre = ordre
        self.proj = proj
        self.dim = dim
        self.draw = draw
        self.t = t
        self.res = res
        self.a = a
        self.b = b
        self.c = c
        self.center = center
    def CamRot(self, v, sx, sy):
        x = v[0]
        y = v[1]
        z = v[2]
        theta = sx
        phi = sy
        zeta = 0
        Fx=(x*cos(theta)-z*sin(theta))*cos(zeta)-(y*cos(phi)-x*sin(theta)*sin(phi)-z*cos(theta)*sin(phi))*sin(zeta)
        Fy=(x*cos(theta)-z*sin(theta))*sin(zeta)+cos(zeta)*(y*cos(phi)-x*sin(theta)*sin(phi)-z*cos(theta)*sin(phi))
        Fz=y*sin(phi)+x*sin(theta)*cos(phi)+z*cos(phi)*cos(theta)
        return [Fx, Fy, Fz]
    def tesselation_shader(self, res, t):
        dim = self.dim
        coord=[[] for _ in range(res)]
        for i in range(res):
            for j in range(res):
                x=i*dim/res - (res-i)*dim/res
                y=j*dim/res - (res-j)*dim/res
                coord[i].append((x, y, 0))#20*sin(self.a*x + self.b*y + self.c*t)))
        return coord
    
    def normals(self, res, dim, t, sx, sy):
        normals = [[] for _ in range(res)]
        for i in range(res):
            for j in range(res):
                x=i*dim/res - (1-i)*dim/res
                y=j*dim/res - (1-j)*dim/res
                l=sqrt((self.a**2 + self.b**2)*cos(self.a*x + self.b*y + self.c*t)**2 + 1)
                normals[i].append(self.CamRot([0, 0, 1], sx, sy))#self.CamRot((-self.b*cos(self.a*x + self.b*y + self.c*t)/l, self.a*cos(self.a*x + self.b*y + self.c*t)/l, 1/l), sx, sy))
        return normals
    def scalaire(self, v, u): return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
        
    def triangularisation(self, c, clr, t, sx, sy):
        n=len(c[0])
        f=self.draw
        norm = self.normals(self.res, self.dim, t, sx, sy)
        if not clr: clr=[[1 for _ in c[i]] for i in range(len(c))]
        for i in range(n-1):
            for j in range(n-1):
                #calcul lumiere
                light = [500, 0, 0]

                lum = max(0, self.scalaire(norm[i][j], Normalize(light)))
                L = Normalize(diffVect(light, c[i][j]))
                C = Normalize(diffVect([0, 0, -1300],c[i][j]))
                H = Normalize(addVect(L, C))
                specular = (max(0,self.scalaire(H, norm[i][j])))**100

                #projection
                f([[self.proj(c[i][j]), self.proj(c[i][j+1]), self.proj(c[i+1][j+1])], (120*lum*(1-specular) + specular*255, specular*255, 255*lum*(1-specular) + specular*255)])
                f([[self.proj(c[i][j]), self.proj(c[i+1][j]), self.proj(c[i+1][j+1])], (120*lum*(1-specular) + specular*255, specular*255, 255*lum*(1-specular) + specular*255)])
                
                #print([self.proj(c[i][j]), self.proj(c[i][j+1]), self.proj(c[i+1][j+1])])
    
    def rendering(self, sx, sy, t):
        new_coord = self.tesselation_shader(self.res, t) #[ [self.proj(self.tesselation_shader(self.res)[i][j]) for j in range(len(self.tesselation_shader(self.res)[i]))] for i in range(len(self.tesselation_shader(self.res)))]
        rot_coord = [ [diffVect(self.CamRot(j, sx, sy), self.center) for j in new_coord[i]] for i in range(len(new_coord))]
        self.triangularisation(rot_coord, self.vertex_color, t, sx, sy)

def diffVect(u, v):
    return [u[0]-v[0], u[1]-v[1], u[2]-v[2]]
def addVect(u, v):
    return [u[0]+v[0], u[1]+v[1], u[2]+v[2]]
def Normalize(u):
    r = sqrt(u[0]**2 + u[1]**2 + u[2]**2)
    return [u[0]/r, u[1]/r, u[2]/r]
        
