import customtkinter as ctk
import pyperclip
import random
import pyperclip

f = ''

app = ctk.CTk()
app.geometry("400x250")
app.resizable(False, False)    
app.title("Secure Password Generator")

def pass_gen():
    li = 'qwertyuiopasdghjklçzxcvbnm'
    ttc = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
    fr = '!"#$%&/()=?»«}[{@£|-_:.;,/]'
    num = '1234567890'
    d = 0
    c = ''
    global f
    for i in range(random.randint(12,20)):

        c = [random.choice(li), random.choice(ttc), random.choice(fr), random.choice(num)]
        f = c[random.randint(0, 3)]


    for i in c:
        if i not in li:
            ps = random.randint(0, len(f))
            pv = str(random.choice(li))
            f = f[:ps] + pv + f[ps:]
        if i not in ttc:
            ps = random.randint(0, len(f))
            pv = str(random.choice(ttc))
            f = f[:ps] + pv + f[ps:]
        if i not in fr:
            ps = random.randint(0, len(f))
            pv = str(random.choice(fr))
            f = f[:ps] + pv + f[ps:]
        if i not in num:
            ps = random.randint(0, len(f))
            pv = str(random.choice(num))
            f = f[:ps] + pv + f[ps:]
        else:
            pass
    return l1.configure(text=f'a password segura e \n {f}',font=('robonto',26))


def copy_pass():
    if f == '':
        l1.configure(text=f'clique em gerar \n para gerar a senha segura',font=('robonto',26))
    else:
        l1.configure(text=f'a password foi copiada para \na Área de transferência',font=('robonto',26))
        return pyperclip.copy(str(f))
d = 'copiar'


l1 = ctk.CTkLabel(app,text='gerador de senhas seguras',font=('robonto',26))
l1.place_configure(y=80,x=250,anchor="center",bordermode='inside')
l1.configure(text=f,font=('robonto',26))


b1 = ctk.CTkButton(app,fg_color='#003d5c',font=('arial',20),command=pass_gen,text='gerar',anchor="center",border_width=2,border_color="#012B40",hover=True,hover_color='#014161')
b1.place_configure(width=150,height=50,x=50,y=180)

b2 = ctk.CTkButton(app,fg_color='#003d5c',font=('arial',20),text=d,command=copy_pass,anchor="center",border_width=2,border_color='#012B40',hover=True,hover_color="#014161")
b2.place_configure(width=150,height=50,x=300,y=180)



app.mainloop()
