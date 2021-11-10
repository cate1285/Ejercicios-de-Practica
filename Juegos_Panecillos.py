from random import randint


def convertiralista(numero):
  res = [str(i) for i in str(numero)]
  return res

def adivinarelnumero():
  lista_adivinarelnumero=[]
  x=input("Que numero crees que es?")
  for u in x:
    lista_adivinarelnumero.append(u)
  return lista_adivinarelnumero



def validarnumero():
  if len(lista_adivinarelnumero) != 3:
    print("debe ser un numero de 3 digitos")
    juego_en_curso=True

def position1(lista_numero_azar,lista_adivinarelnumero):
  while True:
    juego_en_curso
    pista=[]
    for i in range(len(lista_adivinarelnumero)):
      if lista_adivinarelnumero[i]== lista_numero_azar[i]:
        print("fermi")
        pista.append("fermi")
      elif lista_adivinarelnumero[i] in lista_numero_azar:
        pista.append("Pico")
        print("Pico")
    if len(pista)== 0:
      print("panecillos")
    break

def jugarnuevamente():
  jugar=("Quieres jugar Otra Vez? si/no")
  return input(jugar).lower().startswith("s") 





print("Esto es el juego de panecillos")
digitosNum= 3
MAXADIVINANZAS=10
print("Estoy pensando en un numeroo de %s digitos. Intenta adivinar cual es." % (digitosNum))
print("Aqui hay algunas pistas:")
print("Cuando digo: Eso significa::")
print("Pico   Un digito es correcto pero en la posicion incorrecta")
print("Fermi   Un digito es correcto y en la posicion correcta.")
print("Panecillos   Ningun digito es correcto.")



while True:
  juego_en_curso=True
  numero=randint(100,900)

  while juego_en_curso:
    

    lista_numero_azar=convertiralista(numero)
    lista_adivinarelnumero=adivinarelnumero()
    validarnumero()
    
    if lista_numero_azar== lista_adivinarelnumero:
      print("ganaste")
      break
    elif lista_numero_azar!= lista_adivinarelnumero:
      position1(lista_numero_azar,lista_adivinarelnumero)
      juego_en_curso=True

    else:
      print("perdiste " +"el numero era "+ str(numero))
      break

  if not jugarnuevamente():
    break