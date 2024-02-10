import Graphics as grph
from math import sqrt


def scalaire(v, u): return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
def vecAB(A, B):
    return [B[0]-A[0], B[1]-A[1], B[2]-A[2]]
def diffVect(u, v):
    return [u[0]-v[0], u[1]-v[1], u[2]-v[2]]
def addVect(u, v):
    return [u[0]+v[0], u[1]+v[1], u[2]+v[2]]
def multiVect(u, x):
    return [u[0]*x, u[1]*x, u[2]*x]
def linearInterpolation( a, b, t):
    return addVect(multiVect(a,(1-t)) ,multiVect(b,t))
def Normalize(u):
    r = sqrt(u[0]**2 + u[1]**2 + u[2]**2)
    if not r: return u
    return [u[0]/r, u[1]/r, u[2]/r]




class illuminationPipeline:
    def __init__(self, normals, cameraPosition, vertex_position, lightPosition, vertex_color) -> None:
        self.normals = normals
        self.cameraPosition = cameraPosition
        self.visibilite = []
        self.vertex_position = vertex_position
        self.spec = []
        self.lightPosition = lightPosition
        self.vertNumber = len(vertex_position[0])
        self.vertex_color = vertex_color

    #checks if vertix is visible (dot product)
    def isVisible(self):
        self.visibilite = [[max(0,scalaire(Normalize(vecAB(self.vertex_position[i][j], self.cameraPosition)), Normalize(self.normals[i*self.vertNumber + j]))) for j in range(self.vertNumber)] for i in range(self.vertNumber)]

    # spec = (C + L).N
    def specularity(self):
        self.spec = [[max(0,(scalaire(Normalize(addVect(vecAB(self.vertex_position[i][j], self.cameraPosition),vecAB(self.vertex_position[i][j], self.lightPosition))), Normalize(self.normals[i*self.vertNumber + j])))**100) for i in range(self.vertNumber)] for j in range(self.vertNumber)]

    def fragShader(self):
        a = [linearInterpolation(multiVect(self.vertex_color[i][j], self.visibilite[i][j]), [255]*3, self.spec[i][j]) for j in range(self.vertNumber-1) for i in range(self.vertNumber-1)]
        a.extend([linearInterpolation(multiVect(self.vertex_color[i+1][j+1], self.visibilite[i+1][j+1]), [255]*3, self.spec[i+1][j+1]) for j in range(self.vertNumber-1) for i in range(self.vertNumber-1)])
        self.vertex_color = a

    def rendering(self):
        self.isVisible()
        self.specularity()
        self.fragShader()