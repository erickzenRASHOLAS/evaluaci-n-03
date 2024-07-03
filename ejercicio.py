#prueba n3
from funciones import *
pedido=[]
pedidos=()
while True:
    os.system('cls')
    print( "\t BIENVENIDO A GAXPLOSIVE :)")
    print("1. Registar Pedido")
    print("2. Listar ")
    print("3. Buscar pedido por rut")
    print("4. Imprimir hoja de ruta")
    print("5. Salir")
    opc=int(input("Seleccione una opción: "))
    os.system('cls')
    
    if opc==1:
        registrar_pedido()
    elif opc ==2:
        listar_pedidos()
    elif opc==3:
        buscar_por_rut
    elif opc==4:
        archivo_csv()
    elif opc==5:
        break
    else:
        print("ERROR!!! INGRESE UNA OPCIÓN VALIDA!!!")
        time.sleep(2)
print("hasta luego!!")
time.sleep(2)