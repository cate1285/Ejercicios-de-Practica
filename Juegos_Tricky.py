import random
def dibujarTablero(tablero):
    print("     |     |")
    print("   ",tablero[7] + "|"+ tablero [8] , "   |" , tablero[9])
    print("     |     |")
    print("-------------------")
    print("     |     |")
    print("   " ,tablero [4] +"|"+tablero [5]  , "   |" , tablero[6])
    print("     |     |")
    print("-------------------")
    print("     |     |")
    print("  " ,tablero [1] ,"|",tablero [2] , "  |" , tablero[3])
    print("     |     |")

def ingresaLetraJugador():
    letra=""
    while not (letra=="X" or letra=="O"):
        print("¿Quiere ser X o O?")
        letra = input().upper()
    if letra == "X":
        return ["X","O"]
    else:
        return ["O","X"]
    
def quienComienza():
    if random.randint(0,1) ==0:
        return "La computadora"
    else:
        return "El jugador"

  

def hacerJugada(tablero,letra,jugada):
    tablero[jugada] = letra

def esGanador (tablero,letra):
    return ((tablero[4] == letra and tablero[5]==letra and tablero[6]==letra)or
           (tablero[1] == letra and tablero[2]==letra and tablero[3]==letra)or
           (tablero[7] == letra and tablero[4]==letra and tablero[1]==letra)or
           (tablero[8] == letra and tablero[5]==letra and tablero[2]==letra)or
           (tablero[9] == letra and tablero[6]==letra and tablero[3]==letra)or
           (tablero[7] == letra and tablero[5]==letra and tablero[3]==letra)or
           (tablero[7] == letra and tablero[5]==letra and tablero[3]==letra))
    

def obtenerDuplicadoTablero(tablero):
    dupTablero= []
    for i in tablero:
        dupTablero.append(i)
    return dupTablero
def hayEspacioLibre(tablero,jugada):
    return tablero [jugada] == " "

def obtenerJugadaJugador(tablero):
    jugada = " "
    while jugada not in  "1 2 3 4 5 6 7 8 9".split() or not hayEspacioLibre(tablero,int(jugada)):
        print("cual es tu proxima jugada?(1-9)")
        jugada = input()
    return int(jugada)
    
def elegirAzarDeLista(tablero,listaJugada):
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)
    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None

    
def obtenerJugadaComputadora(tablero,letraComputadora):
    if letraComputadora == "X":
        letraJugador="O"
        
    else:
        letraJugador ="X"
        
    for i in range (1, 10):
        copia =obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia,i):
            hacerJugada(copia,letraComputadora,i)
            if esGanador(copia,letraComputadora):
                return i
    for i in range(1, 10):
      copia = obtenerDuplicadoTablero(tablero)
      if hayEspacioLibre(copia, i):
        hacerJugada(copia,letraComputadora,i)
        if esGanador (copia, letraJugador):
          return i
            
    jugada = elegirAzarDeLista(tablero, [1,3,7,9])
    if jugada != None :
      return jugada
    
    elif hayEspacioLibre(tablero , 5):
      return 5
    
    else:
      elegirAzarDeLista(tablero, [2,4,6,8])

def tableroCompleto(tablero):
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True

def jugarDeNuevo():
    print("¿Jugar de nuevo? si /no")
    return input().lower().startswith("s")

print("esto es tricky")
while True:
    tablero=[" "] * 10
    letraJugador, letraComputadora = ingresaLetraJugador()
    turno =quienComienza()
    print(turno + " primero")
    juegoEnCurso = True
    
    while juegoEnCurso:
        if turno == "El jugador":
            dibujarTablero(tablero)
            jugada =obtenerJugadaJugador(tablero)
            hacerJugada(tablero,letraJugador,jugada)
            
            if esGanador (tablero, letraJugador):
                dibujarTablero(tablero)
                print("ganaste")
                juegoEnCurso=False
            
            else:
                if tableroCompleto(tablero):
                    dibujarTablero(tablero)
                    print("Es un empate")
                    break
                else:
                    turno ="La computadora"
                
        else:
            jugada = obtenerJugadaComputadora(tablero,letraComputadora)
            hacerJugada(tablero,letraComputadora,jugada)
            
            if esGanador(tablero,letraComputadora):
                dibujarTablero(tablero)
                print("la computadora gano")
                juegoEnCurso = False
            else:
                if tableroCompleto(tablero):
                    dibujarTablero(tablero)
                    print("empate")
                    break
                else:
                    turno="El jugador"

    if not jugarDeNuevo():
      break