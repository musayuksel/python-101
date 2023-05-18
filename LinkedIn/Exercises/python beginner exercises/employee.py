# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a .  in between, and follow it with @and.digital at the end. Make sure the entire email is in lowercase.

class Employee:
    def __init__(self,firstname,lastname):
        self.fullname = firstname + " " + lastname
        self.email = firstname.lower() + "." + lastname.lower() + "@and.digital"

    def employee_info(self):
        return "Fullname: {} \nEmail: {}".format(self.fullname,self.email)




emp1 = Employee("Musa","Yuksel")
print(emp1.employee_info())
