def main():
    cad1 = input("Ingrese una cadena: ")
    cad2 = input("Ingrese una cadena: ")
    if cad2 in cad1:
        print("La segunda se encuentra dentro de la primera")
    else:
        print("La segunda NO se encuentra dentro de la primera")


if __name__ == "__main__":
    main()