from math import sin, cos, sqrt, floor
class graphics_pipeline :
    def __init__(self, vertex_color, proj, dimx, dimy, draw, t, res, center, disc, grad):
        self.vertex_position = []
        self.vertex_color = vertex_color
        self.proj = proj
        self.dimx = dimx
        self.dimy = dimy
        self.draw = draw
        self.t = t
        self.res = res
        self.center = center
        self.disc = disc
        self.triangles = []
        self.normales = []
        self.grad = grad

    #subdivide plane and disceplace vertices
    def vertexShader(self):
        dimx = self.dimx
        dimy = self.dimy
        res = self.res
        coord=[[] for _ in range(res)]
        for i in range(res):
            for j in range(res):
                x=i*dimx/res - (res-i)*dimx/res
                y=j*dimy/res - (res-j)*dimy/res
                coord[i].append(self.disc(x, y))
        self.vertex_position = coord
    
    #calculate normals
    def normals(self):
        dimx = self.dimx
        dimy = self.dimy
        res = self.res
        for i in range(res):
            for j in range(res):
                x=i*dimx/res - (res-i)*dimx/res
                y=j*dimy/res - (res-j)*dimy/res
                g = self.grad(x, y)
                B = [0, 1, g[2]]
                T = [1, 0, g[0]]
                self.normales.append(Normalize(cross(T, B)))

    #color
    def fragShader(self):
        self.vertex_color = [[[120, 0, 255] for _ in range(len(self.vertex_position[0]))] for _ in range(len(self.vertex_position))]

    #generate triangles
    def triangularisation(self):
        c = self.vertex_position
        self.triangles = [[self.proj(c[i][j]), self.proj(c[i][j+1]), self.proj(c[i+1][j+1])] for j in range(len(c[0])-1) for i in range(len(c[0])-1)]
        self.triangles.extend([[self.proj(c[i+1][j+1]), self.proj(c[i][j]), self.proj(c[i+1][j])] for j in range(len(c[0])-1) for i in range(len(c[0])-1)])

    #combine function to render
    def rendering(self):
        self.normals()
        self.vertexShader()
        self.fragShader()
        self.triangularisation()

def scalaire(v, u): return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]


def diffVect(u, v):
    return [u[0]-v[0], u[1]-v[1], u[2]-v[2]]
def addVect(u, v):
    return [u[0]+v[0], u[1]+v[1], u[2]+v[2]]


def Normalize(u):
    r = sqrt(u[0]**2 + u[1]**2 + u[2]**2)
    if not r: return u
    return [u[0]/r, u[1]/r, u[2]/r]
