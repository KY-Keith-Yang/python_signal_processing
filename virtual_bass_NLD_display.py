#20230308 keith
#display tow NLD type, refer paper: Reproducing Low-Pitched Signals through Small Loudspeakers

from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np



wav_fname = "D:\\python_signal_processing\\python_signal_processing\\10Hz.wav"
samplerate,data = wavfile.read(wav_fname)
print(samplerate)
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")
print(type(data[0][0]))
if isinstance(data[0][0],np.int16):
    print("audio quantify bit = 16bit")
    data = data/(2**15)
    print(max(data[:,0]))
print(f"L ch audio peak value = {20*np.log10(max(data[:,0]))} dBFS")
print(f"R ch audio peak value = {20*np.log10(max(data[:,1]))} dBFS")
time = np.linspace(0.,length,data.shape[0])
yn_1 = 0
un_1 = 0
yn = np.zeros(882)
un = np.abs(data[:,0])
for i in range(data.shape[0]):
#for i in range(100):
    if (un_1 <= 0) and (un[i] > 0) :
        yn[i] = 0
        print(yn[i])
    else:
        yn[i] = un_1+yn_1

    un_1 = un[i]
    yn_1 = yn[i]
   # print(i)



plt.plot(time,yn/max(yn),"--",label = "full wave integrator")
plt.plot(time,data[:,0],"-.",label = "input")
plt.plot(time,np.abs(data[:,0]),label = "full wave rectification")
#plt.plot(time,np.abs(data[:,0]),label = "full wave")
#plt.plot(time, data[:,1],label = "Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()