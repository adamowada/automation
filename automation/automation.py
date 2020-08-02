import re


with open('./assets/potential-contacts.txt', 'r') as mixed_contacts:
    mixed_contacts = mixed_contacts.read()
    results = re.findall(r'(\d\d\d\.\d\d\d\.\d\d\d\d|\d\d\d\-\d\d\d\-\d\d\d\d|\(\d\d\d\)\d\d\d.\d\d\d\d)', mixed_contacts, flags=re.M)
    for i in results:
        for char in i:
            cleaned_phone_numbers = open('./assets/phone_numbers.txt', 'a')
            if re.match('[0-9]', char):
                cleaned_phone_numbers.write(char)
            elif re.match(r'\(', char):
                cleaned_phone_numbers.write('')
            else:
                cleaned_phone_numbers.write('-')
            cleaned_phone_numbers.close()
        cleaned_phone_numbers = open('./assets/phone_numbers.txt', 'a')
        cleaned_phone_numbers.write('\n')
        cleaned_phone_numbers.close()

with open('./assets/phone_numbers.txt', 'r+') as unsorted:
    unsorted = list(unsorted)
    unsorted.sort()
    unsorted = list(dict.fromkeys(unsorted))
    phonebook1 = open('./assets/phone_numbers.txt', 'w')
    phonebook1.close()
    for i in unsorted:
        phonebook = open('./assets/phone_numbers.txt', 'a')
        phonebook.write(i)
        phonebook.close()
