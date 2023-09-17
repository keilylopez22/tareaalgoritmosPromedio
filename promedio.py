texto = "Juan,98,87,89,90|Jose,90,43,20,40|Pedro,70,80,89,90"
listaEstudiantes= texto.split("|")
archivo= open("promedio.txt","w")
#print(listaEstudiantes)
for estudiante in listaEstudiantes:
   # print(estudiante)
    listaDeDatos = estudiante.split(",")
    #print(listaDeDatos)
    nombre = listaDeDatos[0]
    nota1 = int(listaDeDatos[1])
    nota2 = int(listaDeDatos[2])
    nota3 = int(listaDeDatos[3])
    nota4 = int(listaDeDatos[4])

    promedio =(nota1 + nota2 + nota3 + nota4 ) / 4
    print(nombre, "=" , promedio)
    
    archivo.write(nombre+ "="+str(promedio)+"\n")
    
    

    

    
