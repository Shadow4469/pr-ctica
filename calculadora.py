print("CALCULADORA")
num1 = float(input("digite el primer número: "))
num2 = float(input("digite el segundo número: "))
op = input("ingresa el tipo de operacion: +,-,*,/: ")

if(op == "+"): 
    print(f"la suma es: {num1+num2}")

if(op == "-"):
    print(f"la resta es: {num1-num2}")

if(op == "*"):
    print(f"la multiplicación es: {num1*num2}")

if(op == "/"):
    print(f"la división es: {num1/num2}")
