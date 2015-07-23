#!/usr/bin/env python3
import threading, time, tkinter, tkinter.messagebox

reminder = ("")
sleepTime = ("")
reminder_filePath = ('/home/callum/Documents/Popupreminder/Reminder.txt')
top = tkinter.Tk()

def popupBox():
    f = open(reminder_filePath, 'r')
    print(f.read())

def createPopup():
    B1 = tkinter.Button(top, text = 'You have reminders to view!\n click to view in terminal', command = popupBox)
    B1.pack()
    top.mainloop()

createPopup()

while True:
    def createReminder(reminder):
        reminder = input("What would you like to add to your list of reminders: ")
        if reminder == ("nothing"):
            print("Okay")
            wantReminder()
        elif reminder == ("quit"):
            quit()
        else:
            with open(reminder_filePath, 'a') as reminderFile:
                reminderFile.write(reminder + '\n')
            print("Reminder added!")

    def wantReminder():
        want_reminder = input("Would you like to see your reminders?" + "\n" + "y/n: ")
        if want_reminder == ("y"):
            f  = open(reminder_filePath, 'r')
            print(f.read())
        elif want_reminder == ("quit"):
            quit()
        else:
            sleeping()

    def sleeping():
        sleepTime = input("How long (seconds) before you would like to be reminded again: ")
        sleepTime = float(sleepTime)
        time.sleep(sleepTime)

    createReminder(reminder)
    wantReminder()
