import random
import tkinter as tk
import pyperclip
from tkinter import ttk 

color = ''

app = tk.Tk()
style = ttk.Style(app)
app.geometry("400x200")
app.resizable(False, False)    
app.title("Secure Password Generator")
app.configure(background="black")
style.theme_use('default')
color = 'black'
color_bg = 'black'
color_fg = 'white'
btn_bg = '#444444'     # fundo normal do botão
btn_fg = 'orange'      # texto do botão
btn_active = '#666666' # fundo quando estiver 'hover'
btn_pressed = '#222222'

lf = ttk.LabelFrame(app, text='Password generator')
lf.pack(padx=20, pady=1)
style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.TLabelframe.Label", background=color, foreground="4CCB08#")
style.configure("Custom.TLabelframe", background=color, foreground="blue")
style.configure(
    "BW.TButton",
    background=color,      
    foreground="white",      
    borderwidth=2,           
    relief="solid",          
    focusthickness=0  
)
style.map(
    "BW.TButton",
    background=[
        ("active", color),    # hover
        ("pressed", "gray30")    # pressed
    ],
    foreground=[
        ("disabled", "gray50")
    ]
) 

lf = ttk.LabelFrame(app, text='        Password generator', style="Custom.TLabelframe")
lf.place(relx=0.5, rely=0.5, width=390, height=190,anchor=tk.CENTER)

Labe = ttk.Label(lf, text="", background=color,font=("Arial", 12), foreground="white")
Labe.pack(pady=10,fill='both')
ll = ttk.Label(lf, text="", background=color, foreground="#4CCB08", font=("Arial", 14), anchor='center', justify='center', width=30)
ll.pack(pady=10,fill='both')

botao = ttk.Button(lf, command=lambda: secure_pass(),style="BW.TButton", text="Generate Password", padding=5)
botao.place(x=50, y=100,width=120)
copiar = ttk.Button(lf, text="Copy to Clipboard",style="BW.TButton", command=lambda: copy(), padding=5)
copiar.place(x=220, y=100, bordermode='inside',width=120)


text_var = tk.StringVar()
textbox = ttk.Entry(lf, textvariable=text_var).place(x=99999,y=99999)
text_var.trace_add("write", lambda *args: ll.config(text=text_var.get()))

def secure_pass():
    digits = '0123456789'
    specials = '«»-/*+?=_@#$%&()!:;"%<>[]{}|^`~'
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abc = [
        random.choice(digits),
        random.choice(specials),
        random.choice(lowers),
        random.choice(uppers)
    ]
    l = '' 
    i = 0
    while i < random.randint(8,16) :
        l = str(l) +random.choice(abc)
        i +=1
    text_var.set(l)
    Labe.config(text="         Your Secure Password is:", background=color, foreground="white")
    all_chars = digits + specials + lowers + uppers
    while len(abc) < random.randint(8, 16):
        abc.append(random.choice(all_chars)) 
        random.shuffle(abc)
        l = ''.join(abc)
    text_var.set(l)
    return l

c = text_var.get()

def copy():
    cp = text_var.get()
    global ll
    global Labe
    if cp =='':
        ll.config(text="click on the botton generate pass\n to generate the secure password", background=color, foreground="white",font=('arial',12))
    else: 
        pyperclip.copy(cp)
        Labe.config(text="        password copy to the clipboard!", background=color, foreground="white")

app.mainloop()