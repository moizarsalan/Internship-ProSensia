# Used for text to speech and voices for AI assistant
import pyttsx3
# Used for speech recognition
import speech_recognition as sr
# Used to open google and other websites in default browser
import webbrowser
# Used for date and time
from datetime import datetime                     
# Pywhatkit will be used in playing videos on youtube        
import pywhatkit                                                                                     
                                                                                                      

# This function is used for text-to-speech.                                                         
def speak(text):                                                                                     
    engine = pyttsx3.init()                                                                          
    # Set the voice for the assistant                                                               
    voice_id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0' 
    engine.setProperty('voice', voice_id)                                                            
    print("")  
    print("-------")                                                                                      
    print(f"--> AI: {text}")  
    print("-------")                                                               
    print("")                                                                                        
    engine.say(text=text)                                                                            
    engine.runAndWait()                                                                              
                                                                                                     

# This function is for speech recognition. It recognizes user input.
def speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("--------------")
        print("Listening.....")
        print("--------------")
        # Adjust for ambient noise and listen to user input
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=8)
    try:
        print("---------------")
        print("Recognizing....")
        print("---------------")
        # Use Google Speech Recognition to convert audio to text
        query = recognizer.recognize_google(audio, language="en")
        print("--------")
        print(f"--> User: {query}")
        print("--------")
        return query.lower()
    except sr.UnknownValueError:
        # Handle when the speech recognition could not understand the audio
        return ""
    except sr.RequestError as e:
        # Handle when there is an issue with the Google Speech Recognition service
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

        

#The functions below will help in openning following tabs      
# 1- Google                                                    
# 2- Youtube                                                   
# 3- Facebook                                                  
# 4- Instagram                                                 
# 5- Github                                                    


# Open Google in a web browser
def open_google():
    webbrowser.open("https://www.google.com")

# Open YouTube in a web browser
def open_youtube():
    webbrowser.open("https://www.youtube.com")

# Open Facebook in a web browser
def open_facebook():
    webbrowser.open("https://www.facebook.com")

# Open Instagram in a web browser
def open_instagram():
    webbrowser.open("https://www.instagram.com")

# Open GitHub in a web browser
def open_github():
    webbrowser.open("https://www.github.com")


# The mainfunction takes a query as input, converts it to lowercase for case-insensitive comparison, and then 
# performs various actions based on the content of the query. 
# The execution will take place by speaking following keywords in sentence              
# Keywords: hello, time, date, google, youtube, facebook, github, instagram, play                                    

def main_execution(query):
    query = str(query).lower()

    if "hello" in query:
        speak("Hi, How may I help you?!")

    elif "time" in query:
        time_now = datetime.now().strftime("%H:%M")
        speak(f"The time now is: {time_now}")

    elif "date" in query:
        date_today = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is: {date_today}")

    elif "google" in query:
        open_google()
        speak("Opening Google.")
    # open's youtube
    elif "youtube" in query:
        open_youtube()
        speak("Opening YouTube.")

    elif "facebook" in query:
        open_facebook()
        speak("Opening Facebook.")

    elif "instagram" in query:
        open_instagram()
        speak("Opening Instagram.")

    elif "github" in query:
        open_github()
        speak("Opening GitHub.")
    # plays user searched video on youtube
    elif "play" in query:
        search = query.replace("play on youtube", "")
        pywhatkit.playonyt(search)     
    
    
    elif "stop" in query:
        speak("bye! Have a good day.")
        exit()


# Main loop for continuous listening and execution 
# It will exit once the user will say stop        


while True:
    print("")
    user_query = speech_recognition()
    main_execution(user_query)