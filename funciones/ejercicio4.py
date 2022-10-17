def facturaSinIva(total_factura, IVA_FALTANTE):
    total_sin_iva = total_factura+(total_factura*IVA_FALTANTE)/100
    print(total_sin_iva)

def factura(total_factura, IVA):
    total = total_factura+(total_factura*IVA)/100
    print(total)

def main():
    total_factura = int(input("Cuanto es la factura?\n"))
    
    agregar = print("Desea Agregar IVA? 1- Si. 2- No\n")
    if agregar == 1:
        IVA = print("Cuanto es su IVA?\n")
        factura(total_factura, IVA)
    else:
        facturaSinIva(total_factura, 21)


if __name__ == "__main__":
    main()
