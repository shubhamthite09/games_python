from gtts import gTTS
from playsound import playsound

# r = sr.Recognizer()
#
# with sr.Microphone as source:
#     print("speak anything : ")
#     audio = r.listen(source)
#
#     try:
#         text = r.recognize_google(audio)
#         print("you said : {} ".format(text))
#     except:
#         print("sorry i can't recognize your voice ")
def audio_output(str):
    audio = gTTS(str)
    output_audio = audio.save("output.mp3")
    playsound("output.mp3")
audio_output("hey, surekha what are you doing")

