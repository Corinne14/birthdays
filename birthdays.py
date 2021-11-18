birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
HEAD
    'Rowan Atkinson': '01/6/1955',
    'Massimo XXXXX': '02/12/1998',
    'AAA BBB': '14/03/2000'
 HEAD
>>>>>>> 149ffc5e887e67734e9848c4963aa42fc905eae1
    'Rowan Atkinson': '01/6/1955'
    'Massimo Xxxxx': '02/12/1998'
>>>>>>> main
}

    'Rowan Atkinson': '01/6/1955',
    "Corinne XXX": "14/06/1999"}
 corinne

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

