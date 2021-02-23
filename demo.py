class impresiones:
    '''Esta clase es para realizar impresiones,
    tanto de str, int o float
    '''
    # no hay entrada, self hace referencia
    # al objeto creado de la clase en si,
    # siempre debe aparecer como parametro de entrada a la hora
    # de programar las funciones, no asi cuando es llamada la funcion
    def __init__(self,dato):#constructor de la clase siempre se llama init
        '''Esta funcion es el constructor de la clase
        impresiones
        Entrada:
            - dato: puede ser de tipo str, int, o float
        Salida: No hay parametros de salida
        '''
        self.dato=dato #se guarda el parametro de entrada dato 
                       # en el atributo dato de la clase
    
    def identificar_tipo(self,dato):
        '''Esta funcion se encarga de identificar el tipo
        de dato que se desea imprimir
        Entrada:
            - dato: puede ser de tipo str, int, o float
        Salida:
            - tipo: devuelve el tipo del dato ingresado
        '''
        tipo=type(dato)
        return tipo
    def imprimir_tipo(self):
        '''Esta funcion se encarga de imprimir el tipo
        del dato ingresado
        Entrada: no hay parametros de entrada
        Salida: no hay parametros de salida
        '''
        #para acceder a algun atributo o funcion de una clase
        #desde otra funcion de la misma clase, se debe de utilizar
        #la palabra self seguida de un punto y a continuacion
        #el nombre del atributo o funcion que querramos utilizar
        self.tipo=self.identificar_tipo(self.dato)
        print("el tipo del dato ingresado es: ",self.tipo)
    def imprimir(self):
        '''Esta funcion se encarga de imprimir el dato ingresado
        Entrada: no hay parametros de entrada
        Salida: no hay parametros de salida
        '''
        print("el dato es: ", self.dato)