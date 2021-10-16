import speech_recognition as sr

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except :  # For Error handling
        print("Network connection error")
        return "none"
    return text

while 1:  # Do this forever
    var= int(input())  # get input from user

    if(var == 1):
        print("LED turned ON")
    elif(var== 0):
        print("LED turned OFF")
    else:
        print("Type 1 to turn on LED and 0 to turn OFF LED")





