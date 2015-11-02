# -*- coding: utf-8 -*-
class parametro():
    def __init__(self,nombre,tipo,unidad,valorDefecto,tablaValores):
        self.nombre=nombre
        self.tipo=tipo
        self.unidad=unidad
        self.puntero=valorDefecto        
        self.tablaValores=tablaValores
        
        
        
    def __str__(self):
        return "Nombre:{}\nParametro:{}\nTipo:{}\nUnidad:{}\nTabla de valores:{}".format(type(__name__),self.nombre,self.tipo,self.unidad,self.tablaValores)

    def aumentarValor(self):
        if self.puntero<len(self.tablaValores):
            self.puntero +=1
        return
                
    def disminuirValor(self):
        if self.puntero>0:
            self.puntero -=1
        return
        
    def valor(self):
        if type(self.tablaValores)==range:
            return self.tablaValores[self.puntero]
        
        


a=parametro("Frecuencia",2,"Hz",valorDefecto=2,tablaValores=range(0,101))
print (str(a))
a.aumentarValor()
print (a.valor)


































