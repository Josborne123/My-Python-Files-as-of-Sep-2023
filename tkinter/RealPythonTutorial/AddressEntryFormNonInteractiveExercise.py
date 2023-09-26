import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

window.rowconfigure([0,1,2,3,4,5,6,7], minsize=10)
window.rowconfigure(8, minsize=35)
window.columnconfigure([0,1], minsize=50)

frm_form = tk.Frame()
frm_form.pack()

firstname = tk.Label(master=frm_form, text="First Name:")
lastname = tk.Label(master=frm_form, text="Last Name:")
address1 = tk.Label(master=frm_form, text="Address Line 1:")
address2 = tk.Label(master=frm_form, text="Address Line 2:")
city = tk.Label(master=frm_form, text="City:")
state = tk.Label(master=frm_form, text="State/Province:")
postalcode = tk.Label(master=frm_form, text="Postal Code")
country = tk.Label(master=frm_form, text="Country:")


entryname = tk.Entry(master=frm_form, bg="white", fg="black", width=50, relief="solid")
entry2 = tk.Entry(master=frm_form, bg="white", fg="black", width=50, relief="solid")
entry3 = tk.Entry(master=frm_form, bg="white", fg="black", width=50, relief="solid")
entry4 = tk.Entry(master=frm_form, bg="white", fg="black", width=50, relief="solid")
entry5 = tk.Entry(master=frm_form, bg="white", fg="black", width=50, relief="solid")
entry6 = tk.Entry(master=frm_form, bg="white", fg="black", width=50, relief="solid")
entry7 = tk.Entry(master=frm_form, bg="white", fg="black", width=50, relief="solid")
entry8 = tk.Entry(master=frm_form, bg="white", fg="black", width=50, relief="solid")


firstname.grid(row=0, column=0, sticky="e")
lastname.grid(row=1, column=0, sticky="e")
address1.grid(row=2, column=0, sticky="e")
address2.grid(row=3, column=0, sticky="e")
city.grid(row=4, column=0, sticky="e")
state.grid(row=5, column=0, sticky="e")
postalcode.grid(row=6, column=0, sticky="e")
country.grid(row=7, column=0, sticky="e")


entryname.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)
entry6.grid(row=5, column=1)
entry7.grid(row=6, column=1)
entry8.grid(row=7, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X)

submit = tk.Button(master=frm_buttons, text="Submit", width=6, height=1, relief="raised")
#submit.grid(row=8, column=1, sticky="e")
submit.pack(side=tk.RIGHT, padx=5, pady=5)

clear = tk.Button(master=frm_buttons, text="Clear", width=6, height=1, relief="raised")
#clear.grid(row=8, column=1, sticky="e")
clear.pack(side=tk.RIGHT, padx=7, pady=5)



window.mainloop()