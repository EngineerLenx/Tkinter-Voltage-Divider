from tkinter import *
from tkinter import ttk

#Ventana
root = Tk()
root.title("Cálculo de divisores de tensión")
root.geometry("400x300")
root.resizable(0, 0)

#Entrada de datos
ent_voltajein = Entry(root, width = 12, bg = "#393D42", fg = "white")
ent_voltajein.place(x = 80, y = 182)
ent_resis1 = Entry(root, width = 12, bg = "#393D42", fg = "white")
ent_resis1.place(x = 80, y = 62)
ent_resis2 = Entry(root, width = 12, bg = "#393D42", fg = "white")
ent_resis2.place(x= 80, y = 102)
ent_voltajeout = Entry(root, width = 12, bg = "#393D42", fg = "white")
ent_voltajeout.place(x= 80, y = 142)

#Funciones
def radiob_select():
    rb_s = select_opc.get()
    if rb_s == 3:
        find_Vo()
    elif rb_s == 2:
        find_r2()
    elif rb_s == 1:
        find_r1()

def find_Vo():
    try:
        sa_ohm = ohm.get()
        sa_ohm2 = ohm2.get()
        #Si resis1 es kilo ohms
        if sa_ohm == "KΩ":
            resistencia1 = float(ent_resis1.get())
            resistencia1K = resistencia1 * 1000
        #+ si resis2 es ohms
            if sa_ohm2 == "Ω":
                resistencia2 = float(ent_resis2.get())
                resistencia2 = (resistencia2)
                Vi = ent_voltajein.get()
                Vi = float(Vi)       
                Vo = Vi * (resistencia1K / (resistencia1K + resistencia2))
                print(Vo)
                result_divisor.config(text = '{:.3}'.format(Vo))
        #si resis1 es ohms
        if sa_ohm == "Ω":
            resistencia1 = float(ent_resis1.get())
            resistencia1 = (resistencia1)
            #+ si resis2 es kilo ohms
            if sa_ohm2 == "KΩ":
                resistencia2 = float(ent_resis2.get())
                resistencia2K = resistencia2 * 1000
                Vi = float(ent_voltajein.get())  
                Vo = Vi * (resistencia1 / (resistencia1 + resistencia2K))
                print(Vo)
                result_divisor.config(text = '{:.3}'.format(Vo))
        #si resis1 es mega ohms
        if sa_ohm == "MΩ":
            resistencia1 = float(ent_resis1.get())
            resistencia1M = resistencia1 * 1000000
            #+ si resis2 es ohms
            if sa_ohm2 == "Ω":
                resistencia2 = float(ent_resis2.get())
                resistencia2 = resistencia2
                Vi = float(ent_voltajein.get())
                Vo = Vi * (resistencia1M / (resistencia1M + resistencia2))
                print(Vo)
                result_divisor.config(text = '{:.3}'.format(Vo))
        #si resis1 es ohms
        if sa_ohm == "Ω":
            resistencia1 = float(ent_resis1.get())
            resistencia1 = (resistencia1)
            #+ si resis2 es mega ohms
            if sa_ohm2 == "MΩ":
                resistencia2 = float(ent_resis2.get())
                resistencia2M = resistencia2 * 1000000
                Vi = float(ent_voltajein.get())
                Vo = Vi * (resistencia1 / (resistencia1 + resistencia2M))
                print(Vo)
                result_divisor.config(text = '{:.0e}'.format(Vo))
        #si resis1 es kilo ohms
        if sa_ohm == "KΩ":
            resistencia1 = float(ent_resis1.get())
            resistencia1K = resistencia1 * 1000
            #+ resis2 es mega ohms
            if sa_ohm2 == "MΩ":
                resistencia2 = float(ent_resis2.get())
                resistencia2M = resistencia2 * 1000000
                Vi = float(ent_voltajein.get())
                Vo = Vi * (resistencia1K / (resistencia1K + resistencia2M))
                print(Vo)
                result_divisor.config(text = '{:.3}'.format(Vo))
        #si resis1 es mega ohms
        if sa_ohm == "MΩ":
            resistencia1 = float(ent_resis1.get())
            resistencia1M = resistencia1 * 1000000
            #+ si resis2 es kilo ohms
            if sa_ohm2 == "KΩ":
                resistencia2 = float(ent_resis2.get())
                resistencia2K = resistencia2 * 1000
                Vi = float(ent_voltajein.get())
                Vo = Vi * (resistencia1M / (resistencia1M + resistencia2K))
                print(Vo)
                result_divisor.config(text = '{:.3}'.format(Vo))
        #si resis1 y resis2 son ohms
        if sa_ohm == "Ω" and sa_ohm2 == "Ω":
            resistencia1 = float(ent_resis1.get())
            resistencia1 = (resistencia1)
            resistencia2 = float(ent_resis2.get())
            resistencia2 = (resistencia2)
            Vi = float(ent_voltajein.get())
            Vo = Vi * (resistencia1 / (resistencia1 + resistencia2))
            print(Vo)
            result_divisor.config(text = '{:.3}'.format(Vo))
        #si resis1 y resis2 son kilo ohms
        if sa_ohm == "KΩ" and sa_ohm2 == "KΩ":
            resistencia1 = float(ent_resis1.get())
            resistencia1K = resistencia1 * 1000
            resistencia2 = float(ent_resis2.get())
            resistencia2K = resistencia2 * 1000
            Vi = float(ent_voltajein.get())
            Vo = Vi * (resistencia1K / (resistencia1K + resistencia2K))
            print(Vo)
            result_divisor.config(text = '{:.3}'.format(Vo))
        #si resis1 y resis2 son mega ohms
        if sa_ohm == "MΩ" and sa_ohm2 == "MΩ":
            resistencia1 = float(ent_resis1.get())
            resistencia1M = resistencia1 * 1000000
            resistencia2 = float(ent_resis2.get())
            resistencia2M = resistencia2 * 1000000
            Vi = float(ent_voltajein.get())
            Vo = Vi * (resistencia1M / (resistencia1M + resistencia2M))
            print(Vo)
            result_divisor.config(text = '{:.3}'.format(Vo))
        uniRs.config(text = "V")
    except ValueError:
        pass

