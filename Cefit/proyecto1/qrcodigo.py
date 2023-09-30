# 1. Generador de Códigos QR: Implementa un generador de códigos QR que convierta texto o enlaces en códigos QR.
import qrcode
import tkinter

def generar_codigo_qr(texto, nombre_archivo):
    # Crea un objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Agrega el texto o enlace al código QR
    qr.add_data(texto)
    qr.make(fit=True)

    # Crea una imagen del código QR y guárdala en un archivo
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)

if __name__ == "__main__":
    texto = input("Ingrese el texto o enlace que desea convertir en código QR: ")
    nombre_archivo = input("Ingrese el nombre del archivo de imagen de salida (por ejemplo, codigo_qr.png): ")

    generar_codigo_qr(texto, nombre_archivo)
    print(f"Se ha generado el código QR y se ha guardado en {nombre_archivo}")
