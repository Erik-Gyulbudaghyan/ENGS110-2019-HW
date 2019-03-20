def setupInitMoney():
    money = float(input("write the number of money: "))
    while (money<=0):
        print("Error, not in the range of Money ")
        money = float(input("write the number of money: "))
    return money
def setupPercent():
    percent = float(input("number of percent in %: "))
    while (percent<0 or percent>100):
        print("Error, not in the range of % ")
        percent = float(input("number of percent in %: "))
    return percent
def setupYears():
    years = int(input("number of years from 1 to 20: "))
    while (years<=0 or years>20):
        print("Error, not in the range of years")
        years = int(input("number of years from 1 to 20: "))
    return years
def calculateTheResultMoney(initMoney, percent, years):
    while (years >0):
        result = initMoney * (1 + (percent/100))
        years = years - 1
    return result
def main():
    print ("this is my app ")
    initMoney = setupInitMoney()
    percent = setupPercent()
    years = setupYears()
    result = calculateTheResultMoney(initMoney, percent, years)
    print("After", years, "your", initMoney,"increase to", result)

main()    
