class SSN:
    def __init__(self, ssn):
        self.mSSN = ssn
    
    def setSSN(self, ssn):
        self.mSSN = ssn
        
    def getSSN(self):
        return self.mSSN
    
    def __eq__(self, student):
        if (self.mSSN == student.getSSN()):
            return True
        else:
            return False