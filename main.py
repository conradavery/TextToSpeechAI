import speech_recognition as sr
import pyttsx3
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below in plain conversation text, do not inlcude emojis.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""
context = ""

model = OllamaLLM(model="gemma2:2b")

prompt = ChatPromptTemplate.from_template(template)
chain= prompt| model

def text_to_speech(result):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can change [0] to [1] for a different voice
    engine.say(result)  # Say the result
    engine.runAndWait()
    engine.say("listening")
    engine.runAndWait()
    listen()
    

def handle_conversation(user_input):
    global context
    result= chain.invoke({"context": context, "question": user_input})
    context += f"\nUser: {user_input}\nAI: {result}"
    text_to_speech(result)
    
    #listen()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Transmitting...")
        user_input = r.recognize_google(audio)
        if user_input.lower() == "exit" or user_input.lower() == "stop":
            print("Stopping")
        else:
            handle_conversation(user_input)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__=="__main__":
    listen()


