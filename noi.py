from gtts import gTTS
import playsound
import os

# text = "tôi có thể giúp gì cho bạn" 
def noi(text):   
    print("AI: " + text)
    output = gTTS(text,lang="vi", slow=False)
    file1 = str("noi" + str(0) + ".mp3")
    output.save(file1)
    playsound.playsound(file1, True)
    os.remove(file1)
