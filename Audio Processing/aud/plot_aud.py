import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("wav1.wav","rb")

sample_frequency = obj.getframerate()
n_samples = obj.getnframes() # returns number of audio frames
signal_wave = obj.readframes(-1) # reads and returns all frames(-1) as bytes object

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

obj.close()

signal_array = np.frombuffer(signal_wave, dtype = np.int16)

times = np.linspace(0, t_audio, num = n_samples)

plt.figure(figsize = (15,5))
plt.plot(times,signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)
plt.show()


