import tkinter as tk
import subprocess
import speech_recognition as sr
import pyttsx3

MAX_ATTEMPTS = 3  # Maximum number of login attempts

def openLoginScreen():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x200")
    
    password_label = tk.Label(login_window, text="Enter Password:")
    password_label.pack()
    
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()
    
    attempts = 0  # Variable to track the number of login attempts
    
    def login():
        nonlocal attempts  # Use the attempts variable defined in the outer scope
        password = password_entry.get()
        if password == "101":
            speak("Your password is correct. Welcome Sir!")
            login_window.destroy()
            run_script()
        else:
            attempts += 1
            if attempts == MAX_ATTEMPTS - 1:
                speak("Your password is incorrect. This is your last attempt.")
            elif attempts == MAX_ATTEMPTS:
                speak("Your password is incorrect. Login failed.")
                login_window.destroy()
            else:
                speak("Your password is incorrect. Please try again.")
    
    def listen_password():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for password...")
            audio = r.listen(source)
        
        try:
            password = r.recognize_google(audio)
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
            login()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error: {e}")
    
    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack()
    
    speak_button = tk.Button(login_window, text="Speak Password", command=listen_password)
    speak_button.pack()
    login_window.after(500, speak_prompt)

def speak_prompt():
    speak("Please enter the password.")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def run_script():
    # Execute your python script
    subprocess.call(['python', 'hence.py'])

# Create the main window
root = tk.Tk()
root.title("Welcome")

# Set the background image
bg_image = tk.PhotoImage(file="Megan real.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Make the background image full screen
root.geometry('{}x{}'.format(bg_image.width(), bg_image.height()))

# Create the "Let's Begin" button
button = tk.Button(root, text="Let's Begin", command=openLoginScreen, bg="blue", fg="white", font=("Helvetica", 20))
button.pack()

root.mainloop()
