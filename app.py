from flask import Flask, render_template, request, redirect
from tkinter import *
import speech_recognition as sr
from tkinter.ttk import Combobox
from googletrans import Translator, LANGUAGES
 
app = Flask(__name__)
 

def Translate(type, text):
    root = Tk()
    root.geometry('1100x320')
    root.resizable(0, 0)
    root.iconbitmap('etc .ico')
    root['bg'] = 'red'

    root.title('Language translator')
    Label(root, text="Language Translator", font="Arial 20 bold").pack()
    Label(root, text="Enter Text", font='arial 13 bold',
          bg='white smoke').place(x=165, y=90)
    Input_text = Entry(root, width=60)
    Input_text = text
    Input_text.place(x=35, y=135)
    Input_text.get()
    Label(root, text="Output", font='arial 13 bold ',
          bg='white smoke').place(x=820, y=90)
    Output_text = Text(root, font='arial 10', height=5,
                       wrap=WORD, padx=5, pady=5, width=50)
    Output_text.place(x=670, y=130)

    language = type
    language = list(LANGUAGES.values())
    dest_lang = Combobox(root, values=language, width=25)
    dest_lang.place(x=130, y=180)
    dest_lang.set("Choose the Language")



# voice translator
@app.route('/voice-translation', methods=['POST'])
def voice_translation():
    if request.method == 'POST':
        input_text = recognize_speech()
        target_lang = request.form['lang']

        translator = Translator()
        translated = translator.translate(text=input_text, dest=target_lang)

        return render_template('index.html', input_text=input_text, translated=translated.text)

    return render_template('index.html', input_text='', translated='')

def recognize_speech():
    recog= sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Say  some blaa blaaa")
        audio = recog.listen(source)

    try:
        text = recog.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "audio is not understood"
    except sr.RequestError as e:
        return f"Could not request results  ; {e}"




def translate(type, text):
    translator = Translator()
    translated = translator.translate(text=text, dest=type)
    return translated
@app.route('/', methods=['POST', 'GET'])
def translate():
    if request.method == 'POST':
        input_text = request.form['data']
        target_lang = request.form['lang']

        if 'voice' in request.form:
            input_text = recognize_speech()
       # print(type1, text)
        translator = Translator()
        translated = translator.translate(input_text, dest=target_lang)

        return render_template('index.html', input_text=input_text, translated=translated.text)

    return render_template('index.html', input_text='', translated='')


if __name__ == '__main__':
    app.run(debug=True)
