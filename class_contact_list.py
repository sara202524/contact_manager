from validator import contact_validator


class ContactList :
    def __init__(self, name, family , phone_number , address ,title):
        self.name=name
        self.family=family
        self.phone_number=phone_number
        self.address=address
        self.title=title


    def save(self):
        print(self.name+' '+self.family+' '+'saved')




    def find_by_family(self):
        print(f'{self.name}-{self.family}''found')



    def validator (self):
        return contact_validator(self)




