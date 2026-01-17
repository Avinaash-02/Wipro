class Car:
    def brand(self,brand_name):
        self.brand_name = brand_name
    def year(self,mfg_year):
        self.mfg_year = mfg_year
    def output(self):
        return f"Brand Name: {self.brand_name}, Manufacture Year: {self.mfg_year}"
car= Car()
car.brand("Toyota")
car.year("1975")
print(car.output())
