from pydub import AudioSegment

audio = AudioSegment.from_wav("wav1.wav")

# Basic Manipulation

audio = audio + 4 
audio = audio * 3
audio = audio.fade_in(10000)

audio.export("mashup.mp3", format = "mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")
