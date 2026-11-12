#La primera línea pregunta cuánto cuesta la compra y guarda esa cantidad en importe.
#La segunda pregunta cuánto dinero entrega el cliente y guarda esa cantidad en entregado.
importe = float(input("Importe de la compra €: "))
entregado = float(input("Dinero entregado €: "))

#Primero se resta el precio de la compra al dinero entregado y se convierte el resultado a céntimos. Después se muestra el cambio en euros.
#Luego se calcula cuántos billetes de 20 € hacen falta y se guarda lo que sobra para seguir calculando las demás monedas y billetes.
cambio = round((entregado - importe) * 100)

print("Cambio:", cambio / 100, "€")

billetes_20 = cambio // 2000
cambio = cambio % 2000

#Calcula cuántos billetes de 10 € hacen falta y en la segunda guarda lo que sobra después de apartarlos.
billetes_10 = cambio // 1000

#Calcula cuántos billetes de 50 € hacen falta y en la segunda guarda lo que sobra después de apartarlos.
monedas_50 = cambio // 50
cambio = cambio % 50
cambio = cambio % 1000

#Calcula cuántos billetes de 5 € hacen falta y en la segunda guarda lo que sobra después de apartarlos.
billetes_5 = cambio // 500
cambio = cambio % 500

#Calcula cuántos billetes de 2 € hacen falta y en la segunda guarda lo que sobra después de apartarlos.
monedas_2 = cambio // 200
cambio = cambio % 200

#Calcula cuántos billetes de 1 € hacen falta y en la segunda guarda lo que sobra después de apartarlos.
monedas_1 = cambio // 100
cambio = cambio % 100

#Calcula cuántos billetes de 20 € hacen falta y en la segunda guarda lo que sobra después de apartarlos.
monedas_20 = cambio // 20
cambio = cambio % 20

#Calcula cuántos billetes de 10 € hacen falta y en la segunda guarda lo que sobra después de apartarlos.
monedas_10 = cambio // 10
cambio = cambio % 10

#calcula cuántas monedas de 5 céntimos hacen falta. Como es la moneda más pequeña, ya no queda nada por calcular.
monedas_5 = cambio // 5

#La primera línea muestra cuántos billetes de 20 € hay que devolver y la segunda muestra cuántos billetes de 10 €.
print("Billetes de 20 €:", billetes_20)
print("Billetes de 10 €:", billetes_10)

#Estas líneas muestran cuántos billetes de 5 € y cuántas monedas de 2 €, 1 €, 50, 20, 10 y 5 céntimos hay que devolver.
print("Billetes de 5 €:", billetes_5)
print("Monedas de 2 €:", monedas_2)
print("Monedas de 1 €:", monedas_1)
print("Monedas de 50 céntimos:", monedas_50)
print("Monedas de 20 céntimos:", monedas_20)
print("Monedas de 10 céntimos:", monedas_10)
print("Monedas de 5 céntimos:", monedas_5)