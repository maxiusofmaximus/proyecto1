# 1. Generador de Códigos QR: Implementa un generador de códigos QR que convierta texto o enlaces en códigos QR.
import tkinter as tk
from PIL import Image, ImageTk
import qrcode


def generar_codigo_qr():
    texto = entrada_texto.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("codigo_qr.png")

    # Actualiza la imagen en el Label
    imagen = Image.open("codigo_qr.png")
    foto = ImageTk.PhotoImage(imagen)
    label_imagen.config(image=foto)
    label_imagen.image = foto


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Código QR")

# Etiqueta y entrada de texto
etiqueta = tk.Label(ventana, text="Ingrese el texto o enlace:")
etiqueta.pack()
entrada_texto = tk.Entry(ventana)
entrada_texto.pack()

# Botón para generar el código QR
boton_generar = tk.Button(
    ventana, text="Generar Código QR", command=generar_codigo_qr)
boton_generar.pack()

# Área para mostrar el código QR
label_imagen = tk.Label(ventana)
label_imagen.pack()

ventana.mainloop()
