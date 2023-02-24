# input

X = int(input("ingrese un numero de X: "))

Y = int(input("ingrese el numero de Y: "))

# processing
if X == Y:
    # output
    print("los numeros son iguales...")
else:
    if X > Y:
        mayor = X
    else:
            mayor = Y
    print("el mayor entre: " + str(X) + " y " + str(Y) + " es " + str(mayor))
    