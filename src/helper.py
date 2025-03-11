import speech_recognition as sr
import google.generativeai as genai 
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 
from gtts import gTTS

print("perfect!!")
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = groq_api_key


def voice_input():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
        
        
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")
    
    
def llm_model_object(user_text):
    #model = "models/gemini-pro"
    
    
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key = groq_api_key
    )
    
    response = model.invoke(user_text)
    
    result = response.content
    
    return result