def Modulus (num1:int, num2: int) -> int:
    #Add two numbers
    mod = num1 % num2
    return mod
#Driver code
num1, num2 = 8, 30
mod = Modulus(num1, num2)
print(f"The Modulus of {num1} and {num2} is = {mod}.")