'''
@Author: Shreyash More

@Date: 2023-06-14 15:11:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-14 15:11:30

@Title : Address book uc 1 to create a addressbook

'''
from addressbook import AddressBook
from contact import Contact

def main():
    # creating the addressbook
    address_book=AddressBook()
    while(True):
        print("----*Contact-Menu*----")
        print("\n 1 Add Contact \n 2 Display \n 3 Exit ")
        print("--------xxx-------")
        try:
            choice = int(input("Enter your choice : "))
            if choice==1 :
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
                print("Contact added Sucessfully!!!!")

            elif choice == 2:
                first_name = input("Enter first name: ")
                contact = address_book.search_contact(first_name)
                if contact:
                    address_book.display(contact)
                else:
                   print("no contact found")

            elif choice ==3:
                break
            else:
                print("Enter a valid number!!!\n")
        except ValueError:
            print("Enter a integer!!!")
                     
if __name__ == "__main__":
    main()
