print("---------------------------------------------------------")
print("---------------------------------------------------------")
user=input("Ingrese su usuario:")
password=input("Ingrese su contraseña: ")
saldo=10000


if password=="1234" and user=="admin":
    print("---------------------------------------------------------")
    print("Ingreso Exitoso")
    print("---------------------------------------------------------")
    print ("CAJERO AUTOMATICO")
    print("-------ISPC-------")
    print("Listado de opciones:")
    print("1)   Ingreso de dinero")
    print("2)   Extraccion de dinero")
    print("3)   Consulta de saldo")
    print("4)   Salir")
    
    
    
    while True:
        opcioningreso=input("Ingrese su eleccion:")
        
        if opcioningreso=="1":
            print ("Usted ha ingresado la opcion 1")
            ingresodinero=int (input("Monto que desea ingresar:"))
            saldo=saldo+ingresodinero
            print ("Total de su cuenta bancaria es:",saldo)
            break
         
    
        elif opcioningreso=="2":
            print ("Usted ha ingresado la opcion 2")
            retirodinero=int (input("Monto que desea retirar:"))
            if saldo<retirodinero:
                print ("No se puede completar la operacion porque no dispone del monto")
            else: 
                saldo=saldo-retirodinero
                print("Total del saldo es:",saldo)
            break
        
        elif opcioningreso=="3":
            print ("Usted ha ingresado la opcion 3")
            print ("Total de su cuenta bancaria es:",saldo)
            break
        elif opcioningreso=="4":
            exit            

        else: print("Opcion invalida. Por favor ingrese una opcion valida.")


else: print("Contraseña Incorrecta o usuario incorrecto")