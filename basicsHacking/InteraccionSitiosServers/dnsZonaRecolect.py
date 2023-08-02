import dns.resolver

ConsultasDNS = {
    "Host Address": "A",
    "Authoritative name server": "NS",
    "Mail destination": "MD",
    "Mail forwarder": "MF",
    "Canonical name for an alias": "CNAME",
    "Start of a zone of authority": "SOA",
    "Mailbox domain name": "MB",
    "Mail group member": "MG",
    "Mail rename domain name": "MR",
    "Null RR": "NULL",
    "Well known service description": "WKS",
    "Domain name pointer": "PTR",
    "Host information": "HINFO",
    "Mailbox or mail list information": "MINFO",
    "Mail exchange": "MX",
    "Text strings": "TXT",
    "Transfer of an entire zone": "AXFR",
    "Mailbox-related records": "MAILB",
    "Mail agent RR": "MAILA",
    "All records": "ANY",
}
errores=[]
def main():
    try:
        web = input("Ingresa la web a analizar: ")
        for descripcion, valor in ConsultasDNS.items():
            try:
                a = dns.resolver.resolve(web, valor)
                print("Consulta: " + descripcion+" : "+valor)
                for q in a:
                    print(q)
                print("********************")
            except dns.resolver.NoAnswer:
                errores.append("NoAnswer: "+web+" : "+ descripcion+" : "+valor)	
            except dns.resolver.NXDOMAIN:
                errores.append("NXDOMAIN: "+"No se encontró el dominio "+web+" : "+ descripcion+" : "+valor)	
            except:
                errores.append("No se puede conectar para la consulta: "+web+" : "+ descripcion+" : "+valor)

    except KeyboardInterrupt:
        print("Saliendo...")
    finally:
        print("********************")
        print("ERRORRES: ")
        for error in errores:
            print(error)


if __name__ == '__main__':
    main()