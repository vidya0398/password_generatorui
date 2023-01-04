import tkinter
import random
from tkinter import messagebox
import json

FONT_NAME = "Italic"
WHITE = '#FFFFFF'
GREY = '#808080'
window = tkinter.Tk()
window.title("Password manager")
window.config(padx=20, pady=40, bg=WHITE)
char_list = [ 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
              'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
              'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
              's', 'S', 't', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x',
              'X', 'y', 'Y', 'z', 'Z', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}',
              '}', '|', ]


def button_clicked():
    if len(user_input_email.get()) == 0 or len(user_input_password.get()) == 0 or len(user_input_website.get()) == 0:
        messagebox.showinfo(title='Error', message="Please fill all your details")
    else:
        messagebox.showinfo(title='Notification', message="Your data is saved")
        new_dict = {
            user_input_website.get(): {
                "email": user_input_email.get(),
                "password": user_input_password.get(),
            }
        }
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_dict)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            # user_input_email.delete(0, 'end')
            user_input_password.delete(0, 'end')
            user_input_website.delete(0, 'end')


def generate_pwd():
    password = random.sample(char_list, 10)
    string_password = ''.join(password)
    user_input_password.insert(0, string_password)


def search_pwd():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        #print(data)
        if user_input_website.get() in data:
            nested_dict = data.get(user_input_website.get())
            email = nested_dict.get("email")
            password = nested_dict.get("password")
            messagebox.showinfo(title='Notification', message=f"'Email'={email},'Password'={password}")

        else:
            messagebox.showinfo(title='Notification', message="The details for this website are not stored.")



window.minsize(width=500, height=300)
canvas = tkinter.Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
password_img = tkinter.PhotoImage(file="password_img2.png")
canvas.create_image(90, 85, image=password_img)
password_text = canvas.create_text(90, 182, text="MyPass", font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=0, column=1, rowspan=2, columnspan=2)

website_label = tkinter.Label(text="Website: ", font=("Italic", 12, "bold"), bg=WHITE)
website_label.grid(row=2, column=0)

email_label = tkinter.Label(text="Email:   ", font=("Italic", 12, "bold"), bg=WHITE)
email_label.grid(row=3, column=0)

password_label = tkinter.Label(text="Password:", font=("Italic", 12, "bold"), bg=WHITE)
password_label.grid(row=4, column=0)

user_input_website = tkinter.Entry(relief="raised", fg='#000000', width=20, highlightbackground=GREY,
                                   highlightthickness=1)
user_input_website.grid(row=2, column=1)
user_input_website.focus()

search_button = tkinter.Button(text="Search", width=20, command=search_pwd)
search_button.grid(row=2, column=2)

user_input_email = tkinter.Entry(relief="raised", fg='#000000', width=50, highlightbackground=GREY,
                                 highlightthickness=1)
user_input_email.grid(row=3, column=1, columnspan=2)
user_input_email.insert(0, "vidyar0398@gmail.com")

user_input_password = tkinter.Entry(relief="raised", fg='#000000', width=20, highlightbackground=GREY,
                                    highlightthickness=1, show='*')
user_input_password.grid(row=4, column=1)

generate_pwd_button = tkinter.Button(text="Generate password", width=20, command=generate_pwd)
generate_pwd_button.grid(row=4, column=2)

add_pwd_button = tkinter.Button(text="Add", width=40, command=button_clicked)
add_pwd_button.grid(row=5, column=1, columnspan=2)

#
# my_label = tkinter.Label(text="I am a label", font=("Italic", 24, "bold"))
# my_label.grid(row=0, column=0)
#
#
# def button_clicked():
#     my_label.config(text=user_input.get())
#
#
# button1 = tkinter.Button(text="Clickme", command=button_clicked)
# button1.grid(row=2, column=2)
# button2 = tkinter.Button(text="Clickme", command=button_clicked)
# button2.grid(row=1, column=3)
window.mainloop()