def find_r1():
    try:
        s_ohm1 = ohm.get()
        s_ohm2 = ohm2.get()
        Vo = ent_voltajeout.get()
        Vo = float(Vo)
        #si la resistencia que introduce está en ohms
        if s_ohm2 == "Ω":
            resistencia2 = ent_resis2.get()
            resistencia2 = float(resistencia2)
            if s_ohm2 == "Ω" and s_ohm1 == "Ω":
                Vi = float(ent_voltajein.get())
                r1 = resistencia2 * Vo / (Vi - Vo)
                print(r1)
                uniRs.config(text = "Ω")
                result_divisor.config(text = '{:.4}'.format(r1))
            if s_ohm2 == "Ω" and s_ohm1 == "KΩ":
                Vi = float(ent_voltajein.get())
                r1 = resistencia2 * Vo / (Vi - Vo)
                r1 = r1 / 1000
                print(r1)
                uniRs.config(text = "KΩ")
                result_divisor.config(text = '{:.3}'.format(r1))
            if s_ohm2 == "Ω" and s_ohm1 == "MΩ":
                Vi = float(ent_voltajein.get())
                r1 = resistencia2 * Vo / (Vi - Vo)
                r1 = r1 / 1000000
                print(r1)
                uniRs.config(text = "MΩ")
                result_divisor.config(text = '{:.2e}'.format(r1))
        #si la resistencia que introduce está en kilo ohms
        if s_ohm2 == "KΩ":
            resistencia2 = ent_resis2.get()
            resistencia2 = float(resistencia2)
            resistenciaK2 = resistencia2 * 1000
            Vi = float(ent_voltajein.get())
            r1 = resistenciaK2 * Vo / (Vi - Vo)
            if s_ohm2 == "KΩ" and s_ohm1 == "Ω":
                r1 = resistenciaK2 * Vo / (Vi - Vo)
                print(r1)
                uniRs.config(text = "Ω")
                result_divisor.config(text = '{:.7}'.format(r1))
            if s_ohm2 == "KΩ" and s_ohm1 == "KΩ":
                r1 = resistenciaK2 * Vo / (Vi - Vo)
                r1 = r1 / 1000
                print(r1)
                uniRs.config(text = "KΩ")
                result_divisor.config(text = '{:.4}'.format(r1))
            if s_ohm2 == "KΩ" and s_ohm1 == "MΩ":
                r1 = resistenciaK2 * Vo / (Vi - Vo)
                r1 = r1 / 1000000
                print(r1)
                uniRs.config(text = "MΩ")
                result_divisor.config(text = '{:.3}'.format(r1))
        #si la resistencia que introduce está en mega ohms
        if s_ohm2 == "MΩ":
            resistencia2 = ent_resis2.get()
            resistencia2 = float(resistencia2)
            resistenciaM2 = resistencia2 * 1000000
            Vi = float(ent_voltajein.get())
            r1 = resistenciaM2 * Vo / (Vi - Vo)
        if s_ohm2 == "MΩ" and s_ohm1 == "Ω":
            r1 = resistenciaM2 * Vo / (Vi - Vo)
            print(r1)
            uniRs.config(text = "Ω")
            result_divisor.config(text = '{:.10}'.format(r1))
        if s_ohm2 == "MΩ" and s_ohm1 == "MΩ":
            r1 = resistenciaM2 * Vo / (Vi - Vo)
            r1 = r1 / 1000000
            print(r1)
            uniRs.config(text = "MΩ")
            result_divisor.config(text = '{:.4}'.format(r1))
        if s_ohm2 == "MΩ" and s_ohm1 == "KΩ":
            r1 = resistenciaM2 * Vo / (Vi - Vo)
            r1 = r1 / 1000
            print(r1)
            uniRs.config(text = "KΩ")
            result_divisor.config(text = '{:.7}'.format(r1))
    except ValueError:
        pass

