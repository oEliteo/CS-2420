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
    
    def __int__(self):
        self_as_int = int(elf.mSSN.replace("-", ''))
        return self_as_int