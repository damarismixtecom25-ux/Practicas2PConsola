if __name__ == "__main__":
    from holaMundo import Mensaje
    from Persona import Persona
    from operacionesMatematicas import OperacionesMatematicas
    from Cuadrado import Cuadrado
    from Triangulo import Triangulo
    from Rectangulo import Rectangulo

    print("Este es el programa ptincipal")
    print("Seleccione una opción:")
    print("1. Mostrar mensaje")
    print("2. Edad de una persona")
    print("3. Operaciones matemáticas")
    print("4. Figuras geometricas")
    opcion = input("Seleccione un numero de la opcion que desea ejecutar: ")

    if opcion == "1":
        mensaje = Mensaje("Hola Mundo Programación con clases")
        mensaje.mostrar()
    elif opcion == "2":
        nombre = input("Ingrese el nombre de la persona: ")
        anio_nacimiento = int(input("Ingrese el año de nacimiento de la persona: "))
        anio_actual = int(input("Ingrese el año actual: "))
        persona = Persona(nombre, anio_nacimiento, 0)
        print(f"Nombre: {persona.nombre}, Edad: {persona.calcular_edad(anio_actual)} años")
    elif opcion == "3":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        operacion = OperacionesMatematicas(a, b)
        print("Suma:", operacion.sumar())
        print("Resta:", operacion.restar())
        print("Multiplicación:", operacion.multiplicar())
        print("División:", operacion.dividir())
    elif opcion == "4":
        print("Escribe el numero de la figura geometrica que deseas calcular el area y perimetro:")
        print("1. Cuadrado")
        print("2. Triangulo")
        print("3. Rectangulo")
        figura= input("ingrese el numero de la figura geometrica que desea calcular: ")
        if figura == "1":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(f"Area del cuadrado: {cuadrado.area()}, Perimetro del cuadrado: {cuadrado.perimetro()}")
        elif figura == "2":
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            triangulo = Triangulo (base, altura)
            print(f"Area del triangulo: {triangulo.area()}, Perimetro del triangulo: {triangulo.perimetro()}")
        elif figura == "3":
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            rectangulo = Rectangulo(base, altura)
            print(f"Area del rectangulo: {rectangulo.area()}, Perimetro del rectangulo: {rectangulo.perimetro()}")
    
    else:print("La opción no es válida")
