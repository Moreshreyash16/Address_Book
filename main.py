'''
@Author: Shreyash More

@Date: 2023-06-16 20:03:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-16 20:03:30

@Title : Address book uc 14 to save and view AddressBook to a csv file

'''
from addressbook import AddressBook,Contact
from log import logging
import os 

def main():
    logger = logging.getLogger()
    address_books={}
    while True:
        print("\n-------Addressbook-------")
        print(" 1 Add AddressBook \n 2 Update AddressBook \n 3 Display \n 4 Display All contact \n 5 Delete Adressbook \n 6 Sort \n 7 View Addresbook \n 8 Exit" )
        print("--------------------------")
        try:
            choice = int(input("Enter your choice : "))
            if choice ==1:
                name=input("Enter a name of new Address Book : ")
                if name=="":
                    print("Enter a valid name")
                elif name not in address_books:
                    address_books[name]=AddressBook()
                    logger.info("Address book created Succesfully")
                else:
                    logger.info("This name already exist plss choose another name")
            elif choice == 2:
                if len(address_books)==0:
                    logger.info("first Create a Addressbook to update it !!! ")
                    
                else:
                    name=input("Enter a name of Address Book : ")
                    if name in address_books:
                        current_address_book = address_books[name]
                    else:
                        print("Address book not found! \n")
                        continue
                    while(True):
                        print("----Contact-Menu----")
                        print("\n 1 Add Contact \n 2 Delete contact \n 3 Update Contact \n 4 Display \n 5 Back\n")
                        print("-----------------")
                        try:
                            sub_choice = int(input("Enter your choice : "))
                            if sub_choice==1 :
                                first_name = input("\nEnter first name: ")
                                if current_address_book.search_contact(first_name):
                                    logger.info(" This is name already exits please enter a new name!!! \n")
                                else:
                                    last_name = input("Enter last name: ")
                                    address = input("Enter address: ")
                                    city = input("Enter city: ")
                                    state = input("Enter state: ")
                                    zip_code = input("Enter zip code: ")
                                    phone_number = input("Enter phone number: ")
                                    email = input("Enter email: ")

                                    if first_name and last_name and address and city and state and zip_code and email !="":
                                        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                                        current_address_book.add_contact(contact)
                                        logger.info("Contact added Sucessfully!!!!")
                                    else:
                                        print("Enter a valid input")

                            elif sub_choice==2:
                                if len(current_address_book.contacts)==0:
                                    logger.info("No contact available,Please add contact first\n")
                                
                                else:
                                    name=input("The name of your contact that you want to delete : ")
                                    search=current_address_book.search_contact(name)
                                    if search:
                                        logger.warning("Are you sure you want to delete this contact? (y/n): ")
                                        confirm = input("(y/n) : ")
                                        if confirm.lower() == 'y':
                                            current_address_book.remove_contact(search)
                                            logger.info("Contact deleted Sucessfully!!!!")
                                        elif confirm.lower()=="n":
                                            logger.info("Deletion cancelled")
                                        else:
                                            logger.info("Enter valid choice")
                                    else:
                                        logger.info("Contact not found")

                            elif sub_choice==3:
                                name=input("The name of your contact that you want to edit : ")
                                search=current_address_book.search_contact(name) 
                                if search:
                                    c_index=current_address_book.update_contact(search)
                                    while(True):
                                        print("What do you want to edit ? ")
                                        print("\n----Editing Menu-----")
                                        print(" 1 First name \n 2 Last_name \n 3 Address \n 4 City  \n 5 state \n 6 zip_code \n 7 phone_number \n 8 email \n 9 Back ")
                                        print("-------------------")
                                        try:
                                            update_choice=int(input("Enter a choice : "))
                                            if update_choice==1:
                                                updated_fname=input("Enter a new first name : ")
                                                current_address_book.update_firstname(updated_fname,c_index)
                                            elif update_choice==2:
                                                updated_lname=input("Enter a new last name : ")
                                                current_address_book.update_lastname(updated_lname,c_index)
                                            elif update_choice==3:
                                                updated_address=input("Enter a new Address : ")
                                                current_address_book.update_address(updated_address,c_index)
                                            elif update_choice==4:
                                                updated_city=input("Enter a new city : ")
                                                current_address_book.update_city(updated_city,c_index)
                                            elif update_choice==5:
                                                updated_state=input("Enter a new state : ")
                                                current_address_book.update_state(updated_state,c_index)
                                            elif update_choice==6:
                                                updated_zip=int(input("Enter a new pincode : "))
                                                current_address_book.update_zipcode(updated_zip,c_index)
                                            elif update_choice==7:
                                                updated_phone=int(input("Enter a new Phone number : "))
                                                current_address_book.update_phonenumber(updated_phone,c_index)
                                            elif update_choice==8:
                                                updated_email=input("Enter a new Email : ")
                                                current_address_book.update_email(updated_email,c_index)
                                            elif update_choice==9:
                                                break
                                            else:
                                                print("Enter valid choice")    
                                        except:
                                            logger.error("Enter a integer")
                                else:
                                        print("name not found")
                            elif sub_choice == 4:
                                first_name = input("Enter first name: ")
                                contact = current_address_book.search_contact(first_name)
                                if contact:
                                    current_address_book.display(contact)
                                else:
                                    logger.info("no contact found")

                            elif sub_choice == 5:
                                break
                            else:
                                logger.info("Enter a valid number!!!\n")
                        except ValueError:
                            logger.error("Enter a integer!!!")
            elif choice==3:
                if len(address_books)>0:
                    no=1
                    print("The books that are present are ")
                    for key,value in address_books.items():
                        print(f"{no}.{key}")
                        no+=1
                else:
                    logger.info("No Addressbook present plss create one!!!!!\n")
            elif choice==4:
                if address_books.keys():
                    no=1
                    for key,value in address_books.items():
                        print(f"Address book :{no}.{key}")
                        contacts=value.display_firstname()
                        no+=1
                        contacts =sorted(contacts)
                        for i in range(len(contacts)):
                            print(f" {i+1}.{contacts[i]}")
                else:
                    logger.info(" No contacts found \n")

            elif choice==5:
                name=input("The name of your Adressbook that you want to delete : ")
                if name in address_books.keys():
                    logger.warning("Are you sure you want to delete this contact? (y/n): ")
                    confirm = input("(y/n) : ")
                    if confirm.lower() == 'y':
                        del address_books[name]
                        logger.info("Addressbook Deleted Successfully")        
                    elif confirm.lower()=="n":
                        logger.info("Deletion cancelled")
                    else:
                        logger.info("Enter valid choice")
                else:
                    logger.info("Contact not found")
            
            elif choice==6:
                print("-----Sort Menu------")
                print(" 1 Sort by State \n 2 Sort by City")
                print("--------------------")
                try:
                    user_choice=int(input("Enter choice: "))
                    if user_choice==1:
                        for key,value in address_books.items():
                            print(value.search_by_place(user_choice))
                    elif user_choice==2:
                        for key,value in address_books.items():
                            print(value.search_by_place(user_choice))
                    else:
                        logger.info("Enter a valid number")
                except ValueError :
                    logger.error("Please Enter a integer")
            elif choice==7:
                try:
                    print("\n------- File Menu -------")
                    print("1 View \n2 Save to txt \n3 Save to csv")
                    print("----------------------------")
                    view_choice=int(input("Enter choice :"))
                    filename=(input("Enter a filename : "))              
                    if view_choice==1:
                        try:
                            with open(filename, 'r') as file:
                                print("Address Book File Contents:")
                                print(file.read())
                        except:
                            print(f"{filename} not found")
                    elif view_choice==2:
                        if current_address_book:
                            for key,value in address_books.items():
                                current_address_book.save_to_file(filename,key)
                            logger.info("file saved successfully!!")
                    
                    elif view_choice==3:
                        if current_address_book:
                            for key,value in address_books.items():
                                current_address_book.save_to_file(filename,key)
                            logger.info("file saved successfully!!")
                    else:
                        print("Enter valid number")
                except:
                    print("Plss add contact or Addressbook ") 
                        
            elif choice==8:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError :
            logger.error("Please Enter a integer")


if __name__ == "__main__":
    main()

