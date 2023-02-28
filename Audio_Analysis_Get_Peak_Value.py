#20230228 Keith Yang
#v1: This function use to get audio data's peak value(dBFS)
#     support file format: .wav, 16bit 

from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np



wav_fname = "D:\\python_signal_processing\\python_signal_processing\\440Hz.wav"
samplerate,data = wavfile.read(wav_fname)
print(samplerate)
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")
print(type(data[0][0]))
if isinstance(data[0][0],np.int16):
    print("audio quantify bit = 16bit")
    data = data/(2**16)
print(f"L ch audio peak value = {20*np.log10(max(data[:,0]))} dBFS")
print(f"R ch audio peak value = {20*np.log10(max(data[:,1]))} dBFS")
time = np.linspace(0.,length,data.shape[0])
plt.plot(time,data[:,0],label = "Left channel")
plt.plot(time, data[:,1],label = "Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()



