#print('FUNCIONA? SI')

#FORMA 1 : SIN HERENCIAS, CON INSTANCIAS
def forma1():
    class Producto:
        def __init__(self,nombre,unidades,precio):
            self.nom=nombre
            self.ud=unidades
            self.pre=precio
        def consultarTotal(self):
            print(f'El total de precio de "{self.nom}" con {self.ud} unidades es de {self.ud*self.pre}€')

    producto1=Producto('camisa',15,9.95) #instanciar
    producto2=Producto('chaqueta',20,19.95) #instanciar
    producto1.consultarTotal() #llamar al método
    producto2.consultarTotal() #llamar al metodo
forma1()


#FROMA 2 : CREANDO VARIAS CLASES Y HEREDANDO
def forma2():
    class Producto: #clase padre Producto
        def __init__(self, nombre, unidades, precio):
            self.nom = nombre
            self.ud = unidades
            self.pre = precio

        def consultarTotal(self):
            print(f'El total de precio de "{self.nom}" con {self.ud} unidades es de {self.ud * self.pre}€')

    class Camisa(Producto): #herencia de la clase Producto
        def consultarTotal(self): #override
            print(f'El total de precio de la "{self.nom}" con {self.ud} unidades es de {self.ud * self.pre}€')

    class Chaqueta(Producto): #herencia de la clase Producto
        def consultarTotal(self): #override
            print(f'El total de precio de la "{self.nom}" con {self.ud} unidades es de {self.ud*self.pre}€')

    producto1 = Camisa('camisa',15,9.95)
    producto2 = Chaqueta('chaqueta',20,19.95)
    producto1.consultarTotal()
    producto2.consultarTotal()
forma2()