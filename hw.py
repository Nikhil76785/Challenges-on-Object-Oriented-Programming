class RomanConverter:

    def __init__(self):
        self.roman = {
            1000: "M", 
            900: "CM", 
            500: "D", 
            400: "CD",
            100: "C", 
            90: "XC", 
            50: "L", 
            40: "XL",
            10: "X", 
            9: "IX", 
            5: "V", 
            4: "IV", 
            1: "I"
        }

    def convert(self, number):
        if number in self.roman:
            return self.roman[number]
        else:
            return "Not supported"

if __name__ == "__main__":
    try:
        number = int(input("Enter an integer: "))
        converter = RomanConverter()
        print(converter.convert(number))
    except ValueError:
        print("Please enter a valid integer")