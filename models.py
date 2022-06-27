from dataclasses import dataclass, make_dataclass, field, asdict
from typing import Optional, Union

# Address = make_dataclass('Address', [
# ('city', str, field(init=False)), ('state', str, field(init=False)), ('country', str, field(init=False))
# ('city', str, None), ('state', str,None), ('country', str, None)
# ])

from uuid import uuid4


@dataclass
class Address:
    # id: uuid4
    city: Optional[str] = field(default=None)
    state: Optional[str] = field(default=None)
    country: Optional[str] = field(default=None)


@dataclass
class Contact:
    # id: uuid4
    username: str
    first_name: str
    last_name: str
    phone: int
    email: str
    address: Address

    def dict_to_contact(self, **kwargs):
        self.username = kwargs.get('username')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.phone = kwargs.get('phone')
        self.email = kwargs.get('email')
        self.address = kwargs.get('address')


class Addressbook:
    def __init__(self):
        self.contacts: dict = {}

    def add_contact(self, contact: Contact):
        """
        adding contact object to contacts dictionary
        :param contact: contact instance
        :return: None
        """
        self.contacts.update({contact.username: contact})

    def del_contact(self, username: str):
        """
        deleting contact data from contacts dictionary
        :param username: key (username)
        :return: None
        """
        self.contacts.pop(username)

    def get_contact(self, username: str):
        """
        retrieve contact details from contacts dictionary
        :param username:  key (username)
        :return: contacts dictionary
        """
        return self.contacts.get(username,None)
