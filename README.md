Speech-to-Text Conversational AI
This project is a speech-to-text conversational AI that uses speech recognition, text-to-speech, and the LangChain Ollama conversational model to interact with users in real time. The system listens to user input, processes it, and responds with spoken text. It allows for natural conversations by continuously updating the conversation context.

Features
Real-time speech recognition using speech_recognition library.
Text-to-speech output using pyttsx3.
Conversational AI powered by the LangChain OllamaLLM model.
Customizable voice settings and speech rate.
Continuous conversation context tracking.
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/speech-to-text-conversational-ai.git
Navigate to the project directory:

bash
Copy code
cd speech-to-text-conversational-ai
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Requirements
Python 3.x
Libraries (included in requirements.txt):
speech_recognition
pyttsx3
langchain_ollama
langchain_core
Usage
To run the project, simply execute the main Python script:

bash
Copy code
python main.py
The AI will listen for your input, respond using the LangChain Ollama model, and speak the response back to you.

Voice Commands
Say "exit" or "stop" to terminate the conversation.
After each response, the AI will say "listening" and wait for further input.
