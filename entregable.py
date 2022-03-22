print ('MENU REGISTROS\n(1)->Nuevo\n(2)->Mostrar\n(3)->Eliminar registros\n')

opcion = input('Elige una opcion ( ): ')

if opcion == '1' :
    print('nuevo registro\n')
    archivo = open('ejemplo.csv','a')
    nombre = input('ingrese el nombre: ')
    Horas = int(input('Numero de horas trabajadas: '))
    print('ingrese el turno: ')
    print('-----(turno mañana = M), (turno tarde = T), (turno noche = N)-----')

    Turno = ''
    while Turno != 'M' and Turno != 'T' and Turno != 'N':
          Turno= input('Turno de trabajo realizado: ')

    if Turno == 'M':
       Salario= 37.00
    elif Turno == 'T':
       Salario= 38.20
    elif Turno == 'N':
       Salario= 38.50

    Pago = Horas * Salario

    if Turno == 'N' and Pago > 200 and Pago < 500:
        Pago = Pago - 0.15 * Pago
        print('El Pago es: ', Pago)

    elif Turno == 'N' and Pago > 800 and Pago < 1000:
        Pago = Pago - 0.17 * Pago
        print('El Pago es: ', Pago)

    else:
        print('El Pago es: ', Pago)
    
    
    print('se han capturado: ', nombre, 'con pago: ', Pago)
    
    archivo.write(nombre)
    archivo.write(',')
    archivo.write(str(Pago))
    archivo.write(',')
    archivo.write('\n')
    archivo.close()


elif opcion == '2':
    print('mostrar registros\n')
    archivo = open('ejemplo.csv')
    print(archivo.read())
    archivo.close()


elif opcion == '3':
     archivo = open('ejemplo.csv','a')
     archivo.truncate()
     
     print('Registros eliminados')
     archivo.close()


else:
    print('Debes de elegir una opcion anterior')

