# Audio formats
# .mp3 - compressed but has losses
# .flac - compressed but loseless
# .wav - uncompressed, best audio quality

import wave

#Audio signal parameters

# - number of channels
# - sample width
# - sample rate( no of samples each second)
# - number of frames
# - values of a frame

obj = wave.open("wav1.wav","rb")

print("No of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("No of frames", obj.getnframes())
print("Parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1) #reads all frames
print(type(frames),type(frames[0]))
print(len(frames)/2)

obj_new = wave.open("wav2.wav","wb")
obj_new.setnchannels(3)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)
obj_new.close()
