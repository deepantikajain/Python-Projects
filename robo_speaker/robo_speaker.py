import pyttsx3

print("🤖 ROBO SPEAKER (Type 'exit' to stop)")

engine = pyttsx3.init()

while True:
    text = input("Enter what you want me to speak: ")
    
    if text.lower() == "exit":
        print("👋 Robo Speaker stopped!")
        break
    
    engine.say(text)
    engine.runAndWait()
