class autores0559():
    id_autor=0
    Nombre=" "
    Apellidos=" "
    libros_escritos=0
    contacto=" "
    pais=" "
    Popularidad=" "
    def datos_A(selft):
        print(f"Id del autor: {Autoex.id_autor}")
        print(f"Nombre del autor: {Autoex.Nombre} ")
        print(f"Apellido del autor: {Autoex.Apellidos}")
        print(f"Libros escritos: {Autoex.libros_escritos}")
        print(f"Contacto del autor: {Autoex.contacto}")
        print(f"Pais del autor: {Autoex.pais}")
        print(f"Popularidad del autor: {Autoex.Popularidad}")
        
    def list_prov(selft):
        prov=["Casa del buo","Amigos lectores","Portal de libros","Libros magicos","Lector ES"]
        for m in prov:
            print(m)
    def tupla_libros(selft):
        lib=("Mi culpa","Trampa es ley","Mala mia","Brisa","Bufon")
        for x in lib:
            print(x)
        
    def diccionario_Sucursales(selft):
        vent={
            "Libros magicos":"  calle 3 de mayo,100",
            "Tienda de libros":" calle verdura,1090",
            "Libreria Paraiso":"  calle 5 de abril,980",
            "Libreria del mañana":" calle naranja,7890",
            "Tienda de libros 2":"  calle 5 de julio,4568"
        }
        for x, y in vent.items():
            print(x,y)
            
    def altas(selft):
        print("Los datos se guardaron correctamnete..")
    
    def bajas(selft):
        print("Los datos fueron borrados correctamente..")   
        
Autoex=autores0559()

print("--Datos del auntor--")
Autoex.id_autor=1234567
Autoex.Nombre="Vannesa"
Autoex.Apellidos="Morales"
Autoex.libros_escritos=7
Autoex.contacto="VaneM@gmail.com"
Autoex.pais="Mexico"
Autoex.Popularidad="Media"
Autoex.datos_A()
print("--Proveedores de los libros--")
Autoex.list_prov()
print("--Libros en venta--")
Autoex.tupla_libros()
print("--Sucursales--")
print("Sucursal"," ","       Direccion")
Autoex.diccionario_Sucursales()
Autoex.altas()
Autoex.bajas()