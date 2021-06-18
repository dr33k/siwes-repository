import Operations.CitizenOperations as op

citizen_dict = None

#Dashboard method. This is what the user sees
def dashboard():
    global citizen_dict
    while True:
        answer = input("Welcome, what would you like to do today? \n"
                       "\nEnter 1 to register a new citizen"
                       "\nEnter 2 update a citizen's record"
                       "\nEnter 3 to search for a citizen"
                       "\nEnter 4 to delete dead citizens"
                       "\nEnter 5 to search for citizens with a surname\n>>>")

        if(answer == "1"):
            #There was really no need for the Cititzen class since it is not serializeable and all the citizen's details are stored in a python dictionary
            citizen_object = op.create_citizen()
        elif(answer == "2"):
            update_records()
        elif(answer == "3"):
            citizen_dict = op.search_citizen(input("\nEnter the Citizen's UID: "))
            if len(citizen_dict) == 0:
                print("This citizen is not recognized")
            else:
                print("Details of citizen ")
                print(citizen_dict)
        elif(answer == "4"):
            op.delete_dead_citizens()
        elif answer == "5":
            citizen_dict = op.search_citizen_with_surname(input("\nEnter the Citizen's surname: "))
            if len(citizen_dict) == 0:
                print("No citizen with this surname")
            else:
                print(citizen_dict)

        else:
            print("Input not recognized")


#The update_records function is used by the dashboard function
def update_records():
    global citizen_dict
    while True:
        uid = input("\nEnter the Citizen's UID: ")

        #This part here uses the check number in op to check if the uid provided has any character other than numbers
        #It searches for the Citizen with the UID if it exists
        #If it doesnt exist it handles the error by itself and an error message is displayed
        citizen_dict = op.search_citizen(uid)
        if len(citizen_dict) > 0:
            while True:
                try:
                    response = input(
                                "\nEnter 1 to update first name"
                               "\nEnter 2 update last name"
                               "\nEnter 3 to update age"
                               "\nEnter 4 to update gender"
                               "\nEnter 5 to update tribe"
                                "\n Enter 6 to update state of origin"
                                "\n Enter 7 to update mobile number"
                                "\n Enter 8 to update email"
                                "\n Enter 9 to update address"
                                "\n Enter 0 to update life status\n")
                    if response == "1":
                        citizen_dict["f_name"] = op.check_string(input("\nEnter new First name "))
                        op.update(citizen_dict)
                        print("New first name is " + citizen_dict["f_name"])
                        break
                    elif response == "2":
                        citizen_dict["l_name"] = op.check_string(input("\nEnter new Last name "))
                        op.update(citizen_dict)
                        print("New last name is " + citizen_dict["l_name"])
                        break
                    elif response == "3":
                        citizen_dict["age"] = op.check_number(input("\nEnter new age "))
                        op.update(citizen_dict)
                        print("New age is " + str(citizen_dict["age"]))
                        break
                    elif response == "4":
                        citizen_dict["gender"] = op.check_string(input("\nEnter new gender "))
                        op.update(citizen_dict)
                        print("New gender is " + citizen_dict["gender"])
                        break
                    elif response == "5":
                        citizen_dict["tribe"] = op.check_string(input("\nEnter new tribe "))
                        op.update(citizen_dict)
                        print("New tribe is " + citizen_dict["tribe"])
                        break
                    elif response == "6":
                        citizen_dict["state"] = op.check_string(input("\nEnter new State of origin "))
                        op.update(citizen_dict)
                        print("New state of origin is " + citizen_dict["state"])
                        break
                    elif response == "7":
                        citizen_dict["mobile_no"] = op.check_string(input("\nEnter new Mobile number "))
                        op.update(citizen_dict)
                        print("New mobile number is " + citizen_dict["mobile_no"])
                        break
                    elif response == "8":
                        citizen_dict["email"] = op.check_string(input("\nEnter new Email address "))
                        op.update(citizen_dict)
                        print("New email is " + citizen_dict["email"])
                        break
                    elif response == "9":
                        citizen_dict["address"] = op.check_string(input("\nEnter new Address "))
                        op.update(citizen_dict)
                        print("New address is " + citizen_dict["address"])
                        break
                    elif response == "0":
                        status = input("\nEnter new Life status: 1 or 0 if Alive or Dead ")
                        if status == "0":
                            citizen_dict["life_status"] =False
                            op.update(citizen_dict)
                            print("New life status is " + str(citizen_dict["life_status"]))
                        elif status == "1":
                            citizen_dict["life_status"] =True
                            op.update(citizen_dict)
                            print("New life status is " + str(citizen_dict["life_status"]))
                        else:
                            print("Invalid input, Life status unchanged")
                        break
                    else:
                        print("\n Input not recognized")

                except TypeError as error:
                    print(error)
                    continue
        break

dashboard()
