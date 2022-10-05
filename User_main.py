from cProfile import label
import os
from tkinter import * #interface gráfica
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser
from Extrapolar import calcular
import pandas as pd

# --------------------------- INTERFACE GERAL ---------------------------#
VERDE_ESCURO = '#45da9c'
VERDE_CLARO = "#5EF9B8"
BACKGROUND = VERDE_ESCURO
answer = False


root = Tk()
#root.state('zoomed')

# Ícone da barra
#root.iconbitmap('favicon.ico')

# Título
root.title("EXTRAPOLADOR DE TÁBUAS")
root.resizable(0,0) # remove o botão de maximizar e minimizar
root.iconbitmap('./UI imgs/favicon.ico')
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

calcular_img = Image.open("./UI imgs/Screenshot_5.png")
calcular_img_resized = calcular_img.resize((100,37), Image.ANTIALIAS)
calcular_img = ImageTk.PhotoImage(calcular_img_resized)

gitimg = Image.open('./UI imgs/gitimg.png')
gitimg_resized = gitimg.resize((30, 30), Image.ANTIALIAS) #resize (width, height)
gitimg = ImageTk.PhotoImage(gitimg_resized)


def callback(url):
    webbrowser.open_new(url)





link_label = Label(root, text= "github.com/jgpds", bg=BACKGROUND, fg='white', cursor='hand2', font=('Arial', 13, 'italic', UNDERLINE))
link_label.place(x = 50, y = 553)
link_label.bind("<Button-1>", lambda e: callback("https://github.com/jgpds/"))

def is_original_data_ok(data_original):
    if len(data_original.columns.values.tolist()) == 2 and 'q_x' in data_original.columns.values.tolist() and 'e_x' in data_original.columns.values.tolist():
        return 'Ok'
    else:
        return 'Not Ok'


def openFile():
    label_warning.place_forget()
    global filepath
    filepath = filedialog.askopenfilename()
    print(filepath)
    outputName.config(state='normal')
    outputName.insert(0, filepath)
    outputName.config(state='disabled')
    filepath = os.path.abspath(filepath)
    global data_original
    try:
        data_original = pd.read_excel(filepath)
    except ImportError:
        label_warning.place(x=420, y=450)
    global status_original_data
    print(f"data original -> : {data_original}")
    status_original_data = is_original_data_ok(data_original)
    print(filepath)
    entry_fa.place(x=420, y=310)
    label_fa.place(x=400, y=310)
    entry_w.place(x=420, y=340)
    label_w.place(x=400, y=340)
    entry_f_x.place(x=420, y=370)
    label_f_x.place(x=400, y=370)
    label_button2.place(x=420, y=400)

def answerYes():
    if status_original_data == 'Ok':
        label_warning.place_forget()
        calcular(data_original=data_original, fa=100, w=115, f_x=0.5)
    else:
        label_warning.place(x=420, y=450)
        print('Not ok')



label_button = Label(root, image=import_img, highlightthickness=0, borderwidth=0, cursor='hand2', activebackground="LightSteelBlue2")
label_button.place(x=410, y=230)
label_button.bind("<Button-1>", lambda e: openFile())

label_button2 = Label(root, image=calcular_img, highlightthickness=0, borderwidth=0, cursor='hand2', activebackground="LightSteelBlue2")

label_button2.bind("<Button-1>", lambda e: answerYes())

label_warning = Label(root, text="A planilha escolhida não é válida.".upper(), fg='red', background='white', font= ('Ubuntu', 9))


entry_fa = Entry(width=35, fg = 'black', bg="#f0f0f0")
entry_fa.insert(0, "100")
entry_w = Entry(width=35, fg='black', bg="#f0f0f0")
entry_f_x = Entry(width=35, fg='black', bg="#f0f0f0")
entry_f_x.insert(0, "0.5")

label_fa = Label(text='FA', fg = 'black', bg='white')
label_w = Label(text='ω', fg='black', bg='white', font=("Arial", 11))
label_f_x = Label(text='f_x', bg='white')



label_git = Label(root, image=gitimg, bg=BACKGROUND)
label_git.place(x=10, y=550)

outputName = Entry(width=35, state='disabled')
outputName.place(x=420, y=280)



root.mainloop()

