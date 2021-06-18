import random
import time
class Citizen:
    def __init__(self, f_name,l_name, age,gender, mobile_no, email, address, tribe, state):
        self.__UID = str(int(time.mktime(time.gmtime())))
        self.__f_name = f_name
        self.__l_name = l_name
        self.__age = age
        self.__gender = gender
        self.__mobile_no = mobile_no
        self.__email = email
        self.__address = address
        self.__tribe = tribe
        self.__state = state
        self.__alive = True

    def get_f_name(self):
        return self.__f_name

    def get_l_name(self):
        return self.__l_name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_mobile_no(self):
        return self.__mobile_no

    def get_address(self):
        return self.__address

    def get_tribe(self):
        return self.__tribe

    def get_state(self):
        return self.__state

    def get_UID(self):
        return self.__UID

    def is_alive(self):
        return self.__alive

    def set_f_name(self,f_name):
        self.__f_name = f_name

    def set_l_name(self,l_name):
        self.__l_name = l_name

    def set_age(self,age):
        self.__age = age

    def set_gender(self,gender):
        self.__gender = gender

    def set_address(self,address):
        self.__address = address

    def set_tribe(self,tribe):
        self.__tribe = tribe

    def set_state(self,state):
        self.__state = state

    def set_alive(self,alive):
        self.__alive = alive

    def set_mobile_no(self,mb):
        self.__mobile_no = mb