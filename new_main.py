from tkinter import *
from tkinter import messagebox, ttk
import googletrans
from googletrans import Translator

def labelChange():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000, labelChange)

def translateNow():
    global language
    try:
        text_ = text1.get(1.0, END).strip()  # Get the text and strip whitespace
        c2 = combo1.get()  # Source language
        c3 = combo2.get()  # Target language

        if text_:
            translator = Translator()

            # Get source language code from combo1
            src_lang_code = None
            for code, lang_name in language.items():
                if lang_name.lower() == c2.lower():
                    src_lang_code = code
                    break

            # Get target language code from combo2
            target_lang_code = None
            for code, lang_name in language.items():
                if lang_name.lower() == c3.lower():
                    target_lang_code = code
                    break

            if src_lang_code and target_lang_code:
                # Perform the translation using googletrans
                translated = translator.translate(text_, src=src_lang_code, dest=target_lang_code)
                text2.delete(1.0, END)  # Clear the output text field
                text2.insert(END, translated.text)  # Insert the translated text
            else:
                messagebox.showerror("Language Error", "Unable to detect source or target language.")
        else:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

root = Tk()
root.title("Leefo Translator")
root.geometry("1080x400")

root.iconbitmap("google.ico")

arrow = PhotoImage(file="arrow_image.png")
image_label = Label(root, image=arrow, width=80, height=60)
image_label.place(x=510, y=80)

language = googletrans.LANGUAGES
languageV = list(language.values())

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("english")

label1 = Label(root, text="ENGLISH", font="segoe 20 bold", fg="black", bg="white", width=25, border=2, relief=GROOVE)
label1.place(x=100, y=80)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=50, y=118, width=440, height=210)

text1 = Text(f1, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("spanish")

label2 = Label(root, text="SPANISH", font="segoe 20 bold", fg="black", bg="white", width=25, border=2, relief=GROOVE)
label2.place(x=680, y=80)

f2 = Frame(root, bg="black", bd=5)
f2.place(x=630, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

labelChange()

button = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="grey", fg="black", command=translateNow)
button.place(x=500, y=250)

root.configure(bg="white")
root.mainloop()
