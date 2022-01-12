import random
import math

class V:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        return V(self.x+other.x,self.y+other.y,self.z+other.z)
    def __neg__(self):
        return V(-self.x,-self.y,-self.z)
    def __sub__(self,other):
        return V(self.x-other.x,self.y-other.y,self.z-other.z)
    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+", "+str(self.z)+">"
    def __mul__(self,other):
        if (type(self)==type(other)):
            return self.x*other.x+self.y*other.y+self.z*other.z
        else:
            return V(self.x*other,self.y*other,self.z*other)
    def __pow__(self,other):
        return V(self.y*other.z-self.z*other.y,self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)
    def r(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    def unit(self):
        return self*(1/self.r())

class Particle:
    def __init__(self,position,velocity,mass):
        self.position=position
        self.velocity=velocity
        self.mass=mass
    def __str__(self):
        return str(self.position)+"   "+str(self.velocity)+"   "+str(self.mass)
    def appForce(self,force,dt):
        self.velocity=self.velocity+force*(dt/self.mass)
    def increment(self,dt):
        self.position=self.position+self.velocity*dt
    def combine(self,other):
        newPos = (self.position+other.position)*0.5
        newMass = self.mass+other.mass
        newVel = (self.velocity*self.mass+other.velocity*other.mass)*(1/newMass)
        self.position = newPos
        self.mass = newMass
        self.velocity = newVel
     

        
def populateParticles(n,sphereBool,maxpos,maxvel,minmass,maxmass):
    llist=[]
    if sphereBool:
        for i in range(n):
            r=random.random()*maxpos
            rphi=random.random()*math.pi
            rtheta=random.random()*2*math.pi
            v=random.random()*maxvel
            vphi=random.random()*math.pi
            vtheta=random.random()*2*math.pi
            mass=minmass+(maxmass-minmass)*random.random()
            pos=V(r*math.sin(rphi)*math.cos(rtheta),r*math.sin(rphi)*math.sin(rtheta),r*math.cos(rphi))
            vel= V(v*math.sin(vphi)*math.cos(vtheta),v*math.sin(vphi)*math.sin(vtheta),v*math.cos(vphi))
            llist.append(Particle(pos,vel,mass))
    return llist

class ParticleSystem:
    def __init__(self,particles,g,dt,dr):
        self.particles=particles
        self.G=g
        self.dt=dt
        self.dr=dr
    def printout(self):
        for i in self.particles:
            print(i)
    def increment(self):
        for i in range(len(self.particles)):
            body = self.particles[i]
            for j in range(len(self.particles)):
                body.appForce(self.force(i,j),self.dt)
        for i in range(len(self.particles)):
            body = self.particles[i]
            body.increment(self.dt)
        for i in self.particles:
            for j in self.particles:
                if i!=j:
                    if (i.position-j.position).r()<=self.dr:
                        i.combine(j)
                        self.particles.remove(j)
    def numParticles(self):
        return len(self.particles)
    def force(self,i,j): #force of jth particle on ith particle
        if i==j:
            return zero
        else:
            return -(self.particles[i].position-self.particles[j].position)*(self.G*self.particles[i].mass*self.particles[j].mass/(((self.particles[i].position-self.particles[j].position).r())**3))

system = ParticleSystem(populateParticles(2,True,10,0.3,1,10),1,0.01,0.1)
ihat = V(1,0,0)
jhat = V(0,1,0)
khat = V(0,0,1)
zero = V(0,0,0)
#system = ParticleSystem([Particle(ihat,zero,1),Particle(-ihat,zero,1)],1,0.1,1.0)
num=1
while num<30:
    print(num)
    system.printout()
    system.increment()
    num+=1