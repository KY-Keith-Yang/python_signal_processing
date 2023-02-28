# 20230224 Keith Yang
#v1:use to generate sinewave 16bit only
# 20230228 Keith Yang
#v2:1.use scipy to fenerate tone, can use all config like gain,channel,quantify bit ... 
#   2.can not set quantify bit to 24bit
from scipy.io.wavfile import write
import numpy as np;
import wave;
import struct

# generate config parameter
gain_dB = 0    # dB
fs = 44100  # samperate
fre = 440  #sinewave frequency
phi = 0   # initial phase
time = 20    # time second
ch_num = 1 # mono = 1 or stereo = 2
quantify_bit = 2 # 16bit = 1 or 32bit = 2
file_name = '440Hz.wav'   # define file name
#Tp = T*fs   #total point
#Ts = []
#data = []
#Ts = np.linspace(0,T,Tp) #sample index

def sine_tone_gen_func(gain_dB,fs,fre,phi,time,ch_num, quantify_bit):
    Ts = np.arange(0,time,1/fs)
    gain_scale = 10**((gain_dB) /20)  # full scale
    data = gain_scale*np.sin(2*np.pi*fre*Ts+phi)
    if quantify_bit == 1:
        amplitude = np.iinfo(np.int16).max
    elif quantify_bit == 2:
        amplitude = np.iinfo(np.int32).max  
    data = amplitude*data
    if ch_num == 2:
        data = np.c_[data,data]

    print(data)
    if quantify_bit == 1:
        write(file_name,fs, data.astype(np.int16))
    elif quantify_bit ==2:
        write(file_name,fs, data.astype(np.int32))

sine_tone_gen_func(gain_dB,fs,fre,phi,time,ch_num, quantify_bit)




### use python wave lib
# file = wave.open('sine.wav',"wb")
# file.setnchannels(1)
# file.setsampwidth(2)
# file.setframerate(fs)
# #file.setnframes(len(Ts))
# for s in data:
#     file.writeframes(struct.pack('h',int(s*2**15)))

# file.close()
### use python wave lib

















