import pyttsx3

engine = pyttsx3.init()

text = "Type your text here"
n = int(input("How many times do you want to repeat the text:"))


engine.setProperty('rate', 120)
for n in range(n):
    engine.say(text)

engine.runAndWait()

