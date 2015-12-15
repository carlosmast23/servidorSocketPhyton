import socket
import threading

#Clase que hereda de la clase Thread para poder manejar un hilo para
#controlar la lectura y escritura sobre el socket.
class Socket(threading.Thread):
    
    def __init__(self,sc,socket_conexion,datos_cliente):
        #informacion de la conexion con el cliente
        self.datos_cliente=datos_cliente
        #socket que recibe para manejar
        self.sc=sc
        self.socket_conexion=socket_conexion
        #inicializar el constructor del hilo
        threading.Thread.__init__(self)
        self.stoprequest = threading.Event()
        #variable para definir cuando detener el hilo
        self.condicion=True


    def leer(self):
        try:
            bufSize=1024
            datos_recibidos=self.sc.recv(bufSize)
            return datos_recibidos.decode('utf-8')        
        except socket.error as msg:
            print("Socket Error: %s" % msg)
    
    def escribir(self, mensaje):
        #enviar mensaje en formato utf8
        self.sc.send(mensaje.encode('utf8'))
    
    def desconectar(self):
        #terminar socket
        self.sc.close()
    
    #imprime la informacion de conexion con el cliente
    def imprimir(self):
        print(self.datos_cliente)

    def run(self):
        while self.condicion:
            #controla si se produce un erro on el escritura
            try:
            
                trama = self.leer()
                #print("trama->"+trama);
                #cuando la conexion rebiba la palabra exit termina
                if trama == "EXIT" or trama is None:
                    #desconecta y elimina el socket de la lista
                    self.socket_conexion.eliminar_socket(self)                        
                    self.desconectar()
                    self.condicion=False
                    print('cliente desconectado')
                else:
                        #print(trama)
                        self.escribir("Phyton dice recibido '"+trama+"'");
            
            except socket.error as msg:
                    self.socket_conexion.eliminar_socket(self)
                    self.desconectar()