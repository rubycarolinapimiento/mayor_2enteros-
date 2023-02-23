# Programa para veriicar cual de dos numeros enteros es el mayor 

print("...........................")
print("......MAYOR 2 ENTEROS......")
print("...........................")

# input 
x = int(input("Digite el valr de x: "))
y = int(input("Digite el valor de y: "))

# procesing 
if x == y: 
      # ouput
      print("Los numeros iguales...")    
else:
         if x > y: 
             mayor = x
         else: 
            mayor = y     
#ouput 
print("El mayor entre " + str(x) + " y " + str(y) + " es " + str(mayor))