def find_r2():
    try:
        s_ohm2 = ohm2.get()
        s_ohm = ohm.get()
        Vo = ent_voltajeout.get()
        Vo = float(Vo)
        #si la resistencia que introduce está en ohms
        if s_ohm == "Ω":
            resistencia1 = ent_resis1.get()
            resistencia1 = float(resistencia1)
            if s_ohm == "Ω" and s_ohm2 == "Ω":
                Vi = float(ent_voltajein.get())
                r2 = (Vi - Vo) / (Vo) * (resistencia1)
                print(r2)
                uniRs.config(text = "Ω")
                result_divisor.config(text = '{:.4}'.format(r2))
            if s_ohm == "Ω" and s_ohm2 == "KΩ":
                Vi = float(ent_voltajein.get())
                r2 = (Vi - Vo) / (Vo) * (resistencia1)
                r2 = r2 / 1000
                print(r2)
                uniRs.config(text = "KΩ")
                result_divisor.config(text = '{:.1}'.format(r2))
            if s_ohm == "Ω" and s_ohm2 == "MΩ":
                Vi = float(ent_voltajein.get())
                r2 = (Vi - Vo) / (Vo) * (resistencia1)
                r2 = r2 / 1000000
                print(r2)
                uniRs.config(text = "MΩ")
                result_divisor.config(text = '{:.3e}'.format(r2))
        #si la resistencia que introduce está en kilo ohms
        if s_ohm == "KΩ":
            resistencia1 = ent_resis1.get()
            resistencia1 = float(resistencia1)
            resistenciaK1 = resistencia1 * 1000
            Vi = float(ent_voltajein.get())
            if s_ohm == "KΩ" and s_ohm2 == "Ω": 
                r2 = (Vi - Vo) / (Vo) * (resistenciaK1)
                print(r2)
                uniRs.config(text = "Ω")
                result_divisor.config(text = '{:.7}'.format(r2))
            if s_ohm == "KΩ" and s_ohm2 == "KΩ": 
                r2 = (Vi - Vo) / (Vo) * (resistenciaK1)
                r2 = r2 / 1000
                print(r2)
                uniRs.config(text = "KΩ")
                result_divisor.config(text = '{:.4}'.format(r2))
            if s_ohm == "KΩ" and s_ohm2 == "MΩ": 
                r2 = (Vi - Vo) / (Vo) * (resistenciaK1)
                r2 = r2 / 1000000
                print(r2)
                uniRs.config(text = "MΩ")
                result_divisor.config(text = '{:.1}'.format(r2))
        #si la resistencia que introduce está en mega ohms
        if s_ohm == "MΩ":
            resistencia1 = ent_resis1.get()
            resistencia1 = float(resistencia1)
            resistenciaM1 = resistencia1 * 1000000
            Vi = float(ent_voltajein.get())
            if s_ohm == "MΩ" and s_ohm2 == "Ω":
                r2 = (Vi - Vo) / (Vo) * (resistenciaM1)
                print(r2)
                uniRs.config(text = "Ω")
                result_divisor.config(text = '{:.10}'.format(r2))
            if s_ohm == "MΩ" and s_ohm2 == "KΩ":
                r2 = (Vi - Vo) / (Vo) * (resistenciaM1)
                r2 = r2 / 1000
                print(r2)
                uniRs.config(text = "KΩ")
                result_divisor.config(text = '{:.7}'.format(r2))
            if s_ohm == "MΩ" and s_ohm2 == "MΩ":
                r2 = (Vi - Vo) / (Vo) * (resistenciaM1)
                r2 = r2 / 1000000
                print(r2)
                uniRs.config(text = "MΩ")
                result_divisor.config(text = '{:.4}'.format(r2))
    except ValueError:
        pass

