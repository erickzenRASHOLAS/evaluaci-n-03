import os, time, msvcrt
pedido=[]
pedidos=[]

def registrar_pedido():
    
    rut=int(input("ingrese rut sin puntos ni guión: "))
    nombre=str(input("ingrese nombre : "))
    dirección=str(input("ingrese dirección : "))
    comuna=str(input("ingrese comuna : "))
    pedido.append(rut)
    pedido.append(nombre)
    pedido.append(dirección)
    pedido.append(comuna)
    
    time.sleep(2)
    os.system('cls')
    cant_cilindro5=0
    cant_cilindro15=0
    monto_final=0
    valor_cili5=12500
    valor_cili15=25500
    print(f"CILINDRO 5KG {valor_cili5}$")
    print(f"CILINDRO 15KG {valor_cili15}$")
    lleva_de_5=int(input("INGRESE CANTIDAD DE CILINDROS DE 5KG QUE LLEVA: "))
    lleva_de_15=int(input("INGRESE CANTIDAD DE CILINDROS DE 15KG QUE LLEVA: "))
    cant_cilindro5=cant_cilindro5+lleva_de_5
    cant_cilindro15=cant_cilindro15+lleva_de_15
    monto_final=monto_final+(cant_cilindro5*valor_cili5)+(cant_cilindro15*valor_cili15)
    pedido.append(lleva_de_5)
    pedido.append(lleva_de_15)
    pedido.append(monto_final)
    pedidos.append(pedido)
    return


def listar_pedidos():

    for pedido in pedidos:
        print (f"{pedidos}\nrut: {pedido[0]} \nnombre: {pedido[1]} \ndirección: {pedido[2]} \ncomuna: {pedido[3]} \nCIL.5KG: {pedido[4]} \nCIL.15KG: {pedido[5]} \nTOTAL: {pedido[6]}" )
        time.sleep(2)
        os.system

def buscar_por_rut():

    while True:
        try:
            rutbuscar=int(input("INGRESE RUT A BUSCAR"))
            for pedido in pedidos:
                if rutbuscar in pedido[0]: 
                    print(pedido)
                else:
                    print("NO EXISTE PEDIDO ASOCIADO A ESTE RUT")
        except:
            len(pedidos)<=0
            print("ERROR!! NO HAY NINGUN PEDIDO REALIZADO")
            return
        
def archivo_csv():
    print("archivo creado :()")