class Student():
    def __init__(self):
        self.mLastName = ''
        self.mFirstName = ''
        self.mSSN = ''
        self.mEmail = ''
        self.mAge = ''
        
    def setLastName(self, name):
        self.mLastName = name
    
    def setFirstName(self, name):
        self.mFirstName = name
        
    def setSSN(self, ssn):
        self.mSSN = ssn
        
    def setEmail(self, email):
        self.mEmail = email
        
    def setAge(self, age):
        self.mAge = age
        
    def getLastName(self):
        return self.mLastName
    
    def getFirstName(self):
        return self.mFirstName
    
    def getSSN(self):
        return self.mSSN
    
    def getEmail(self):
        return self.mEmail
    
    def getAge(self):
        return self.mAge
    
    def setMembers(self, lastName, firstName, ssn, email, age):
        self.setLastName(lastName)
        self.setFirstName(firstName)
        self.setSSN(ssn)
        self.setEmail(email)
        self.setAge(age)
        
    def __eq__(self, rhs):
        if self.getSSN() == rhs.getSSN():
            return True
        else:
            return False
        
    def __lt__(self, rhs):
        num1 = self.getSSN().strip("-")
        num2 = rhs.getSSN().strip("-")
        if(num1 < num2):
            return True
        else:
            return False
        
    def __gt__(self, rhs):
        num1 = self.getSSN().strip("-")
        num2 = rhs.getSSN().strip("-")
        if(num1 > num2):
            return True
        else:
            return False
    
    def __int__(self):
        self_as_int = self.getSSN().strip("-")
        return self_as_int
            
    