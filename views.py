from dataclasses import asdict

from addressbook_problem.models import Addressbook, Contact, Address


class AddressbookView:
    def __init__(self):
        self.addressbook_obj = Addressbook()

    def add_contact(self):
        username = input('Enter username(only set once and cannot be change later): ')
        first_name = input('Enter First name: ')
        last_name = input('Enter last name: ')
        email = input('Enter email: ')
        phone = int(input('Enter phone: '))
        city = input('Enter city: ')
        state = input('Enter state: ')
        country = input('Enter country: ')
        address = Address(city, state, country)
        contact = Contact(username=username, first_name=first_name,
                          last_name=last_name, email=email, phone=phone, address=address)
        self.addressbook_obj.add_contact(contact)

    def get_contact_details(self):
        username = input('Enter username ')
        contact_details = self.addressbook_obj.get_contact(username)
        if contact_details is None:
            print('user not found')
            return None
        contact_dict = asdict(contact_details)
        print(contact_dict)
        return contact_details

    def update_contact(self):
        contact_detail = self.get_contact_details()
        if contact_detail is None:
            return None
        contact_dict = asdict(contact_detail)
        update_key = input('Which you want to update: ')
        if update_key == 'username':
            print('username cannot be update')
            return None
        if update_key not in contact_dict:
            print('invalid input')
            return None
        update_value = input('update data: ')
        contact_dict[update_key] = update_value
        contact_detail.dict_to_contact(**contact_dict)

    def delete_contact(self):
        username = input('Enter username')
        contact_details = self.addressbook_obj.get_contact(username)
        if contact_details is None:
            print('username not found')
            return None
        self.addressbook_obj.del_contact(username)
        print('delete successfully')
