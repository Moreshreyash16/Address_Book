# it creates the class addressbook
class AddressBook:
    def __init__(self):
        self.contacts = []

def add_contact(self, contact):
    """
    Description:
        It adds contact 
    Parameter:
        contact: take multiple contact as input using class contact
    Return:
        None
    """
    self.contacts.append(contact)
    print("Contact added successfully.")

def display (self,contact):
        """
    Description:
        It display contact 
    Parameter:
        contact: take multiple contact as input using class contact
    Return:
        None
    """
        print("Contact Found:")
        print("First Name: ", contact.first_name)
        print("Last Name: ", contact.last_name)
        print("Address: ", contact.address)
        print("City: ", contact.city)
        print("State: ", contact.state)
        print("Pin code: ", contact.zip_code)
        print("Phone Number: ", contact.phone_number)
        print("Email: ", contact.email)
    
def search_contact(self, first_name):
    """
    Description:
        It searchs the contact 
    Parameter:
        contact: take multiple contact as input using class contact
    Return:
        contact
    """
    for contact in self.contacts:
        if contact.first_name == first_name:
            return contact
         
    
    
    


         
    
    
    
