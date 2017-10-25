# Jon Palmer
# Term Project: Interactive Particle Systems
# Display and alter a particle everytime a sound is detected

from Particle import *
from ParticleSystem import *

add_library("sound")

AMPLITUDE_MULTIPLIER = 100000
AMPLITUDE_THRESHOLD = 300 
audioInput = None
amplitude = None

particleSystems = []

def setup():
    global audioInput, amplitude
    fullScreen() 
    audioInput = AudioIn(this, 0) # Bind the input to the program
    audioInput.start()            # Start listening 
    amplitude = Amplitude(this)   # Create an Amplitude monitoring object
    amplitude.input(audioInput)   # Bind the input to the amplitude monitor

def draw():
    global amplitude
    background(0)
    noStroke()
    for ps in particleSystems:
        ps.update()
        ps.draw()
    if currentAmplitude() > AMPLITUDE_THRESHOLD:
        particleSystems.append(ParticleSystem(random(width), random(height), amplitude))    

def currentAmplitude():
    return int(AMPLITUDE_MULTIPLIER * amplitude.analyze())

 