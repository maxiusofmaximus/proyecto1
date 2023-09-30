# 1. Generador de Códigos QR: Implementa un generador de códigos QR que convierta texto o enlaces en códigos QR.
import tkinter as tk
from PIL import Image, ImageTk
import qrcode

def generar_codigo_qr(texto, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)

def mostrar_codigo_qr(texto):
    ventana = tk.Tk()
    ventana.title("Código QR")

    # Genera el código QR y lo guarda en un archivo
    nombre_archivo = "codigo_qr.png"
    generar_codigo_qr(texto, nombre_archivo)

    # Carga la imagen PNG en un objeto PhotoImage de Tkinter
    imagen = Image.open(nombre_archivo)
    foto = ImageTk.PhotoImage(imagen)

    # Crea un Label para mostrar la imagen
    label_imagen = tk.Label(ventana, image=foto)
    label_imagen.pack()

    ventana.mainloop()

if __name__ == "__main__":
    texto = input("Ingrese el texto o enlace que desea convertir en código QR: ")
    mostrar_codigo_qr(texto)
