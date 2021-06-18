import json
from Citizen import Citizen


records = dict()


def create_citizen():
    citizen = dict()
    while True:
        print("\nCreate New Citizen")
        try:
            citizen["f_name"] = check_string(input("Enter first name "))
            citizen["l_name"] = check_string(input("Enter last name "))
            citizen["age"] = check_number(input("Enter age "))
            citizen["gender"] = check_gender(input("Enter gender "))
            citizen["email"] = check_email(input("Enter functional email "))
            citizen["tribe"] = check_string(input("What tribe are you: "))
            citizen["state"] = check_string(input("What Nigerian state are you from: "))
            citizen["mobile_no"] = check_phone_no(input("Enter working mobile number: "))
            citizen["address"] = input("Where do you live: ").strip("\"")
            citizen["life_status"] = True
            break
        except TypeError as error:
            print(str(error)+", try again")
            continue
        except ValueError as error:
            print(str(error)+", try again")
            continue

    a_citizen = Citizen(citizen["f_name"], citizen["l_name"], citizen["age"], citizen["gender"], citizen["mobile_no"],
    citizen["email"], citizen["address"], citizen["tribe"], citizen["state"])

    citizen["uid"] = a_citizen.get_UID()

    load()

    dump({citizen["uid"]:citizen})
    print("New citizen with UID "+ str(a_citizen.get_UID())+" created successfully")
    return citizen

def search_citizen(uid):
    global records
    cit = tuple()
    try:
        if (str(check_number(uid)) == uid):
            load()
            cit = tuple(records[key] for key in records if key == uid)

    except TypeError as error:
        print(error)
        return tuple()
    else:
        return cit[0]

def search_citizen_with_surname(surname):
    global records
    tuple_of_citizens = tuple()
    try:
        if (check_string(surname)  == surname):
            load()
            tuple_of_citizens = tuple(records[key] for key in records if records[key]["l_name"] == surname)

    except TypeError as error:
        print(error)
        return tuple()
    else:
        return tuple_of_citizens

def delete_dead_citizens():
    load()
    global records
    list_of_keys_to_be_deleted = list()

    for key in records:
        if str(records[key]["life_status"] )== "False":
            list_of_keys_to_be_deleted.append(key)

    for i in list_of_keys_to_be_deleted:
        records.pop(i)

    print("\nDead citizens deleted")

#The load and dump methods provide access to the json database
#They fetch and persist information respectively
def load():
    global records
    file = open("db/citizen_records.json", "r")
    records = json.load(file)
    file.close()

def dump(dictionary):
    global records
    load()
    file = open("db/citizen_records.json","w")
    records.update(dictionary)
    json.dump(records,file)
    file.close()

def update(dictionary):
    global records
    load()
    file = open("db/citizen_records.json", "w")
    records[dictionary["uid"]] = dictionary
    json.dump(records, file)
    file.close()

#All the check methods here provide validation for the different input fields
#They take in an input and raise a type errror if the requirements for that input are satisfied
#Else they return the input

def check_string(name):
    if len(name) < 2:
        raise TypeError("This field should have at least 2 letters")

    rejects = ["0","1","2","3","4","5","6","7","8","9","0",",","@","!","#","$","&","*","(",")","+","=","/","\"","\'",
               ":",";","{","}","[","]"]
    rejected = [x for x in name if x in rejects]
    if len(rejected) != 0:
        raise TypeError("This field shouldnt contain these " + str(rejected))
    return name

def check_email(email):
    if len(email) < 5:
        raise TypeError("This field should have at least 5 characters")

    rejects = ["/","*","+","=","(",")","{","}","[","]",";","\"","\'",]
    rejected = [x for x in email if x in rejects]
    if len(rejected) != 0:
        raise TypeError("your email shouldnt contain these "+str(rejected))
    return email

def check_number(number):
    number = str(number)
    allows = ["1","2","3","4","5","6","7","8","9","0"]
    rejected = [x for x in number if x not in allows]
    if len(rejected) != 0:
        raise TypeError("This field should not contain these  " + str(rejected))
    return int(number)

def check_phone_no(number_string):
    allows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+","-"]
    rejected = [x for x in number_string if x not in allows]
    if len(rejected) != 0:
        raise TypeError("This field should not contain these  " + str(rejected))
    return number_string

def check_gender(gender):
    gender = gender.lower()
    allowed = ["male","female"]
    if gender not in allowed:
        raise ValueError("Incorrect gender")
    return gender
