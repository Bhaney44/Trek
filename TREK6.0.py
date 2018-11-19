import csv
from tkinter import *
import tkinter.messagebox as box



master = Tk()

label1 = Label(master, text = 'Patient_ID', relief = 'groove', width = 40)
label2 = Label(master, text = 'Patient Info', relief = 'groove', width = 40, height = 5)

e1 = Entry(master, relief = 'groove', width = 40)
e2 = Text(master, relief = 'groove', width = 40, height = 5, borderwidth = 2)

def patient_file():
    csvfile = open('trek1.csv', 'r')
    read = csv.reader(csvfile)
    contains_keyword = False
    for row in read:
        if str(e1.get()) in row:
            contains_keyword = True
            break
    if contains_keyword:
        e2.insert("1.0", row, 'r')
    else:
        box.showinfo('Search Result','Patient ID: Not Found')
        master.mainloop()
                                       

def new_patient_file():
    second_interface()
                                 
button3 = Button(master, text = 'Retrieve File', relief = 'groove', width = 25, command=patient_file)
button4 = Button(master, text = 'New Patient', relief = 'groove', width = 25, command=new_patient_file)

label1.grid( row = 1, column = 1, padx = 10 )
label2.grid( row = 2, column = 1, padx = 10 )

e1.grid( row = 1, column = 2, padx = 10 )
e2.grid( row = 2, column = 2, padx = 10 )

button3.grid( row = 3, column = 1, columnspan = 2)
button4.grid( row = 4, column = 1, columnspan = 2)


                
#Static Properties
master.title('Trek Connect') 
    

def second_interface():
        
    master = Tk()
    label1 = Label(master, text = 'Patient ID', relief = 'groove', width = 40)
    label2 = Label(master, text = 'Patient Name', relief = 'groove', width = 40)
    label3 = Label(master, text = 'Community ID', relief = 'groove', width = 40)
    label4 = Label(master, text = 'Height', relief = 'groove', width = 40)
    label5 = Label(master, text = 'Weight', relief = 'groove', width = 40)
    label6 = Label(master, text = 'Comments', relief = 'groove', width = 40, height = 10)

    e1 = Entry(master, relief = 'groove', width = 40)
    e2 = Entry(master, relief = 'groove', width = 40)
    e3 = Entry(master, relief = 'groove', width = 40)
    e4 = Entry(master, relief = 'groove', width = 40)
    e5 = Entry(master, relief = 'groove', width = 40)
    e6 = Text(master, relief = 'groove', width = 40, height = 10, borderwidth = 2)


    def show_entry_fields():
        csvfile = open('trek1.csv', 'a')
        writer = csv.writer(csvfile)
        patients = str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get())
        writer.writerow(patients)
            

    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
            


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
    master.title('TREK')



