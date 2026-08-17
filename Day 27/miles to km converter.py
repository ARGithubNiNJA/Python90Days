from tkinter import *

window=Tk()
window.title("Miles to Km")
window.geometry("200x200")
window.configure(padx=20,pady=20)

def calculate():
    miles=float(miles_entry.get())
    km=round(miles*1.60934)
    label_output.config(text=str(km))

miles_entry=Entry(width=7)

miles_entry.grid(row=1,column=1)
miles_label=Label(text="Miles to Km Converter")

miles_label_miles=Label(text="Miles")
miles_label_miles.grid(row=1,column=2)
miles_is_equal_to=Label(text="is equal to")
miles_is_equal_to.grid(row=2,column=0)

label_output=Label(text="-")
label_output.grid(row=2,column=1)

kilometers_label=Label(text="kilometers")
kilometers_label.grid(row=2,column=2)
calculate_button=Button(text="Calculate",command=calculate)
calculate_button.grid(row=3,column=1)




window.mainloop()
