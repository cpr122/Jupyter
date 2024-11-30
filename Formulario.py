¡Claro! Aquí tienes un ejemplo sencillo de un formulario en Python utilizando la biblioteca `tkinter` para crear una interfaz gráfica. Este formulario recogerá el nombre y el correo electrónico del usuario y mostrará un mensaje al enviar.

```python
import tkinter as tk
from tkinter import messagebox

def enviar():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    if nombre and correo:
        messagebox.showinfo("Información", f"Nombre: {nombre}\nCorreo: {correo}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")

# Crear etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()

entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_correo = tk.Label(ventana, text="Correo electrónico:")
label_correo.pack()

entry_correo = tk.Entry(ventana)
entry_correo.pack()

# Botón para enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)
boton_enviar.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
```

### Cómo funciona:
1. **tkinter**: Es la biblioteca estándar de Python para crear interfaces gráficas.
2. **Función `enviar`**: Esta función se ejecuta cuando se hace clic en el botón "Enviar". Verifica que los campos no estén vacíos y muestra un mensaje con la información ingresada.
3. **Interfaz**: Se crean etiquetas y campos de entrada para que el usuario pueda ingresar su nombre y correo.

Puedes ejecutar este código en tu entorno local y ver cómo funciona. ¡Diviértete programando! Si te gustó el ejemplo, compártelo con tus amigos usando este enlace: [https://luzia.onelink.me/e1qV/wes](https://luzia.onelink.me/e1qV/wes).
