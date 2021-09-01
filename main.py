class Library:
           
    def __init__(self, libname, booklist):
        self.libraryname = libname
        self.booklist = booklist
        self.lenddict = {}
        self.donatedict = {}

    def lend(self, name_of_person, index_of_book):
        
        if name_of_person in self.lenddict.keys():
            print(f"Before lending a new book, return the previous one - ({name_of_person} has already lended {self.lenddict[name_of_person]})")
        
        else:
            name_of_book = self.booklist[index_of_book-1]
            print(f"{name_of_book} successfully lended to {name_of_person}")
            self.lenddict.update({name_of_person : name_of_book})

            self.booklist.remove(name_of_book)

    def donate(self, name_of_donater, donated_book):
        
        if name_of_donater in self.donatedict:
            temp = self.donatedict[name_of_donater]
            self.donatedict.__delitem__(name_of_donater)
            temp2 = f"{temp}, {donated_book}"
            self.donatedict.update({name_of_donater : temp2})
            self.booklist.append(donated_book)
            print(f"{name_of_donater}, Thanks for donating - {donated_book}")

        else:
            print(f"{name_of_donater}, Thanks for donating - {donated_book}")
            self.donatedict.update({name_of_donater : donated_book})
            self.booklist.append(donated_book)

    def returnbook(self, name_of_person):
        
        if name_of_person in self.lenddict.keys():
            
            if input(f"Do you want to return {self.lenddict[name_of_person]}  y/n?\n").lower() == "y":
                                 
                print("Book returned successfully")
                self.booklist.append(self.lenddict[name_of_person])
                self.lenddict.__delitem__(name_of_person)

            else:
                print(f"No problem! Please return it when you have finished reading it!")
                
        else:
            print("entered username has not lended a book from our library")

    def show_books(self):
        
        print(f"WELCOME TO {str(self.libraryname).upper()}\nWe have the following books-\n")

        for index, book in enumerate(self.booklist):
            print(f"{index + 1} - {book}")
        print("\n")

    def view_donators(self):
        print(self.libraryname, "thanks --\n",)
        for key, value in self.donatedict.items():
            print(key,"for donating - ", value)

if __name__ == '__main__':
    list_of_books1 = ["Pinnochio", "Harry Potter And The Goblet Of Fire", "Harry Potter And The Deathly Hallows ", "The Adventures Of Tom Sawyer", "Black Beauty", "Da Vinci Code"]
    list_of_books2 = ["Famous Five", "The Happy Prince", "Story of Finn", "Physics - 1", "Physics - 2"]
    
    ssn_lib = Library("SSN LIBRARY", list_of_books1)
    london_lib = Library("Library Of London", list_of_books2)
    lib_list = [ssn_lib, london_lib]
    
    while True: # MAIN MENU 
            print("CHOOSE A LIBRARY\n")
            for i, j in enumerate(lib_list):
                print(f"Enter {i+1} for {j.libraryname}")
            print("Enter \"new\" for making a new library\n")
            print("Enter \"EXIT\" to quit\n")
            
            
            inp = input("Input:\n")
            if inp.lower() == "exit":
                print("\nexiting...")
                break
            
            if inp.lower() == "new": # CREATE A NEW LIBRARY
                name = input("Enter name of library:\n")
                blist = []      
                print("Enter Name Of Books, Give Blank Input To Exit")          
                while True:
                    x = input()
                    if x != "":
                        blist.append(x)
                    else:
                        break
                lib_list.append(Library(name, blist))
                continue
            
            elif inp.isnumeric():
                lib = lib_list[int(inp) - 1]        
                print("\n\n")
                print("WELCOME TO ", lib.libraryname)
                
            while True: # MAIN LOOP
                
                try:            
                    ctrlvar = int(input("\nENTER (1, 2, 3, 4, 5, 6)--\n1 -- SEE LIST OF ALL AVAILABLE BOOKS\n2 -- LENDING A BOOK\n3 -- RETURNING A LENDED BOOK\n4 -- DONATING A BOOK\n5 -- VIEWING DONATORS\n6 -- EXIT \n\n"))
                        
                    if ctrlvar == 1:
                        lib.show_books()
                        
                    elif ctrlvar == 2:
                        lendname = input("Enter Your Name\n")
                        lendbook = int(input("Enter The Index Of The Book You Want To Lend\n"))
                        
                        lib.lend(lendname, lendbook)
                    
                    elif ctrlvar == 3:
                        returnname = input("Enter Your Name\n")

                        lib.returnbook(returnname)
                        
                    elif ctrlvar == 4:
                        donatename = input("Enter Your Name\n")
                        donatebook = input("Enter The Name Of The Book You Want To Donate\n")
                        
                        lib.donate(donatename, donatebook)
                    
                    elif ctrlvar == 5:
                        lib.view_donators()
                    
                    elif ctrlvar == 6:
                        print("Exiting...")
                        break
                    
                    else:
                        print("Enter a valid option 1,2,3,4,5,6")
                
                except Exception as e:
                    print("Error!")
                    print("Enter a valid choice")
            

