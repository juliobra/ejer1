from classemail import Email
import csv
def leerArchivo():
    with open("correos.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            correo = Email(row[0], row[1], row[2], row[3])
            
            if "@" in correo.retornaEmail():
                correo.crearCuenta()
            else:
                print("La dirección de correo", correo.retornaEmail(), "es incorrecta.")


def contarDominio():
    domBuscado = input("Ingrese el dominio a buscar: ")
    contador = 0
    
    with open("direcciones.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            correo = Email(row[0], row[1], row[2], row[3])
            
            if correo.getDominio() == domBuscado:
                contador += 1
    
            print("Hay", contador, "cuentas con el dominio", domBuscado)
def modificarContra(e1): 
    print("modificar la contraseña\n")
    print("vieja",e1.getContra())
    print("ingrese la contraseña actual: ")
    Actual=input("")
    if (e1.getContra() == Actual):
        print("ingrese la nueva contraseña:\b")
        nueva=input("")
        e1.setContra(nueva) 
         
        
    else :
      print("las contraseñas no coinciden\n")
      modificarContra(e1)

def test(E1):
   
    nombre=E1.cargaDatos()
    correo= E1.retornaEmail()
    
    E1.crearCuenta(correo)
    print("estimado {} enviaremos su correo a la dirección {}".format(nombre,correo))
    print("actual**\n",E1.getContra())
    modificarContra(E1)
    print("**nueva***",E1.getContra())

def modificarContra(e1): 
    print("modificar la contraseña\n")
    print("vieja",e1.getContra())
    print("ingrese la contraseña actual: ")
    Actual=input("")
    if (e1.getContra() == Actual):
        print("ingrese la nueva contraseña:\b")
        nueva=input("")
        e1.setContra(nueva) 
         
        
    else :
      print("las contraseñas no coinciden\n")
      modificarContra(e1)

if __name__ == '__main__':
    E1=Email("","","","")
    test(E1)
    leerArchivo()
    contarDominio()