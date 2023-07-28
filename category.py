class Category:
    def __init__(self, category, vendor):
        self.category = category
        self.vendor = vendor

    def printCategory(self):
        print(f"{self.category}, " + f"{self.vendor}")

    def getCategory(self):
        return self.category
    
    def getVendor(self):
        return self.vendor