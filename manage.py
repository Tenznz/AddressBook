from addressbook_problem.views import AddressbookView


def main():
    address_view = AddressbookView()
    print('''
    =================================================
    ==============    AddressBook    ================
    =================================================
        ''')
    while True:
        user_input = input('''Enter the following choice
                1)Add contact
                2)Update contact
                3)Get contact details
                4)Delete contact
            ''')
        choice = {
            '1': address_view.add_contact,
            '2': address_view.update_contact,
            '3': address_view.get_contact_details,
            '4': address_view.delete_contact
        }
        choice.get(user_input, None)()
        print('========================================')


if __name__ == '__main__':
    # addrs = Address('Banglore', 'India')
    # con = Contact(first_name='Ten', last_name='Duk', phone=123456789, email='dhugkar@gmail.com', address=addrs)
    # addrs_book_obj = Addressbook({con.first_name: con})
    # print(addrs_book_obj.get_contact(con).phone)
    main()