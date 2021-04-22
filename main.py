import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

apps = []

## Make sure comma gets added when files is added only
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]



##Function for browsing our file explorer

def browseFiles():

    ## delete previous labels before adding new label
    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("all files", "*.*"), ("executables", "*.exe")))
    apps.append(filename)
    print(filename)

    ## Create label based on whatever app we have on the apps
    for app in apps:
        label = tk.Label(frame, text=app, bg='#263D89')
        label.pack()


##Function That will run our apps in our GUI app (apps = [])

def runApps():
    for app in apps:
        os.startfile(app)


CANVAS = tk.Canvas(root, height=600, width=600, bg='#263D62')
CANVAS.pack()

frame = tk.Frame(root, bg='#263D42')
frame.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.05)


Browser = tk.Button(root, text='Browser', padx=10, pady=5, fg='white', bg='#196E63', border="0",command=browseFiles )
Browser.pack()

Run = tk.Button(root, text='Run app', padx=9, pady=5, fg='white', bg='#196E63', border="0",command=runApps)
Run.pack()

## Make sure that saved files show even after exiting the app and reopening the app
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

##Save the file 
with open('save.txt', 'w') as saved:
    for app in apps:
        saved.write(app + ',')