# it creates the class addressbook
from log import logging
logger = logging.getLogger()
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
        
    def display_firstname(self):
        """
        Description:
            It prints the first_name 
        Parameter:
            None
        Return:
            None
        """
        for contact in self.contacts:
            print(contact.first_name)
    
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
            
    def update_contact(self,contact):
        """
        Description:
            It finds the index of contact
        Parameter:
            contact: take multiple contact as input using class contact
        Return:
            Index
        """
        index = self.contacts.index(contact)
        return index
    
    def update_firstname(self,new_firstname,index):
        """
        Description:
            It updates the first name of contact 
        Parameter:
            new_firstname: Takes the new first name as a input
            index:  Take index as a input
        Return:
            None
        """
        self.contacts[index].first_name = new_firstname
        logger.info("Contact updated succesfully")

    def update_lastname(self,new_lastname,index):
        """
        Description:
            It updates the last name of contact 
        Parameter:
            new_lastname: Takes the new last name as a input
            index:  Take index as a input
        Return:
            None
        """
        self.contacts[index].last_name = new_lastname
        logger.info("Contact updated succesfully")

    def update_address(self,new_address,index):
        """
        Description:
            It updates the address of contact 
        Parameter:
            new_address: Takes the new address as a input
            index:  Take index as a input
        Return:
            None
        """
        self.contacts[index].address = new_address
        logger.info("Contact updated succesfully")

    def update_city(self,new_city,index):
        """
        Description:
            It updates the city of contact 
        Parameter:
            new_city: Takes the new city as a input
            index:  Take index as a input
        Return:
            None
        """
        self.contacts[index].city = new_city
        logger.info("Contact updated succesfully")

    def update_state(self,new_state,index):
        """
        Description:
            It updates the state of contact 
        Parameter:
            new_state : Takes the new state as a input
            index:  Take index as a input
        Return:
            None
        """
        self.contacts[index].state = new_state
        logger.info("Contact updated succesfully")

    def update_zipcode(self,new_zipcode,index):
        """
        Description:
            It updates the zip code of contact 
        Parameter:
            new_zipcode: Takes the new zipcode as a input
            index:  Take index as a input
        Return:
            None
        """
        self.contacts[index].zipcode = new_zipcode
        logger.info("Contact updated succesfully")

    def update_phonenumber(self,new_phonenumber,index):
        """
        Description:
            It updates the phone number of contact 
        Parameter:
            new_phonenumber: Takes the new phonenumber as a input
            index:  Take index as a input
        Return:
            None
        """
        self.contacts[index].last_name = new_phonenumber
        logger.info("Contact updated succesfully")
    
    def update_email(self,new_email):
        """
        Description:
            It updates the email of contact 
        Parameter:
            new_email: Takes the new email as a input
            index:  Take index as a input
        Return:
            None
        """
        for contact in self.contacts:
            contact.email = new_email
        logger.info("Contact updated succesfully")
    
    def remove_contact(self,contact):
        """
        Description:
            It Deletes the contact from Addressbook
        Parameter:
            contact: Takes the contact as a input
        Return:
            None
        """
        self.contacts.remove(contact)

    


         
    
    
    