def ClearC():
    ent_voltajein.delete(0, END)
    ent_resis1.delete(0, END)
    ent_resis2.delete(0, END)
    ent_voltajeout.delete(0, END)
    result_divisor.config(text = "")
    uniRs.config(text = "")
#Label del título
título_divisor_de_tension = Label(root, text = "DIVISOR DE TENSIÓN SIN CARGA", font = ("consolas", 18))
título_divisor_de_tension.place(x = 15, y = 0)

#Label de Vi
LVi = Label(root, text = "Vi =")
LVi.place(x= 25, y = 180)

#Label de las unidades
uniRs = ttk.Label(root, text = "", width = 4)
uniRs.place(x = 160, y = 222)

#Combobox R1
ohm = StringVar()
ohms = ttk.Combobox(root, state = "readonly", width = 4, textvariable = ohm)
ohms.place(x = 160, y = 60)
ohms["values"] = ("Ω", "KΩ", "MΩ")
ohms.current(0)
#Combobox R2
ohm2 = StringVar()
ohm2 = ttk.Combobox(root, state = "readonly", width = 4, textvariable = ohm2)
ohm2.place(x = 160, y = 100)
ohm2["values"] = ("Ω", "KΩ", "MΩ")
ohm2.current(0)

#Radiobuttons R1, R2 o Vo y botones
select_opc = IntVar()
Res1 = ttk.Radiobutton(root, text = "R1 =", variable = select_opc, value = 1)
Res1.place(x = 15, y = 60)
Res2 = ttk.Radiobutton(root, text = "R2 =", variable = select_opc, value = 2)
Res2.place(x = 15, y = 100)
Vo = ttk.Radiobutton(root, text = "Vo =", variable = select_opc, value = 3)
Vo.place(x = 15, y = 140)
select_opc.set(3)

#Label del resultado
result_divisor = ttk.Label(root, text= "", font = "Consolas", width = 13)
result_divisor.place(x = 80, y = 220)

#Boton del resultado
boton = ttk.Button(root, text = "Calcular", command = radiob_select)
boton.place(x = 15, y = 260)

#Boton de borrado
botonclean = ttk.Button(root, text = "Borrar", command = ClearC)
botonclean.place(x = 120, y = 260)

#Ejecución de la ventana, siempre al final del código.
root.mainloop()