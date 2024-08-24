from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task = task_field.get().strip()
    if not task:
        messagebox.showinfo('Error', 'Field is empty.')
    elif task in tasks:
        messagebox.showinfo('Error', 'Task already exists.')
    else:
        tasks.append(task)
        the_cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task,))
        the_connection.commit()
        update_listbox()
        task_field.delete(0, 'end')

def update_listbox():
    task_listbox.delete(0, 'end')
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        tasks.remove(task)
        update_listbox()
        the_cursor.execute('DELETE FROM tasks WHERE title = ?', (task,))
        the_connection.commit()
    except IndexError:
        messagebox.showinfo('Error', 'No task selected.')

def delete_all_tasks():
    if messagebox.askyesno('Delete All', 'Are you sure?'):
        tasks.clear()
        the_cursor.execute('DELETE FROM tasks')
        the_connection.commit()
        update_listbox()

def close_app():
    the_cursor.close()
    the_connection.close()
    guiWindow.destroy()

def load_tasks():
    tasks.clear()
    for row in the_cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("665x400+550+250")
    guiWindow.configure(bg="#B5E5CF")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT UNIQUE)')
    tasks = []

    functions_frame = Frame(guiWindow, bg="#8EE5EE")
    functions_frame.pack(expand=True, fill="both")

    Label(functions_frame, text="Enter Task:", font=("Arial", 14, "bold"), bg="#8EE5EE").grid(row=0, column=0, padx=20, pady=10, sticky="w")
    task_field = Entry(functions_frame, font=("Arial", 14), width=42)
    task_field.grid(row=0, column=1, padx=20, pady=10, columnspan=3)

    Button(functions_frame, text="Add", width=15, bg='#D4AC0D', font=("Arial", 14, "bold"), command=add_task).grid(row=1, column=0, padx=20, pady=10)
    Button(functions_frame, text="Remove", width=15, bg='#D4AC0D', font=("Arial", 14, "bold"), command=delete_task).grid(row=1, column=1, padx=20, pady=10)
    Button(functions_frame, text="Delete All", width=15, bg='#D4AC0D', font=("Arial", 14, "bold"), command=delete_all_tasks).grid(row=1, column=2, padx=20, pady=10)
    Button(functions_frame, text="Exit", width=52, bg='#D4AC0D', font=("Arial", 14, "bold"), command=close_app).grid(row=2, column=0, columnspan=4, padx=20, pady=10)

    task_listbox = Listbox(functions_frame, width=70, height=9, font="bold", selectmode='SINGLE', bg="WHITE")
    task_listbox.grid(row=3, column=0, columnspan=4, padx=20, pady=10)

    load_tasks()
    update_listbox()
    guiWindow.mainloop()
