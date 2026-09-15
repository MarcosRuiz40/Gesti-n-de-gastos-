import datetime
import csv

# -----------------------------------------------------------------
# Los gastos se guardan como una lista de diccionarios.
# Cada gasto: {"descripcion": str, "monto": float, "categoria": str, "fecha": str}
gastos = []
encabezados = ['fecha', 'categoria', 'monto', 'descripcion']

def eliminarGasto():
    try:
        if not gastos:
            print("No hay gastos para eliminar.\n")
            return
        
        mostrar_gastos()
        
        eliminar = int(input("Que elemento queres eliminar: ")) - 1
        
        gasto_borrado = gastos.pop(eliminar)
        print(f"Se eliminó: {gasto_borrado['descripcion']} - ${gasto_borrado['monto']:.2f}\n")
        
        
    except IndexError:
        print("Valor invalido volver a ingresar otro.")
        pass
    except ValueError:
        print("No se permiten letras solo numeros")
        pass
    

def cargarCSV():
    try:
        with open("gastos.csv", "r", newline="", encoding="utf-8") as archivo:
            leer = csv.DictReader(archivo)
            for i in leer:
                i["monto"] = float(i["monto"])
                gastos.append(i)
                # print(f"se cargaron {len(gastos)} gastos desde gastos.csv\n")
    except FileExistsError:
        pass
    
            
            
def exportar_csv():
    with open("gastos.csv", "w", newline="", encoding="utf-8") as archivo:
        escribir_diccionario = csv.DictWriter(archivo ,fieldnames= encabezados)
        escribir_diccionario.writeheader()
        escribir_diccionario.writerows(gastos)
        print("Archivo CSV creado con éxito!")

def agregar_gasto():
    descripcion = input("Descripción del gasto: ")
    categoria = input("Categoría (ej: comida, transporte, ocio): ")

    # Validamos que el monto sea un número válido
    monto_valido = False
    while not monto_valido:
        monto_texto = input("Monto: ")
        try:
            monto = float(monto_texto)
            if monto <= 0:
                print("El monto tiene que ser mayor a 0.")
                continue
            monto_valido = True
        except ValueError:
            print("Eso no es un número válido, probá de nuevo.")

    fecha = datetime.datetime.now().strftime("%Y-%m-%d")

    gasto = {
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria,
        "fecha": fecha,
    }
    gastos.append(gasto)
    print(f"Gasto agregado: {descripcion} - ${monto:.2f}\n")


def mostrar_gastos():
    if not gastos:
        print("Todavía no cargaste ningún gasto.\n")
        return

    print("\n--- Lista de gastos ---")
    for i, g in enumerate(gastos, start=1):
        print(f"{i}. {g['fecha']} | {g['categoria']:<12} | {g['descripcion']:<20} | ${g['monto']:.2f}")
    print()


def calcular_total():
    total = sum(g["monto"] for g in gastos)
    print(f"Total gastado: ${total:.2f}\n")
    return total


def total_por_categoria():
    if not gastos:
        print("No hay gastos cargados todavía.\n")
        return

    totales = {}
    for g in gastos:
        categoria = g["categoria"]
        totales[categoria] = totales.get(categoria, 0) + g["monto"]

    print("\n--- Total por categoría ---")
    for categoria, monto in totales.items():
        print(f"{categoria}: ${monto:.2f}")
    print()


def mostrar_menu():
    print("=============== Procesador de gastos ===============")
    print("1. Agregar gasto")
    print("2. Ver todos los gastos")
    print("3. Ver total gastado")
    print("4. Ver total por categoría")
    print("5. Exportar archivo")
    print("6. Eliminar gasto")
    print("7. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        match opcion:
            case "1":
                agregar_gasto()
            case "2":
                mostrar_gastos()
            case "3":
                calcular_total()
            case "4":
                total_por_categoria()
            case "5":
                exportar_csv()
            case "6":
                eliminarGasto()
            case "7":
                print("¡Listo! Nos vemos.")
                break
            case _:
                print("Opción inválida, probá de nuevo.\n")


if __name__ == "__main__":
    cargarCSV()
    main()