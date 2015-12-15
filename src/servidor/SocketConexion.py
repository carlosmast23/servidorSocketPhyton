from servidor.Socket import *
import threading

#clase que me permite gestionar nuevas conexiones
#y eliminar las conexiones existentes

class SocketConexion(threading.Thread):
    
     def __init__(self,host,puerto):
         
        #host de la conexion para abrir un socket
        self.host=host
        #puerto de la conexion escucha
        self.puerto=puerto
        #socket para establecer conexion iniciado con los protocolos adecuados
        self.sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #variables para implementar un hilo
        threading.Thread.__init__(self)
        self.stoprequest = threading.Event()
        #condicion del hilo
        self.condicion=True
        #lista de sockets conectados
        self.lista_sockets=[]
        #iniciar configuraciones
        self.iniciar_configuracion()

     def iniciar_configuracion(self):
        address=(self.host,self.puerto)
        #conexion al cliente
        self.sc.bind(address)
        #numero maximo de escuchas que puede aceptar
        self.sc.listen(5)

     #obtiene un objeto de tipo socket con la conexion establecida
     def esperar_conexion(self):
        try:
            socket_servidor, datos_cliente = self.sc.accept() 
            return Socket(socket_servidor,self,datos_cliente)
        except socket.error as msg:
            print("Socket Error: %s" % msg)


     #metodo del hilo que controla        
     def run(self):
        while self.condicion:
            #print ('esperando conexion '+self.nombre)
            socket_conectado=self.esperar_conexion()
            
            #inicia el socket, para empieze a leer y escribir
            socket_conectado.start()

            #agrega el socket a una lista para tener todas las conexiones
            self.lista_sockets.append(socket_conectado)
            

     #imprime la lista de los sockets en la lista       
     def imprimir(self):
         print("-------------------> Lista Clientes<-----------------------")
         for i in self.lista_sockets:
             i.imprimir()
         print(" ")

     #metodo que elimina un socket de la lista    
     def eliminar_socket(self,sc):
        #print("-->"+sc.imprimir())
        ubicacion = self.lista_sockets.index(sc)
        del self.lista_sockets[ubicacion] 
  
     def detener(self):
        self.condicion=False

