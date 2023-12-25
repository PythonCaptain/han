from tkinter import *
import backend

#------------------------- Config ------------------------
widnow = Tk()



#___________Methods______________

def select_all():
    connection = backend.check_connection()
    listTuple = backend.select_all_table(connection)
    

    for rowTuple in listTuple:
        for column in rowTuple:
            print(column,end=" - ")
        print()

def insert_tbl_shop():
    connection = backend.check_connection()
    name = input("enter name : ")
    price = input("enter price : ")
    star = input("enter star : ")
    garanty = input("enter garanty : ")
    backend.insert_into_table_shop(connection,name,price,star,garanty)

def search_tbl_shop():
    connection = backend.check_connection()
    
    name = input("enter your name to search : ")
    resultSearch = backend.search_into_table_shop(connection,name)
    print(resultSearch)

#------------------------- Label ------------------------

nameLabel = Label(widnow,text="name")
nameLabel.grid(row=0,column=0)

priceLabel = Label(widnow,text="price")
priceLabel.grid(row=0,column=2)

starLabel = Label(widnow,text="star")
starLabel.grid(row=1,column=0)

garantyLabel = Label(widnow,text="garanty")
garantyLabel.grid(row=1,column=2)


#------------------------- Entry ------------------------

nameEntry = Entry(widnow)
nameEntry.grid(row=0,column=1)

priceEntry = Entry(widnow)
priceEntry.grid(row=0,column=3)

starEntry = Entry(widnow)
starEntry.grid(row=1,column=1)

garantyEntry = Entry(widnow)
garantyEntry.grid(row=1,column=3)


#------------------------- ListBox ------------------------

pythonListBox = Listbox(widnow,width=40,height=7)
pythonListBox.grid(row=2,column=0,rowspan=3,columnspan=2)

#------------------------- ScrollBar ------------------------

pythonScrollbar = Scrollbar(widnow)
pythonScrollbar.grid(row=2,column=2,rowspan=3)

#------------------------- ScrollBar ------------------------
pythonListBox.configure(yscrollcommand=pythonScrollbar.set)
pythonScrollbar.configure(command=pythonListBox.yview)

#-------------------------- Button ------------------------

selectButton = Button(widnow,text="select",command=select_all)
selectButton.grid(row=2,column=3)

insertButton = Button(widnow,text="insert",command=insert_tbl_shop)
insertButton.grid(row=3,column=3)

updateButton = Button(widnow,text="update",command=select_all)
updateButton.grid(row=4,column=3)

deleteButton = Button(widnow,text="delete",command=insert_tbl_shop)
deleteButton.grid(row=5,column=3)

searchButton = Button(widnow,text="search",command=select_all)
searchButton.grid(row=6,column=3)

clearButton = Button(widnow,text="clear",command=insert_tbl_shop)
clearButton.grid(row=7,column=3)

exitButton = Button(widnow,text="exit",command=insert_tbl_shop)
exitButton.grid(row=8,column=3)

widnow.mainloop()

