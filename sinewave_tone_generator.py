# 20230224
#v1:use to generate sinewave 16bit only

import numpy;
import wave;
import struct
gain_dB = 0    # dB
gain_scale = 10**((gain_dB) /20)  # full scale
fs = 44100  # samperate
fre = 440  #sinewave frequency
phi = 0   # initial phase
T = 20    # time second
Tp = T*fs   #total point
#Ts = []
#data = []
#Ts = numpy.linspace(0,T,Tp) #sample index
Ts = numpy.arange(0,T,1/fs)


data = gain_scale*numpy.sin(2*numpy.pi*fre*Ts+phi)

file = wave.open('sine.wav',"wb")
file.setnchannels(1)
file.setsampwidth(2)
file.setframerate(fs)
#file.setnframes(len(Ts))
for s in data:
    file.writeframes(struct.pack('h',int(s*2**15)))

file.close()










