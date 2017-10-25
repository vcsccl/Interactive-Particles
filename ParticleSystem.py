# ParticleSystem
# A collection of particles rise and change color

from Particle import *

class ParticleSystem:
    
    NUMBER_OF_PARTICLES = 50
    
    def __init__(self, x, y, amplitude):
        self.particles = []
        self.done = False
        self.x = x
        self.y = y
        self.amplitude = amplitude
        for _ in range(ParticleSystem.NUMBER_OF_PARTICLES):
            self.particles.append(Particle(self.x, self.y, self.amplitude))
    
    def draw(self):
        global amplitude
        for p in self.particles:
            p.draw()
    
    def update(self):
        anyParticlesStillOnScreen = False
        for p in self.particles:
            p.move()
            if not p.offScreen():
                anyParticlesStillOnScreen = True
        if not anyParticlesStillOnScreen:
            self.particles = []
            self.done = True

        
    
    
    
    