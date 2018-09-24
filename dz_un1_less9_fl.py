#ex1:Saving progress.
#Make a function that takes personal information as arguments, e.g., name, last name, phone number, address, etc.
# Then make another function that saves the data onto a file. Make sure that it works by checking that the file
# was created and that it contains the right data.
def personal_data ():
    person_data = {'Name': '', 'Last Name': '', 'Phone number': '', 'Adress': ''}
    name = input('Please enter your name: ')
    person_data['Name'] = name
    last_name = input('Please enter your last name: ')
    person_data['Name'] = last_name
    phone_num = input('Please enter your phone number: ')
    person_data['Name'] = phone_num
    adress = input('Please enter your adress: ')
    person_data['Name'] = adress
    st_person = str(person_data)
    #print(type(st_person))

    with open('user_data.py', 'w') as user_data:
        user_data.write(st_person)

personal_data()

#Ex2: Add to the previous program a function for opening up the same file which the data was saved on.
# Make sure that it works by making the function print out the data.
def open_personal_data():
    with open('user_data.py', 'r') as user_data:
        user_info = user_data.read()
    print(user_info)

open_personal_data()