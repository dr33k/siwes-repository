class Roman:
    numerals = {"1":"I",
               
                "5":"V",
                
                "10":"X",
                
                "50":"L",
                
                "100":"C",
                
                "500":"D",
                
                "1000":"M"}

    numerals2 = { "4":"IV",
             "9":"IX",
             "40": "XL",
             "90":"XC",
             "400": "CD",
             "900":"CM"
             }

    @staticmethod
    def convert_to_rom(number):
        numerals = Roman.numerals
        numerals2 = Roman.numerals2

        steps = list(numerals.keys())
        rom_num = list()

        counter = len(steps)-1
        while number > 0:
            if str(number)[0] == "4":
                place_value = 10 ** (len(str(number))-1)
                rom_num.append(numerals2[str(4*place_value)])
                num_string = str(number)
                test_num_string = num_string[1:len(num_string):1]
                if test_num_string == "": number = 0
                else: number = int(test_num_string)

            elif str(number)[0] == "9":
                place_value = 10 ** (len(str(number))-1)
                rom_num.append(numerals2[str(9*place_value)])
                num_string = str(number)
                test_num_string = num_string[1:len(num_string):1]
                if test_num_string == "":
                    number = 0
                else:
                    number = int(test_num_string)

            elif number >= int(steps[counter]):
                number = number - int(steps[counter])
                rom_num.append(numerals[steps[counter]])

            else:
                counter -= 1

            answer = "".join(rom_num)
        return answer


try:
    value = int(input("Enter an integer:\n"))
    print(Roman.convert_to_rom(value))
except ValueError:
    print("Input does not contain a valid number, try again")
