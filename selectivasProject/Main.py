# Estructura simple
a = 33
b = 200

if b > a:
    print(b, "Es mayor que ",a)

#Estrutura Doble
if a > b:
    print(a,"Es mayor que ",b)
else:
    print(a,"No es mayor que",b)



#Condicion Multiple
c = 200
d = 207
if a > b:
    print(c,"es mayor que",d)
elif c < d:
    print(c,"es menor que",d)
else:
    print(c,"es igual que",d)

#Condiciones enlazadas
x = 28
if x > 10:
    print("Por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")

    #Parametros end
    print("Estudiar los sabados", end= ' ')
    print("es genial")

    #parametros set
    print("Daniela","Luis","Carlos","Camila")#agrega un espacio por defecto
    print("Daniela", "Luis", "Carlos", "Camila",sep="")#Quita el espacio
    print("Daniela", "Luis", "Carlos", "Camila",sep=",")#Agrega una coma
    print("Daniela", "Luis", "Carlos", "Camila",
          sep = "_", end="_Curso_Python")#implemetacion end y sep