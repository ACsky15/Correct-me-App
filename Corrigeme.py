import tkinter as tk
from tkinter import scrolledtext
import language_tool_python


def corregir_texto():
    # Obtener el texto ingresado por el usuario
    texto_con_errores = cuadro_texto.get("1.0", tk.END)

    # Crear un objeto LanguageTool
    herramienta_correccion = language_tool_python.LanguageTool('es')

    # Obtener las correcciones sugeridas
    correcciones = herramienta_correccion.check(texto_con_errores)

    # Mostrar el texto original y las correcciones sugeridas
    if correcciones:
        texto_corregido = herramienta_correccion.correct(texto_con_errores)
        print("\nCorrecciones sugeridas:")
        for correccion in correcciones:
            print(f"- {correccion}")
        cuadro_texto_corregido.delete("1.0", tk.END)
        cuadro_texto_corregido.insert(tk.END, texto_corregido)
    else:
        cuadro_texto_corregido.delete("2.0", tk.END)
        cuadro_texto_corregido.insert(tk.END, "No se encontraron errores en el texto.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Corrígeme")
ventana.geometry("300x200")

ventana.config(bg="#75E3F9")

# Crear un cuadro de texto para ingresar texto
etiqueta_entrada = tk.Label(ventana, text="Ingrese el texto a corregir:", font=16, bg="#75E3F9")
etiqueta_entrada.pack(pady=10)

cuadro_texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=90, height=20, font=("Times", "12"), padx=30)
cuadro_texto.pack(pady=15)


# Crear un botón para corregir el texto
boton_corregir = tk.Button(ventana, text="Corregir Texto", command=corregir_texto, background="lavender")
boton_corregir.pack()

# Crear un cuadro de texto para mostrar el texto corregido
etiqueta_salida = tk.Label(ventana, text="Texto corregido:", font=16, bg="#75E3F9")
etiqueta_salida.pack(pady=10)

cuadro_texto_corregido = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=90, height=20, font=("Times", "12")
                                                   , padx=30)
cuadro_texto_corregido.pack(pady=15)

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()