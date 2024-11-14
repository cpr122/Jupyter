def generar_codigo(nombre_variable):
    codigo = f"{nombre_variable} = 5"
    return codigo

nombre_variable = "x"
codigo = generar_codigo(nombre_variable)
exec(codigo)
print(x)  # Salida: 5
