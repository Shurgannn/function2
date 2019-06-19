class Contact:

    def __init__(self, first_name, last_name, phone_number, favorite_contact=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite_contact = favorite_contact
        self.num = args
        self.social_networks = kwargs

    def __str__(self):
        def func_favorite_contact():
            if self.favorite_contact == False:
                return f'В избранных: нет'
            else:
                return f'В избранных: {self.favorite_contact}'

        def func_social_networks():
            stri = ''
            for k, v in self.social_networks.items():
                stri += f'        {k} : {v}\n'
            return stri

        return f'Имя: {self.first_name}\n' \
            f'Фамилия: {self.last_name}\n' \
            f'Телефон: {self.phone_number}\n' \
            f'{func_favorite_contact()}\n' \
            f'Дополнительная информация:\n' \
            f'{func_social_networks()}'


class PhoneBook(Contact):
    contact_list = []

    def __init__(self, name):
        super(Contact, self).__init__()
        self.name = name

    def print_contacts(self):
        count = 0
        for item in self.contact_list:
            count += 1
            print(f'{count} контакт телефонной книги {self.name} :\n{item}')

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def remove_contact(self, remove_tel_number):
        for contact in self.contact_list:
            if contact.phone_number == remove_tel_number:
                self.contact_list.remove(contact)

    def search_favorite_contacts(self):
        for contact in self.contact_list:
            if contact.favorite_contact != False:
                print(contact.favorite_contact)

    def search_contact(self, first_name1, last_name1):
        for contact in self.contact_list:
            if first_name1 == contact.first_name and last_name1 == contact.last_name:
                print(contact)


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    jon = Contact('Jon', 'Smi', '+71876567809', '99999999999999', telegram='@jy', email='jy@smi.com')
    print(jhon)
    my_phonebook = PhoneBook('my phone book')
    my_phonebook.add_contact(jon)
    my_phonebook.add_contact(jhon)
    my_phonebook.print_contacts()
    my_phonebook.remove_contact('+71876567809')
    my_phonebook.print_contacts()
    my_phonebook.search_favorite_contacts()
    my_phonebook.search_contact('Jhon', 'Smith')
