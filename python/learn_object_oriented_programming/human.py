from __future__ import division
import time, datetime, decimal
class Human():
    # Human simulates a person for Kai's example,
    #  or one of God's jokes.

    def __init__(self, birthdate, firstname, middlename, lastname, ethnicity, height):
        self.birthdate = birthdate
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.ethnicity = ethnicity
        self.height = height

    def get_firstname(self):
        print self.firstname

    def get_lastname(self):
        print self.lastname

    def get_fullname(self):
        print self.firstname + " " + self.middlename + " " + self.lastname

    def get_birthdate(self):
        print "I was born on" + " " + self.birthdate + "!"

    def get_age(self):
        today = datetime.date.today()
        birthdate = datetime.datetime.strptime(self.birthdate, "%Y-%m-%d")
        years = today.year - birthdate.year
        print "I am currently " + str(years) + " old."

    def get_height(self, format):
        # print "Format: " + str(format)
        if format == "m":
            height = str(self.height/100)
            print "I am " +height+ " meters."
        elif format == "in":
            remainder_height = str(182.88 % 2.54)
            remainder_height = remainder_height[:1]
            height = str(self.height/2.54) + remainder_height
            print "I am "+ height + " inches."
        elif format == "cm":
            print "I am " + str(self.height) + " centimeters."
        elif format == "ft":
            remainder_height = str(182.88 % 30.48)
            remainder_height = remainder_height[:1]
            height = str(self.height/30.48) + remainder_height
            print "I am " +height+ " feet."
        else:
            print "You need to choose a format [m , cm, in, or ft] "

    def get_ethnicity(self):
        print self.ethnicity

suraya = Human("1994-04-22", "Suraya", "Ashley", "Bradshaw", "White/Asian", 152.4)
suraya.get_firstname()
suraya.get_lastname()
suraya.get_fullname()
suraya.get_birthdate()
suraya.get_age()
suraya.get_height("m")
suraya.get_height("cm")
suraya.get_height("in")
suraya.get_height("ft")
suraya.get_ethnicity()
print "\n"
kai = Human("1993-07-20", "Kai", "Arthur", "Prout", "White/Pacific/African", 199.39)
kai.get_firstname()
kai.get_lastname()
kai.get_fullname()
kai.get_birthdate()
kai.get_age()
kai.get_height("m")
kai.get_height("cm")
kai.get_height("in")
kai.get_height("ft")
kai.get_ethnicity()
