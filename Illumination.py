import Graphics as grph
from math import sqrt, ceil


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
def norm(u):
    return sqrt(u[0]**2 + u[1]**2 + u[2]**2)

def spotLightIntensity(dir, innerRadiusAngle, outerRadiusAngle, vectPosition,lightPosition, normal, intensity):
    vl =Normalize(vecAB(lightPosition, vectPosition))
    dot = scalaire(vl, Normalize(dir))
    lum = max(0, scalaire(normal, vl))*intensity
    if dot > innerRadiusAngle:
        return lum
    elif innerRadiusAngle >= dot > outerRadiusAngle:
        return lum*(dot - outerRadiusAngle)/(innerRadiusAngle - outerRadiusAngle)
    else :
        return 0
    
def pointLightIntensity(innerRadius, outerRadiusCoef, vectPosition, lightPosition, normal, intensity):
    if 1 > intensity: intensity = 1.2
    vl = vecAB(lightPosition, vectPosition)
    lum = max(0, scalaire(normal, Normalize(vl)))*intensity
    l = norm(vl)
    outerRadius = innerRadius * outerRadiusCoef
    if innerRadius > l:
        return lum
    if outerRadius > l > innerRadius:
        return lum*(l - outerRadius )/(innerRadius - outerRadius)
    else :
        return 0





class illuminationPipeline:
    def __init__(self, normals, cameraPosition, vertex_position, light, vertex_color) -> None:
        self.light = light
        self.normals = normals
        self.cameraPosition = cameraPosition
        self.visibilite = []
        self.vertex_position = vertex_position
        self.spec = []
        self.lightPosition = light.lightPosition
        self.vertNumber = len(vertex_position[0])
        self.vertex_color = vertex_color
        self.lit = []
        self.lightIntensity = light.lightIntensity
        self.innerRadiusAngle = light.innerRadiusAngle
        self.outerRadiusAngle = light.outerRadiusAngle

    #checks if vertix is visible (dot product)
    def isVisible(self):
        self.visibilite = [[ceil(scalaire(Normalize(vecAB(self.vertex_position[i][j], self.cameraPosition)), Normalize(multiVect(self.normals[i*self.vertNumber + j],-1)))) for j in range(self.vertNumber)] for i in range(self.vertNumber)]
        return 0
    
    def isLit(self):
        if self.light.lightType == 0:
            self.lit = [[max(0, scalaire(Normalize(vecAB(self.vertex_position[i][j], self.lightPosition)), Normalize(multiVect(self.normals[i*self.vertNumber + j],-1)))) for j in range(self.vertNumber)] for i in range(self.vertNumber)]
            return 0
        if self.light.lightType == 1:
            self.lit = [[spotLightIntensity(self.light.direction, self.innerRadiusAngle, self.outerRadiusAngle, self.vertex_position[i][j], self.lightPosition, self.normals[i*self.vertNumber + j], self.lightIntensity) for j in range(self.vertNumber)] for i in range(self.vertNumber)]
            return 0
        if self.light.lightType == 2:
            self.lit = [[pointLightIntensity( self.innerRadiusAngle, self.outerRadiusAngle, self.vertex_position[i][j], self.lightPosition, self.normals[i*self.vertNumber + j], self.lightIntensity) for j in range(self.vertNumber)] for i in range(self.vertNumber)]
            return 0
    
    # spec = (C + L).N
    def specularity(self):
        self.spec = [[max(0,(scalaire(Normalize(addVect(Normalize(vecAB(self.vertex_position[i][j], self.cameraPosition)),Normalize(vecAB(self.vertex_position[i][j], self.lightPosition)))), Normalize(multiVect(self.normals[i*self.vertNumber + j],-1))))**70) for i in range(self.vertNumber)] for j in range(self.vertNumber)]
        return 0
    
#linearInterpolation(multiVect(self.vertex_color[i][j], self.visibilite[i][j]), [255]*3,
    def fragShader(self):
        a = [multiVect(linearInterpolation(self.vertex_color[i][j], [255*self.visibilite[i][j]]*3, self.spec[i][j]), self.visibilite[i][j]*self.lit[i][j]) for j in range(self.vertNumber-1) for i in range(self.vertNumber-1)]
        a.extend([multiVect(linearInterpolation(self.vertex_color[i+1][j+1], [255*self.visibilite[i+1][j+1]]*3, self.spec[i+1][j+1]), self.visibilite[i+1][j+1]*self.lit[i+1][j+1]) for j in range(self.vertNumber-1) for i in range(self.vertNumber-1)])
        self.vertex_color = a
        return 0
    
    def rendering(self):
        self.isVisible()
        self.isLit()
        self.specularity()
        self.fragShader()
        return 0
