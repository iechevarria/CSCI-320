import fileinput


def isNonNegative(array):
    for i in range(len(array)):
        if i < 0:
            return False
    return True


if __name__ == '__main__':
    for line in fileinput.input():

        if len(line.split()) == 4 and isNonNegative(line.split()):
            print('new batch')
            loan_months = float(line.split()[0])
            down_payment = float(line.split()[1])
            loan_value = float(line.split()[2])
            car_value = float(line.split()[2])
            next_lines = float(line.split()[3])
            
            month = 0
            depreciation = 0.0

            found = False
        
        elif len(line.split()) == 2 and isNonNegative(line.split()) and not found:

            print(line.split())
            if line.split()[0] == '0':
                depreciation = float(line.split()[1])
                car_value = car_value * (1 - depreciation)
            else:
                while month <= int(line.split()[0]):
                    car_value = car_value - (car_value * depreciation)
                    loan_value = loan_value - loan_payment
                    if car_value > loan_value:
                        found = True
                        print("SOLVED")
                    month += 1

                depreciation = float(line.split()[1])
                car_value = car_value * (1 - depreciation)
                if car_value > loan_value and not found:
                        found = True
                        print("SOLVED")
                month += 1

            print(str(car_value) + ' diff ' + str(loan_value))

