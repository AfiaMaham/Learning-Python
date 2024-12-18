# 1. Currency Converter
# Description: A program to convert currency values based on a predefined exchange rate.


def converter(val,currency):
    result = 0
    if(currency == 1):
        result = val * 0.0036
    elif(currency == 2):
        result = val * 0.0034
    elif(currency == 3):
        result = val * 0.0028
    elif(currency == 4):
        result = val * 0.55
    elif(currency == 5):
        result = val * 0.13
    elif(currency == 6):
        result = val * 5.17
    elif(currency == 7):
        result = val * 0.026
    elif(currency == 8):
        result = val * 0.30
    elif(currency == 9):
        result = val * 0.014
    elif(currency == 10):
        result = val * 0.43
    return result


value = int(input("Enter amount: "))
print("Avaliable currencies")
print("1-  US Dollar\n2-  Euro\n3-  Pound\n4-  Yen\n5-  Lira\n6-  Won\n7-  Yuan\n8-  IND rupee\n9-  Rial\n10- Taka")
currency = int(input("Select any from 1 to 10: "))
print(f"Converted Amount: {round(converter(value,currency),3)}")