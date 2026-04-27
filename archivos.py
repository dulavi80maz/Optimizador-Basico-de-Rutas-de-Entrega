#Usando archivos
#open(nombre_archivo, modo)
#nombre_archivo: indicar nombre y tipo
#modo: "r" leer, w "sobreescribir"
#"a" agrega al final, "r+" lee y escribe sin borrar el contenido 
#"a+" lee y agrega al final 

#Escribir
with open("datos.txt" , "w")
archivo.write("Hola Mundo")
 
#Escribir
# with open("datos.txt" , "w") as archivo:
#gregar lineas sin borrar
with open("datos.txt" , "a") as archivo:
     archivo.write ("Hola Andrea  \n"  )
