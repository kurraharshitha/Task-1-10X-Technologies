import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000  # Whisper prefers 16kHz
seconds = 5

print("Recording... Speak now")

audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("input.wav", fs, audio)
print("Audio saved as input.wav")