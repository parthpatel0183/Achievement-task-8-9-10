while True:
    try:
        number = int(input("Please enter the value you want to convert: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if number < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        
        break
if number >= 0: 
    print("You are able to perform the conversion!")
else:
    print("You are not able to perform the conversion.")


def weightConversion(weight, weightUnit):
    if weightUnit == 'kg':  
        convertedweight = ( weight / 2.2)  
    
    elif weightUnit == 'lb': 
        convertedweight = (weight*2.2)  
        
    return convertedweight  

def lengthConversion(length, lengthUnit):
    if lengthUnit == 'm':  
        convertedlength = 3.2 * length  
    
    elif lengthUnit == 'ft': 
        convertedlength = length / 3.2; 
        
    return convertedlength 


def main():
    conversionType = int(input("What do you want to convert: Enter 1 for weight or 2 for length :: "))
    if conversionType == 1:
        inputweight = number
        weightUnit = input("Enter the current unit for the weight :: ")
        weightUnit = weightUnit
        print("Converted weight is :: {:.2f}".format(weightConversion(inputweight, weightUnit)))

        
        
    elif conversionType == 2:    
        inputlength = number
        lengthUnit = input("Enter the current unit for the length :: ")
        lengthUnit = lengthUnit
        print("Converted length is :: {:.3f}".format(lengthConversion(inputlength, lengthUnit)))
        
    else:
        print("Wrong input entered for conversion!!")

main()    




 








