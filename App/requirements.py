
import config as cf
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")   
    print("4- Encontrar buenas películas")
    print("5- Consultar todas las peliculas de un director")
    print("6- Ranking de películas")    
    print("7- Consultar todas las peliculas en las que ha participado un actor")
    print("0- Salir")

def conocer_un_director(criteria,lst1,lst2):

     if len(lst1) == 0 or len(lst2) == 0:
        print("Alguna de las listas está vacía.")
     else:
        t2_start = process_time() #tiempo inicial
        pelis_director=lt.newList(datastructure='ARRAY_LIST', cmpfunction = None)
        info={}
        tit=lt.newList(datastructure='ARRAY_LIST', cmpfunction = None)
        vote_av=lt.newList(datastructure='ARRAY_LIST', cmpfunction = None)
        num_pelis=0
        filas = len(lst1)
        i=1
        while i < filas:
            
            director_name = lst2[i]['director_name']
            if director_name == criteria:
                lt.addLast(tit,lst1[i]['title'])

                info['Titulos peliculas']=tit
                num_pelis+=1
                lt.addLast(vote_av,float(lst1[i]['vote_average']))
            i+=1
        if lt.size(vote_av)==1:
            info['Promedio votos peliculas']=lt.getElement(vote_av,1)
        else:
            suma=0
            for j in range(0,lt.size(vote_av)):
                suma=suma + lt.getElement(vote_av,j)

        info['Promedio votos peliculas']=round(suma/lt.size(vote_av),2)
        info['Total peliculas']=num_pelis
        lt.addLast(pelis_director,info)
        t2_stop = process_time() #tiempo final
        print("Tiempo de ejecucion",t2_stop-t2_start)

     return pelis_director

def conocer_un_actor(criteria,lst1,lst2):
    if len(lst1) == 0 or len(lst2) == 0:
        print("Alguna de las listas está vacía.")
    else:
        t1_start = process_time() #tiempo inicial
        pelis_actor=lt.newList(datastructure='ARRAY_LIST', cmpfunction = None)
        info={}
        tit=lt.newList(datastructure='ARRAY_LIST', cmpfunction = None)
        vote_av=lt.newList(datastructure='ARRAY_LIST', cmpfunction = None)
        num_pelis=0
        i=1
        filas=len(lst2)
        while i<filas:
            if criteria in lst2[i]['actor1_name'] or criteria in lst2[i]['actor2_name'] or criteria in lst2[i]['actor3_name'] or criteria in lst2[i]['actor4_name'] or criteria in lst2[i]['actor5_name']:
                lt.addLast(tit,lst1[i]['title'])
                info['Titulos peliculas']=tit
                num_pelis+=1
                lt.addLast(vote_av,float(lst1[i]['vote_average']))   
            
        
            i+=1
        if lt.size(vote_av)==1:
            info['Promedio votos peliculas']=lt.getElement(vote_av,1)
        else:
            suma=0
            for j in range(0,lt.size(vote_av)):
                suma=suma + lt.getElement(vote_av,j)
        info['Promedio votos peliculas']=round(suma/lt.size(vote_av),2)
        info['Total peliculas']=num_pelis
        lt.addLast(pelis_actor,info)
        t1_stop=process_time()
        print("Tiempo de ejecucion",t1_stop-t1_start)
    return pelis_actor








def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista_1 = [] #instanciar una lista vacia
    lista_2 = [] #instanciar una segunda lista vacia para el segundo archivo CSV
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/AllMoviesDetailsCleaned.csv", lista_1) #llamar funcion cargar datos del primer archivo
                loadCSVFile("Data/AllMoviesCastingRaw.csv", lista_2) #llamar funcion cargar datos del segundo archivo
                print("Archivo: AllMoviesDetailsCleaned.csv"+"\nDatos cargados, "+str(len(lista_1))+" elementos cargados")
                print("\nArchivo: MoviesCastingRaw.csv"+"\nDatos cargados, "+str(len(lista_2))+" elementos cargados")
                
            elif int(inputs[0])==2: #opcion 2
                
            elif int(inputs[0])==3: #opcion 3
                

            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsByCriteria(criteria,12,lista_1,lista_2)
                print("Coinciden ",counter[0]," elementos con el crtierio: '", criteria, "\nCon un promedio de votos de: ", counter[1])
            elif int(inputs[0])==5: #opcion 5
                criteria=input('Ingrese el nombre del director que desea consultar\n')
                print(conocer_un_director(criteria,lista_1,lista_2))
            elif int(inputs[0])==7: #opcion 7
                criteria=input('Ingrese el nombre del actor o actriz que desea consultar\n')
                print(conocer_un_actor(criteria,lista_1,lista_2))
                
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

            elif int(inputs[0])==6: #opcion 6
                genero = input("Ingrese el género de búsqueda:\n")
                numero = int(input("Ingrese el número de películas que quiere ver en el ranking:\n"))
                criterio= int(input("Ingrese:\n1. Si quiere ordenar por Número de votos.\n2. Si quiere ordenar por Calificación.\n"))
                ranking=ranking_genero(genero,numero,lista_1,lista_2,criterio)
                print("El TOP ",numero," de mejores peículas es: (Nombre, Calificación, Número de votos)\n",ranking[0],"\n\nEl TOP ",numero,"de peores películas es:(Nombre, Calificación, Número de votos)\n",ranking[1])

if __name__ == "__main__":
    main()