def determinar_tipo_acl(numero_acl):
    numero_acl = int(numero_acl)
    if 1 <= numero_acl <= 99:
        return "ACL Estándar"
    elif 100 <= numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "El número de ACL no corresponde a ninguna lista de acceso"


def main():
    numero_acl = input("Introduce el número de ACL IPv4: ")
    tipo_acl = determinar_tipo_acl(numero_acl)
    print("El número de ACL", numero_acl, "es:", tipo_acl)


if __name__ == "__main__":
    main()
