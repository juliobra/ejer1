
class Email:
    def __init__(self,idcuenta,dom,tDominio,contra):
        self.__idcuenta = idcuenta
        self.__dom = dom
        self.__tDominio = tDominio
        self.__contra = contra
    
    def retornaEmail(self):
        return self.__idcuenta+"@"+ self.__dom+"."+self.__tDominio
    
    def getDominio (self):
        return self.__dom
    
    def cargaDatos(self):
        
        print("ingrese los datos\n")
        
        nombre=input("ingrese su nombre\n")
        self.__idcuenta=input("idcuenta\n")
        self.__dom=input("dominio\n")
        self.__tDominio=input("tipo dominio\n")
        self.__contra=input("contraseña\n")
        return nombre
   
    def getContra (self):
        return self.__contra
          
    def setContra (self, cont):
        self.__contra=cont
        
    def crearCuenta(self,c): 
        print("cuenta creada para la direccion \n",c)
        print("su contraseña es:\n",self.__contra)