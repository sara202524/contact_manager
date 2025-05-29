import re


def contact_validator(contact):
    errors = []
    if not (type(contact[0]) == int and contact[0]>0):
        errors.append('contact ID must be an integer > 0')

    if not (type(contact[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", contact[1])):
        errors.append('contact Name is Invalid')


    if not (type(contact[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", contact[2])):
        errors.append('contact Family is Invalid')

    if not (type(contact[3]) == int and contact[3]>0):
        errors.append('contact number Amount must be an integer > 0')

    if not (type(contact[4]) == str and re.match(r"^[a-zA-Z\s]{3,70}$", contact[4])):
            errors.append('contact address is Invalid')

    if not (type(contact[5]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", contact[5])):
        errors.append('contact title is Invalid')

    return errors
