print("CALCULADORA")
x1 = float(input("digite el primer número: "))
x2 = float(input("digite el segundo número: "))
op = input("ingresa un tipo de cálculo: +, -, *, /: ")

if (op == "+"): 
    print(f"suma= {x1+x2}")

elif(op == "-"):
    print(f"resta= {x1-x2}")

elif(op == '*'):
    print(f"multiplicación= {x1*x2}")

elif(op == '/'):
    print(f"división= {x1/x2}")

else:(op == "" )
print("especifíque su respuesta")
