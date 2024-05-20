import tkinter as tk

def submit(token_var, master):
    token = token_var.get()
    with open("token.json", "w") as tokenfile:
        tokenfile.write(token)
    token_var.set("")
    master.withdraw()
    second_window()

def submit1(to_var, from_var, subject_var, body_text):
    print("To:", to_var.get())
    print("From:", from_var.get())
    print("Subject:", subject_var.get())
    print("Body:", body_text.get("1.0", "end-1c"))  # Get the text from the text widget

def first_window():
    master = tk.Tk()
    frame = tk.Frame(master)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    token_label = tk.Label(frame, text="Token:")
    token_label.pack(fill='x', expand=True)

    token_var = tk.StringVar()
    token_entry = tk.Entry(frame, textvariable=token_var)
    token_entry.pack(fill='x', expand=True)
    token_entry.focus()

    sub_btn = tk.Button(frame, text='Submit', command=lambda: submit(token_var, master))
    sub_btn.pack(fill='x')

    master.mainloop()

def second_window():
    root1 = tk.Toplevel()
    root1.title('PyMail')

    to_label = tk.Label(root1, text="To:")
    from_label = tk.Label(root1, text="From:")
    subject_label = tk.Label(root1, text="Subject:")
    body_label = tk.Label(root1, text="Body:")

    to_var = tk.StringVar()
    from_var = tk.StringVar()
    subject_var = tk.StringVar()

    to_entry = tk.Entry(root1, textvariable=to_var)
    from_entry = tk.Entry(root1, textvariable=from_var)
    subject_entry = tk.Entry(root1, textvariable=subject_var)
    body_text = tk.Text(root1, height=5, width=30)

    sub_btn = tk.Button(root1, text='Submit', command=lambda: submit1(to_var, from_var, subject_var, body_text))

    to_label.grid(row=0, column=0, pady=2)
    from_label.grid(row=1, column=0, pady=2)
    subject_label.grid(row=2, column=0, pady=2)
    body_label.grid(row=3, column=0, pady=2)

    to_entry.grid(row=0, column=1, pady=2)
    from_entry.grid(row=1, column=1, pady=2)
    subject_entry.grid(row=2, column=1, pady=2)
    body_text.grid(row=3, column=1, pady=2)

    sub_btn.grid(row=4, column=1, pady=2)

    root1.mainloop()

def main():
    first_window()

if __name__ == "__main__":
    main()
