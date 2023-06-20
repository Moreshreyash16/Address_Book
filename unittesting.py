'''
@Author: Shreyash More

@Date: 2023-06-20 15:02:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 15:02:30

@Title : Address book Unit testing

'''
import csv
import os
import json
import unittest
from addresbook import AddressBook,Contact

class TestAddressBook(unittest.TestCase):
    def setUp(self):

        self.address_book=AddressBook()
        
        self.contact1=Contact('Shreyash','More','Nandgaon','Boisar','Maharashtra','401501','122336','shreyash@')
        self.contact2=Contact("Anish","Joshi","Pokhran","Vadodara","Gujrat","401111","879511111","anish@")
        self.contact3=Contact("Rahul","Gaikwad","karad","Satara","maharashtra","4222222","89555222","rahul@")
    

    def test_add_contact(self):
        """
        Description:
            It test for adding the contacts
        Parameter:
            None
        Return:
            None
        """
        self.address_book.add_contact(self.contact1)
        self.assertEqual(len(self.address_book.contacts), 1)
        self.address_book.add_contact(self.contact2)
        self.assertEqual(len(self.address_book.contacts), 2)
        self.address_book.add_contact(self.contact3)
        self.assertNotEqual(len(self.address_book.contacts), 2)
    
    def test_display_firstname(self):
        """
        Description:
            It test for displaying first name of contacts
        Parameter:
            None
        Return:
            None
        """
        self.address_book.add_contact(self.contact1)
        self.assertEqual(self.address_book.display_firstname(),["Shreyash"])
        self.address_book.add_contact(self.contact2)
        self.assertEqual(self.address_book.display_firstname(),['Shreyash','Anish'])
        self.address_book.add_contact(self.contact3)
        self.assertEqual(self.address_book.display_firstname(),['Shreyash','Anish','Rahul'])
    
    def test_search_contact(self):
        """
        Description:
            It test for searching name of contacts
        Parameter:
            None
        Return:
            None
        """
        self.address_book.add_contact(self.contact1)
        self.assertEqual(self.address_book.search_contact("Shreyash"), self.contact1)
        self.assertNotEqual(self.address_book.search_contact("Shreyash"), self.contact2)
        
    def test_remove_contact(self):
        """
        Description:
            It test for removing contacts
        Parameter:
            None
        Return:
            None
        """
        self.address_book.add_contact(self.contact1)
        self.address_book.add_contact(self.contact2)
        self.address_book.add_contact(self.contact3)
        self.address_book.remove_contact(self.contact1)
        self.assertEqual(len(self.address_book.contacts), 2)
        self.assertNotEqual(len(self.address_book.contacts), 3)
    
    def test_update_firstname(self):
        """
        Description:
            It test for updating first name of contacts
        Parameter:
            None
        Return:
            None
        """
        self.address_book.add_contact(self.contact1)
        index=self.address_book.update_contact(self.contact1)
        self.address_book.update_firstname("SHREYASH",index)
        self.assertEqual(self.address_book.display_firstname(),['SHREYASH'])

    def test_update_lastname(self):
        """
        Description:
            It test for displaying Last name of contacts
        Parameter:
            None
        Return:
            None
        """
        self.address_book.add_contact(self.contact1)
        index=self.address_book.update_contact(self.contact1)
        self.assertEqual(self.address_book.update_lastname("MORE",index),True) 

    def test_save_txt(self):
        """
        Description:
            It test for saving the contacts in text file
        Parameter:
            None
        Return:
            None
        """
        book_name="Addresbook 1"
        file_name="sample.txt"
        self.address_book.add_contact(self.contact1)
        self.address_book.save_to_file(file_name,book_name)
        with open(file_name, 'r') as file:
                saved_data = file.read()
        expected_data =f"\nAddress Book : {book_name} \n \n  first Name : Shreyash \n  Last name :More\n  Address :Nandgaon\n  City :Boisar\n  State :Maharashtra\n  zip-code :401501\n  Phone number :122336\n  Email :shreyash@\n"
        self.assertEqual(saved_data, expected_data)
        os.remove(file_name)

    def test_save_csv(self):
        """
        Description:
            It test for saving the contacts in csv file
        Parameter:
            None
        Return:
            None
        """
        file_name="sample.csv"
        self.address_book.add_contact(self.contact1)
        self.address_book.save_to_csv(file_name)
        with open(file_name, 'r') as file:
                reader = csv.reader(file)
                saved_data = list(reader)
        expected_data = [
                ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "Phone Number", "Email"],
                ['Shreyash','More','Nandgaon','Boisar','Maharashtra','401501','122336','shreyash@'],
        ]
        self.assertEqual(saved_data, expected_data)
        os.remove(file_name)
    
    def test_save_json(self):
        """
        Description:
            It test for saving the contacts in json file
        Parameter:
            None
        Return:
            None
        """
        file_name="sample.json"
        self.address_book.add_contact(self.contact1)
        self.address_book.save_to_json(file_name)
        with open(file_name, 'r') as file:
                saved_data  = json.load(file)
                
        expected_data = [
                {
            "first_name": 'Shreyash',
            "last_name": 'More',
            "address": 'Nandgaon',
            "city": 'Boisar',
            "state": 'Maharashtra',
            "zip_code": '401501',
            "phone_number": '122336',
            "email": 'shreyash@'
        }
        ]
        self.assertEqual(saved_data, expected_data)
        os.remove(file_name)

if __name__ == '__main__':
    unittest.main()