def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg:"))
    altura = float(input("Altura en m:"))

    if(peso<=0):
        print ("Revisa tus datos, alguno de ellos es erróneo")
    if(altura<=0):
        print ("Revisa tus datos algunos de ellos es erróneo")
    
    IMC = peso / (altura**2)
    
    if IMC <= 20:
        print("PESO BAJO")
    elif 20 <= IMC <= 25:
        print("NORMAL")
    elif 25 <= IMC <= 30:
        print ("SOPREPESO")
    elif 30 <= IMC <= 40:
        print ("OBESIDAD")
    elif 40 <= IMC:
        print ("OBESIDAD")
    
    
    
    
    

if __name__=='__main__':
    main()