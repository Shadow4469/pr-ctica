#gestionar el ingreso a una discoteca. Verificar si la persona es mayor o menos de edad. Las personas que sean hombres, pagan tarofa básica y las mujeres ingresan gratis

edad = int(input("ingrese su edad: "))
if(edad >= 18):
    genero = input("ingrese su género: ")

    if(genero == "hombre"):
        print("paga tarifa básica")

    if(genero == "mujer"):
        print("entras gratis")
else:
    print("no puedes pasar")