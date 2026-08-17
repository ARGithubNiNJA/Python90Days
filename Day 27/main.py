from tkinter import *

window=Tk()

window.title("My First GUI")
window.geometry("500x500")

def button_clicked():
    my_label.config(text="My Name Is Arsh")
    new_text=input.get()
    my_label.config(text=new_text)

#label creation
#inside the tkinter class there is element called label

my_label=Label(window,text="My Name Is Arsh",font=("Arial",24))#.grid(row=0,column=0)
# my_label.pack()  #this displays the label on the window Packer
my_label.grid(row=0,column=0)


#button
button=Button(window,text="Click Me",command=button_clicked)
# button.pack()
button.grid(row=1,column=1)

#input
input=Entry(window)
print(input.get())
# input.pack()
input.grid(row=1,column=0)

window.mainloop()