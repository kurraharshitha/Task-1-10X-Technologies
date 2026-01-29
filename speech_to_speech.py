import whisper
import pyttsx3

print("Loading speech-to-text model...")
model = whisper.load_model("base")

print("Transcribing audio...")
result = model.transcribe("input.wav")

text = result["text"]
print("You said:", text)

print("Speaking response...")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()