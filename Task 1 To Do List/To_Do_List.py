from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("300x550+300+50")
root.resizable(False, False)

task_list = []

# to add Task
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("taskList.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listBox.insert(END, task)

# to delete Task
def deleteTask():
    task = str(listBox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("taskList.txt", "w") as taskfile:
            for item in task_list:
                taskfile.write(item + "\n")
        listBox.delete(ANCHOR)

#  to Mark Task is complete
def markCompleted():
    task = listBox.get(ANCHOR)
    if task:
        listBox.delete(ANCHOR)
        listbox2.insert(END, task)


def openTaskFile():
    with open("taskList.txt", "r") as taskfile:
        tasks = taskfile.readlines()

    for task in tasks:
        if task.strip():
            task_list.append(task.strip())
            listBox.insert(END, task.strip())

# Edit task
def editTask():
    task = str(listBox.get(ANCHOR))
    task_entry.insert(0, task)
    if task in task_list:
        task_list.remove(task)
        with open("taskList.txt", 'w') as taskfile:
            for item in task_list:
                taskfile.write(item + "\n")

        listBox.delete(ANCHOR)

# icon
Image_icon = PhotoImage(file="Images/iconToDo.png")
root.iconphoto(False, Image_icon)

label = Label(root, text="To Do List", font="arial 20 bold", fg="white", bg="#041E42")
label.pack(side="top", fill=BOTH)



# main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=70)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 15", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="Add", font="arial 20 bold", width=6, bg="#041E42", fg="#fff", bd=0, command=addTask)
button.place(x=210, y=0)

# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#041E42")
frame1.pack(pady=(100, 0))

listBox = Listbox(frame1, font=("arial", 12), width=30, height=6, bg="#041E42", fg="white", cursor="hand2",
                  selectbackground="#5a95ff")
listBox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)

openTaskFile()


# completed tasks
frame2 = Frame(root, bd=3, width=700, height=150, bg="#041E42")
frame2.pack(pady=(20, 0))
title_label = Label(frame2, text="Completed Tasks", bg="#041E42", fg="white", font=("Arial", 16))
title_label.pack()
listbox2 = Listbox(frame2, font=('arial, 12'), width=40, height=6, bg="#041E42", fg="white", cursor="hand2",
                   selectbackground="#041E42")
listbox2.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=BOTH)

# delete
delete_icon = PhotoImage(file="Images/delete.jpg")
delete_icon = delete_icon.subsample(10)
Button(root, image=delete_icon, bd=0, command=deleteTask).place(x=120, y=470)

# Edit
edit_icon = PhotoImage(file="Images/Pen.png")
edit_icon = edit_icon.subsample(10)
Button(root, image=edit_icon, bd=0, command=editTask).place(x=190, y=470)

# Mark complete
mark_completed_icon = PhotoImage(file="Images/Mark.png")
mark_completed_icon = mark_completed_icon.subsample(12)
Button(root, image=mark_completed_icon, bd=0, command=markCompleted).place(x=50, y=470)

root.mainloop()