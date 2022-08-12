""" this example will demonstrate nesting data in a python dictionary """

import datetime

def get_person_data():
    """ ask the user for information on a person. """
    fields = ['first name', 'last name', 'office', 'age']
    person_data = {}
    print('Enter a blank line to end')
    for field in fields:
        answer = input(field.title() + ': ')
        if answer == '':
            return person_data
        person_data[field] = answer
    return person_data


def print_current_status(persons):
    """ this is probably a temporary function.  it prints out what we have
    currently collected in the persons dict. """
    for timestamp, data in persons.items():
        try:
            print(f'{timestamp}:')
            if age not in data:
                print("couldn't find age field")
            for field in data:
                print(f'\t{field}: {data[field]}')
        except (NameError,KeyError) as err:
            print(f'for some reason, we could not find the {err} field')


def main():
    persons = {}
    flag = True
    while(flag):
        person_data = get_person_data()
        if person_data:
            timestamp = str(datetime.datetime.now())
            persons[timestamp] = person_data
        else:
            flag = False
    # TODO: now do something cool with person data
    print_current_status(persons)

if __name__ == '__main__':
    main()
