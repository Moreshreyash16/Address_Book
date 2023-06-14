'''
@Author: Shreyash More

@Date: 2023-06-14 19:11:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-14 19:32:30

@Title : Address book uc 4 to Delete the contact

'''
from addressbook import AddressBook
from contact import Contact

def main():
    # creating the addressbook
    address_book=AddressBook()
    while(True):
        print("----Contact-Menu----")
        print("\n 1 Add Contact \n 2 Delete Contact \n 3 Display \n 4 Update Contact \n 5 Exit ")
        print("-----------------")
        try:
            choice = int(input("Enter your choice : "))
            if choice== 1 :
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                address = input("Enter address: ")
                city = input("Enter city: ")
                state = input("Enter state: ")
                zip_code = input("Enter zip code: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")

                contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                address_book.add_contact(contact)
                print("Contact added Sucessfully!!!!\n")

            elif choice== 2:
                if len(address_book.contacts)==0:
                    print("There is no contact available for Deletion,Plss Add one\n")
                else:
                    name=input("The name of your contact that you want to delete : ")
                    search=address_book.search_contact(name)
                    if search:
                        print("Are you sure you want to delete this contact? (y/n): ")
                        confirm = input("(y/n) : ")
                        if confirm.lower() == 'y':
                            address_book.remove_contact(search)
                            print("Contact deleted Sucessfully!!!!/n")
                        elif confirm.lower()=="n":
                            print("Deletion cancelled")
                        else:
                            print("Enter valid choice")
                    else:
                        print("Contact not found/n")
            elif choice == 3:
                first_name = input("Enter first name: ")
                contact = address_book.search_contact(first_name)
                if contact:
                    address_book.display(contact)
                else:
                   print("No contact found")

            elif choice == 4:
                name=input("The name of your contact that you want to edit : ")
                search=address_book.search_contact(name) 
                if search:
                    c_index=address_book.update_contact(contact)
                    while(True):
                        print("\nWhat do you want to edit ? ")
                        print("-------Update Menu-------")
                        print(" 1 First name \n 2 Last_name \n 3 Address \n 4 City  \n 5 state \n 6 zip_code \n 7 phone_number \n 8 email \n 9 Back ")
                        print("------------------")
                        try:
                            update_choice=int(input("Enter a choice : "))
                            if update_choice==1:
                                updated_fname=input("Enter a new first name : ")
                                address_book.update_firstname(updated_fname,c_index)
                            elif update_choice==2:
                                updated_lname=input("Enter a new last name : ")
                                address_book.update_lastname(updated_lname,c_index)
                            elif update_choice==3:
                                updated_address=input("Enter a new Address : ")
                                address_book.update_address(updated_address,c_index)
                            elif update_choice==4:
                                updated_city=input("Enter a new city : ")
                                address_book.update_city(updated_city,c_index)
                            elif update_choice==5:
                                updated_state=input("Enter a new state : ")
                                address_book.update_state(updated_state,c_index)
                            elif update_choice==6:
                                updated_zip=int(input("Enter a new pincode : "))
                                address_book.update_zipcode(updated_zip,c_index)
                            elif update_choice==7:
                                updated_phone=int(input("Enter a new Phone number : "))
                                address_book.update_phonenumber(updated_phone,c_index)
                            elif update_choice==8:
                                updated_email=input("Enter a new Email : ")
                                address_book.update_email(updated_email,c_index)
                            elif update_choice==9:
                                break
                            else:
                                print("Enter valid choice")    
                        except:
                            print("Enter a integer")
                else:
                    print("Name not found\n")
            elif choice == 5:
                break
            else:
                print("Enter a valid number!!!\n")
        except ValueError:
            print("Enter a integer!!!")


if __name__ == "__main__":
    main()
