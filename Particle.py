# Particle
# A particle is a thing that has a position and x/y velocity
# Radius and color are altered based on volume of input


class Particle:

    MIN_INITIAL_X_VELOCITY = -10
    MAX_INITIAL_X_VELOCITY = 10
    MIN_INITIAL_Y_VELOCITY = -5
    MAX_INITIAL_Y_VELOCITY = 5
    AMPLITUDE_MULTIPLIER = 10000
    
    def __init__(self, x, y, amplitude):
        self.x = random(width)
        self.y = random(height)
        self.xVelocity = random(Particle.MIN_INITIAL_X_VELOCITY, Particle.MAX_INITIAL_X_VELOCITY)
        self.yVelocity = random(Particle.MAX_INITIAL_Y_VELOCITY, Particle.MIN_INITIAL_Y_VELOCITY)
        self.shadeRed = color(255, random(0, 100), random(0, 100), 50)
        self.shadeGreen = color(random(0, 100), 255, random(0, 100), 50)
        self.shadeBlue = color(random(0, 100), random(0, 100), 255, 50)
        self.shadeYellow = color(255, 255, random(100), 50)
        self.shadePurple = color(random(100, 200), random(0, 100), 255, 50)
        self.shadeOrange = color(255, random(100, 200), random(0, 100), 50)
        self.amplitude = amplitude
    
    def draw(self):
        global AMPLITUDE_MULTIPLIER
        if self.amplitude.analyze() * Particle.AMPLITUDE_MULTIPLIER > 250:
            fill(self.shadeGreen)
        elif self.amplitude.analyze() * Particle.AMPLITUDE_MULTIPLIER > 200:
            fill(self.shadeBlue)
        elif self.amplitude.analyze() * Particle.AMPLITUDE_MULTIPLIER > 150:
            fill(self.shadePurple)
        elif self.amplitude.analyze() * Particle.AMPLITUDE_MULTIPLIER > 100:
            fill(self.shadeRed)
        elif self.amplitude.analyze() * Particle.AMPLITUDE_MULTIPLIER > 50:
            fill(self.shadeOrange)
        elif self.amplitude.analyze() * Particle.AMPLITUDE_MULTIPLIER > 0:
            fill(self.shadeYellow)
        rect(self.x, self.y, self.amplitude.analyze() * Particle.AMPLITUDE_MULTIPLIER, self.amplitude.analyze() * Particle.AMPLITUDE_MULTIPLIER)

    def move(self):
        self.x += cos(self.xVelocity ** 8)
        self.y -= self.yVelocity

    def offScreen(self):
        return self.x < 0 or self.y > 0
    