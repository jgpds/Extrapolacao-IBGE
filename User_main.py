import os
from tkinter import * #interface gráfica
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser

# --------------------------- INTERFACE GERAL ---------------------------#
VERDE_ESCURO = '#45da9c'
VERDE_CLARO = "#5EF9B8"
BACKGROUND = VERDE_ESCURO



root = Tk()
#root.state('zoomed')

# Ícone da barra
#root.iconbitmap('favicon.ico')

# Título
root.title("EXTRAPOLADOR DE TÁBUAS")
root.resizable(0,0) # remove o botão de maximizar e minimizar
# Dimensão e cor do background
root.geometry("800x600")  
root.config(bg='#fafafa')

label_verde = Label(root, bg=BACKGROUND, height=600, width=50)
label_verde.place(x=0, y=0)

label_texto = Label(root, bg=BACKGROUND, height=2, width=20, text="Extrapolação de Tábuas", font=("Arial", 18), fg='white')
label_texto
label_texto.place(x=0, y=0)


import_img = Image.open('./UI imgs/Screenshot_1.png')
import_img_resized = import_img.resize((100, 37), Image.ANTIALIAS) #resize (width, height)
import_img = ImageTk.PhotoImage(import_img_resized)

gitimg = Image.open('./UI imgs/gitimg.png')
gitimg_resized = gitimg.resize((30, 30), Image.ANTIALIAS) #resize (width, height)
gitimg = ImageTk.PhotoImage(gitimg_resized)


def callback(url):
    webbrowser.open_new(url)


link_label = Label(root, text= "github.com/jgpds", bg=BACKGROUND, fg='white', cursor='hand2', font=('Arial', 13, 'italic', UNDERLINE))
link_label.place(x = 50, y = 553)
link_label.bind("<Button-1>", lambda e: callback("https://github.com/jgpds/"))

def openFile():
    filepath = filedialog.askopenfilename()
    relfilepath = os.path.relpath(filepath)
    outputName.config(state='normal')
    outputName.insert(0, filepath)
    outputName.config(state='disabled')
    print(filepath)

label_button = Label(root, image=import_img, highlightthickness=0, borderwidth=0, cursor='hand2', activebackground="LightSteelBlue2")
label_button.place(x=410, y=230)
label_button.bind("<Button-1>", lambda e: openFile())

label_git = Label(root, image=gitimg, bg=BACKGROUND)
label_git.place(x=10, y=550)

outputName = Entry(width=35, state='disabled')
outputName.place(x=420, y=280)



root.mainloop()

