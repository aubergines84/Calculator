import tkinter as tk
root = tk.Tk()
root.geometry('350x300')
root.title('calculatrice')
textbox=tk.Text(root,height=1)
textbox.pack(pady=2)
Button=tk.Button(root,text='clear',command=lambda:textbox.delete('1.0', tk.END))
Button.pack()
def calcul():
    equation=textbox.get('1.0', tk.END)
    textbox.delete('1.0', tk.END)

    try:
        total=eval(equation)
        textbox.insert(tk.END, total)
    except:
        textbox.insert(tk.END, 'error')





ButtonFrame=tk.Frame(root)
ButtonFrame.columnconfigure(0,weight=1)
ButtonFrame.columnconfigure(1,weight=1)
ButtonFrame.columnconfigure(2,weight=1)

Btn1=tk.Button(ButtonFrame,text='1',command=lambda:textbox.insert(tk.END,'1'))
Btn1.grid(row=0,column=0,sticky=tk.E+tk.W)
Btn2=tk.Button(ButtonFrame,text='2', command=lambda:textbox.insert(tk.END,'2'))
Btn2.grid(row=0,column=1, sticky=tk.E+tk.W)
Btn3=tk.Button(ButtonFrame,text='3',command=lambda:textbox.insert(tk.END,'3'))
Btn3.grid(row=0,column=2, sticky=tk.E+tk.W)
Btn4=tk.Button(ButtonFrame,text='4',command=lambda:textbox.insert(tk.END,'4'))
Btn4.grid(row=1,column=0, sticky=tk.E+tk.W)
Btn5=tk.Button(ButtonFrame,text='5', command=lambda:textbox.insert(tk.END,'5'))
Btn5.grid(row=1,column=1, sticky=tk.E+tk.W)
Btn6=tk.Button(ButtonFrame,text='6', command=lambda:textbox.insert(tk.END,'6'))
Btn6.grid(row=1,column=2, sticky=tk.E+tk.W)
Btn7=tk.Button(ButtonFrame,text='7', command=lambda:textbox.insert(tk.END,'7'))
Btn7.grid(row=2,column=0, sticky=tk.E+tk.W)
Btn8=tk.Button(ButtonFrame,text='8', command=lambda:textbox.insert(tk.END,'8'))
Btn8.grid(row=2,column=1, sticky=tk.E+tk.W)
Btn9=tk.Button(ButtonFrame,text='9', command=lambda:textbox.insert(tk.END,'9'))
Btn9.grid(row=2,column=2, sticky=tk.E+tk.W)
Btn10=tk.Button(ButtonFrame,text='+',bg='#96bfff', command=lambda:textbox.insert(tk.END,'+'))
Btn10.grid(row=3,column=0,sticky=tk.E+tk.W)
Btn11=tk.Button(ButtonFrame,text='-',bg='#96bfff', command=lambda:textbox.insert(tk.END,'-'))
Btn11.grid(row=3,column=1, sticky=tk.E+tk.W)
Btn12=tk.Button(ButtonFrame,text='0', command=lambda:textbox.insert(tk.END,'0'))
Btn12.grid(row=3,column=2, sticky=tk.E+tk.W)
Btn12=tk.Button(ButtonFrame,text='/', bg='#96bfff', command=lambda:textbox.insert(tk.END,'/'))
Btn12.grid(row=4,column=0, sticky=tk.E+tk.W)
Btn12=tk.Button(ButtonFrame,text='=',bg='#88ff73', command=calcul)
Btn12.grid(row=4,column=1, columnspan=2, sticky=tk.E+tk.W)


ButtonFrame.pack(fill='x', pady=5)




root.mainloop()

