# 6. Un vivero forestal actualiza cada seis meses los
# precios de la planta que vende en función de los
# valores oficiales de inflación mensual. Desean
# desarrollar un programa que proporcione el
# precio actualizado a partir del precio anterior
# y los valores de inflación.

def main():
    precio_anterior = float(input("Ingrese el precio anterior: $"))
    valor_inflacion = float(input("Ingrese el porcentaje del valor de inflación: %"))
    precio_actualizado = precio_anterior * (1 + (valor_inflacion / 100))
    print(f"El precio actualizado es: ${format(round(precio_actualizado), ',d')} pesos")
    print(f"El valor de la inflación es de: ${(valor_inflacion / 100) * precio_anterior} pesos")

if __name__ == "__main__":
    main()
    print("Fin del programa")
