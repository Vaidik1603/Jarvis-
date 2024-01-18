import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    #global instruction
    try:
        with aa.Microphone() as origin:
            print("Listening.....")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis',"")
                print(instruction)
        return(instruction)
    
    except aa.UnknownValueError:
        pass
    
    except aa.RequestError:
        print("Couldn't request!. Check your Internet Connection !!!!!!!")
    return ""

def play_Jarvis():
    instruction = input_instruction()
    print(instruction)
    
    if "play" in instruction:
        song = instruction.replace('play',"")
        talk("Playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current Time is ' + time)

    elif "date" in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's Date is " + date)
    elif "how are you" in instruction:
        talk("I am Good. How about you?")
    
    elif "What is your name?" in instruction:
        talk("My name is Jarvis, What can I do for you?")
    
    elif "who is" in instruction:
        person = instruction.replace('who is',"")
        info = wikipedia.summary(person,1)
        print(info)
        talk(info) 
    else:
        talk("Pardon!!")

play_Jarvis()
