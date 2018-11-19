import csv
from tkinter import *
import tkinter.messagebox as box

master = Tk()

label1 = Label(master, text = 'Enter Patient_ID', relief = 'groove', width = 40)

e1 = Entry(master, relief = 'groove', width = 40)

def patient_file():
    csvfile = open('trek2.csv', 'r')
    read = csv.reader(csvfile)
    contains_keyword = False
    
    for row in read:
        if str(e1.get()) in row:
            contains_keyword = True
            break
    if contains_keyword:
        third_interface()
    else:
        box.showinfo('Search Result','PATIENT ID NOT FOUND: SELECT NEW PATIENT')
        master.mainloop()
                                       

def new_patient_file():
    second_interface()

def next_patient():
    e1.delete(0,END)
    
                                 
button3 = Button(master, text = 'Search Patient File', relief = 'groove', width = 25, command=patient_file)
button4 = Button(master, text = 'New Patient', relief = 'groove', width = 25, command=new_patient_file)
button5 = Button(master, text = 'Clear', relief = 'groove', width = 25, command=next_patient)

label1.grid( row = 1, column = 1, padx = 10 )

e1.grid( row = 1, column = 2, padx = 10 )

button3.grid( row = 3, column = 1, columnspan = 2)
button4.grid( row = 4, column = 1, columnspan = 2)
button5.grid( row = 5, column = 1, columnspan = 2)

#Static Properties
master.title('Trek Connect') 
    

def second_interface():
        
    master = Tk()
    label1 = Label(master, text = 'Patient ID', relief = 'groove', width = 40)
    label2 = Label(master, text = 'Patient Name', relief = 'groove', width = 40)
    label3 = Label(master, text = 'Community ID', relief = 'groove', width = 40)
    label4 = Label(master, text = 'Height', relief = 'groove', width = 40)
    label5 = Label(master, text = 'Weight', relief = 'groove', width = 40)
    label6 = Label(master, text = 'Comments', relief = 'groove', width = 40, height = 5)


    e1 = Entry(master, relief = 'groove', width = 40)
    e2 = Entry(master, relief = 'groove', width = 40)
    e3 = Entry(master, relief = 'groove', width = 40)
    e4 = Entry(master, relief = 'groove', width = 40)
    e5 = Entry(master, relief = 'groove', width = 40)
    e6 = Text(master, relief = 'groove', width = 45, height = 5, borderwidth = 2)


    def show_entry_fields():
        csvfile = open('trek2.csv', 'a')
        writer = csv.writer(csvfile)
        patients = str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get()),str(e6.get(1.0,END))
        writer.writerow(patients)
        return box.showinfo('Confirmation','Entry Confirmed. Select Clear.')
        master.mainloop()

    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(1.0,END)
        
            
    button1 = Button(master, text = 'Enter', relief = 'groove', width = 20, command=show_entry_fields)
    button2 = Button(master, text = 'Clear', relief = 'groove', width = 20, command=clear)


    #Geometry
    label1.grid( row = 1, column = 1, padx = 10 )
    label2.grid( row = 2, column = 1, padx = 10 )
    label3.grid( row = 3, column = 1, padx = 10 )
    label4.grid( row = 4, column = 1, padx = 10 )
    label5.grid( row = 5, column = 1, padx = 10 )
    label6.grid( row = 6, column = 1, padx = 10 )
    e1.grid( row = 1, column = 2, padx = 10 )
    e2.grid( row = 2, column = 2, padx = 10 )
    e3.grid( row = 3, column = 2, padx = 10 )
    e4.grid( row = 4, column = 2, padx = 10 )
    e5.grid( row = 5, column = 2, padx = 10 )
    e6.grid( row = 6, column = 2, padx = 10)
    button1.grid( row = 7, column = 1, columnspan = 2)
    button2.grid( row = 8, column = 1, columnspan = 2)

    #Static Properties
    master.title('New Patient')

def third_interface():

    master = Tk()
    label1 = Label(master, text = 'Enter Patient ID', relief = 'groove', width = 40)
    label2 = Label(master, text = 'Patient Name', relief = 'groove', width = 40)
    label3 = Label(master, text = 'Height', relief = 'groove', width = 40)
    label4 = Label(master, text = 'Weight', relief = 'groove', width = 40)
    label5 = Label(master, text = 'Comments', relief = 'groove', width = 40, height = 5)
    label6 = Label(master, text = 'Patient History', relief = 'groove', width = 40, height = 10)
    

    e1 = Entry(master, relief = 'groove', width = 40)
    e2 = Entry(master, relief = 'groove', width = 40)
    e3 = Entry(master, relief = 'groove', width = 40)
    e4 = Entry(master, relief = 'groove', width = 40)
    e5 = Text(master, relief = 'groove', width = 45, height = 5, borderwidth = 2)
    e6 = Text(master, relief = 'groove', width = 45, height = 10, borderwidth = 2)

    def patient_file():
        csvfile = open('trek2.csv', 'r')
        read = csv.reader(csvfile)
        contains_keyword = False
        for row in read:
            if str(e1.get()) in row:
                contains_keyword = True
                break
        if contains_keyword:
            e6.insert("1.0", row, 'r')
        else:
            box.showinfo('Search Result','PATIENT ID NOT FOUND: SELECT NEW PATIENT')
            master.mainloop()

    def show_entry_fields():
        csvfile = open('trek2.csv', 'a')
        writer = csv.writer(csvfile)
        patients = str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get(1.0,END))
        writer.writerow(patients)
        return box.showinfo('Confirmation','Entry Confirmed. Select Clear.')
        master.mainloop()

    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(1.0,END)
        e6.delete(1.0,END)
        
            
    button1 = Button(master, text = 'Enter', relief = 'groove', width = 20, command=show_entry_fields)
    button2 = Button(master, text = 'Clear', relief = 'groove', width = 20, command=clear)
    button3 = Button(master, text = 'Patient History', relief = 'groove', width = 20, command=patient_file)


    #Geometry
    label1.grid( row = 1, column = 1, padx = 10 )
    label2.grid( row = 2, column = 1, padx = 10 )
    label3.grid( row = 3, column = 1, padx = 10 )
    label4.grid( row = 4, column = 1, padx = 10 )
    label5.grid( row = 5, column = 1, padx = 10 )
    label6.grid( row = 6, column = 1, padx = 10 )
    e1.grid( row = 1, column = 2, padx = 10 )
    e2.grid( row = 2, column = 2, padx = 10 )
    e3.grid( row = 3, column = 2, padx = 10 )
    e4.grid( row = 4, column = 2, padx = 10 )
    e5.grid( row = 5, column = 2, padx = 10 )
    e6.grid( row = 6, column = 2, padx = 10)
    button1.grid( row = 7, column = 1, columnspan = 2)
    button2.grid( row = 8, column = 1, columnspan = 2)
    button3.grid( row = 9, column = 1, columnspan = 2)


    #Static Properties
    master.title('Returning Patient')



