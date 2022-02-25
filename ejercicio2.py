def calcularSueldo(salario, diasTrabajados):
    sueldoapagar = salario/30 * diasTrabajados
    return sueldoapagar

def main():
    nombre = input("Digite el Nombre ==>  ")
    salario = int(input("Digite su salario ==>  "))
    diasTrabajados = int(input("Digite cuantos dias trabajo al mes ==>  "))
    sueldoapagar = calcularSueldo(salario, diasTrabajados)
    print(f"Su nombre es {nombre} y su sueldo es de {sueldoapagar:.0f}")



if __name__ == "__main__":
    main()



