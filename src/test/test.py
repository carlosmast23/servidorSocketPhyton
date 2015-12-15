from servidor.SocketConexion import *
import sys

__author__ = "Carlos Sanchez"
__date__ = "$14-dic-2015 11:18:11$"

if __name__ == "__main__":
    #creo un objeto para escuhar nuevas conexiones
    socketConexion=SocketConexion("localhost",9999)
    condicion=True
    while (condicion):
        print("                                                            ")
        print("-------------------------- MENU ----------------------------")
        print("1.- Iniciar Servidor")
        print("2.- Mostrar Todos los clientes")
        print("3.- Parar Servidor")
        print("4.- Salir")
        print("--------> Seleccione una opcion:")

        valor=input()
        print("                                                            ")

        if valor=="1":
            socketConexion.start()
            print('Servidor Iniciado...')
        elif valor=="2":
            socketConexion.imprimir()
        elif valor=="3":
            socketConexion.detener;
            print('Servidor Detenido...')
        elif valor=="4":
            print('Ejecucion Terminada');
            sys.exit(0)
            
        
    