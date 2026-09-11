import json
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pass():
  nr_letters = randint(8, 10)
  nr_symbols = randint(2, 4)
  nr_numbers = randint(2, 4)

  password_letters=[choice(letters) for _ in range(randint(8,10))]
  password_numbers=[choice(numbers) for _ in range(randint(2,4))]
  password_symbols=[choice(symbols) for _ in range(randint(8,10))]

  password_list = password_letters+password_numbers+password_symbols
  shuffle(password_list)
  password="".join(password_list)
  #print(f"Your password is: {password}")

  password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def Save():
  website_entry_text=website_entry.get()
  password_entry_text=password_entry.get()
  email_entry_text=email_entry.get()
  if len(website_entry_text)<=0:
    messagebox.showwarning(title="Warning",message="Please Enter website")
    website_entry.focus
    return
  elif len(password_entry_text)<=0:
    messagebox.showwarning(title="Warning",message="Please Enter Password")
    password_entry.focus
    return
  elif len(email_entry_text)<=0:
      messagebox.showwarning(title="Warning",message="Please Enter Email")
      email_entry.focus
      return

  else:
    new_data={
        website_entry_text:{
            "email":email_entry_text,
            "password":password_entry_text
        }
    }
    print(new_data)

    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json","w") as data_file:
            json.dumps(new_data,data_file,indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)



def search_password():
   website_search=website_entry.get()
   with open("data.json","r") as data_file:
       json_data = json.load(data_file)
       if website_search in json_data:
           email=json_data[website_search]["email"]
           password=json_data[website_search]["password"]

   print(website_search)








 
 
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "arshkumar930@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons

search_button=Button(text="Search",command=search_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(
    text="Generate Password",
    command=generate_pass
)
generate_password_button.grid(row=3, column=2)

add_button = Button(
    text="Add",
    width=36,
    command=Save
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()


# window=Tk()

# window.title("Password Manager")
# window.config(padx=50,pady=50)
# canvas=Canvas(height=200,width=200)
# logo_image=PhotoImage(file="D://Arsh//pypy//MyPass//logo.png")
# canvas.create_image(100,100,image=logo_image)
# canvas.grid(row=0,column=1)

# #labels
# website_label=Label(text="Website:",width=10)
# website_label.grid(row=1,column=0)

# email_label=Label(text="Email/Username",width=10)
# email_label.grid(row=2,column=0)

# password_label=Label(text="Password:",width=10)
# password_label.grid(row=3,column=0)

# #entries
# website_entry=Entry(width=30)
# website_entry.grid(row=1,column=1,columnspan=2)
# website_entry.focus()

# email_entry=Entry(width=30)
# email_entry.grid(row=2,column=1,columnspan=2)
# email_entry.insert(0,"example@gmail.com")

# password_entry=Entry(width=20)
# password_entry.grid(row=3,column=1,sticky="w")


# #buttons
# password_button=Button(text="Generate Password",width=10,command=generate_pass)
# password_button.grid(row=3,column=1)


# button_Add = Button(text="Add",width=30,command=Save)
# button_Add.grid(row=4, column=1)

# window.mainloop()









