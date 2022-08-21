def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número:"))
    y = int(input("Ingresa el segundo número:"))
    z = int(input("Ingresa el tercer número:"))
    if(x>y and y>z):
        print("",x,"-",y,"-",z)
    elif(y>x and x>z):
        print("",y,"-",x,"-",z)
    elif(z>x and y>x):
        print("",z,"-",x,"-",y)
    elif(z>y and y>x):
        print("",z,"-",y,"-",x)
    elif(x>z and z>y):
        print("",x,"-",z,"-",y)
    elif(y>z and z>x):
        print("",y,"-",z,"-",x)


if __name__=='__main__':
    main()
