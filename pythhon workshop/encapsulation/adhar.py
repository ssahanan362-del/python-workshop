class Adhar:
    def __init__(self, name, adhar_no, DOB, fingerprint, retina):
        self.name = name
        self.adhar_no = adhar_no
        self.DOB = DOB
        self._fingerprint = fingerprint
        self.__retina = retina

    def getretina(self):
        return self.__retina


    def display_userData(self):
        print(f"Name: {self.name}")
        print(f"Adhar Number: {self.adhar_no}")
        print(f"DOB: {self.DOB}")
        print(f"Fingerprint: {self._fingerprint}")
        print(f"Retina : {self.__retina}")
        print(f"Retina2 : {adhar.getretina()}")



adhar = Adhar("MONTY", 123456789012, "28-05-2002", "Matched", "Verified")
adhar.display_userData()
print(adhar.getretina())
