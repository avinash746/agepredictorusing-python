from datetime import date
today = date.today()
 
def exit():
    window.destroy()
def get_age():
    d= int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    age =today.year-y-((today.month, today.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')
 
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#ADD8E6")
window.resizable(width=False,height=False)
window.title("Let's calculate your age")
 
l1 = tk.Label(window,text="The Age Predictor!",font=("sans serif", 20),fg="black",bg="white")
l2 = tk.Label(window,font=("serif",12),text="Enter your Birthday which includes Date,Month and Year",fg="black",bg="#ADD8E6")
 
l_d=tk.Label(window,text="Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#ADD8E6")
l_m=tk.Label(window,text="Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#ADD8E6")
l_y=tk.Label(window,text="Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#ADD8E6")
e1=tk.Entry(window,width=5)
e2=tk.Entry(window,width=5)
e3=tk.Entry(window,width=5)
 
b1=tk.Button(window,text="Calculate Age!",font=("Arial",13),command=get_age)
 
l3 = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#ADD8E6")
t1=tk.Text(window,width=5,height=0,state="disabled")
 
b2=tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)
 
l1.place(x=70,y=5)
l2.place(x=10,y=40)
l_d.place(x=100,y=70)
l_m.place(x=100,y=95)
l_y.place(x=100,y=120)
e1.place(x=180,y=70)
e2.place(x=180,y=95)
e3.place(x=180,y=120)
b1.place(x=100,y=150)
l3.place(x=50,y=200)
t1.place(x=240,y=203)
b2.place(x=100,y=230)
 
window.mainloop()
