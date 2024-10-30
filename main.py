import random

# Lista de palabras para el juego
lista_palabras = ['Python', 'Programacion', 'Computadora', 'Juego', 'Desarrollo', 
                  'Internet', 'Tecnologia', 'Innovacion', 'Aprendizaje', 'Divertido', 
                  'Algoritmo', 'Interactivo', 'Educacion', 'Creatividad', 'Proyecto']

# Función para seleccionar una palabra y mantener letras adivinadas
def seleccionar_palabra():
    return random.choice(lista_palabras).lower()

# Función para mostrar la palabra con guiones bajos para letras no adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    mostrar = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            mostrar += letra + ' '
        else:
            mostrar += '_ '
    return mostrar

# Función principal del juego
def jugar():
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6  # Intentos permitidos
    
    print(f'Palabra: {mostrar_palabra(palabra, letras_adivinadas)}')
    
    while intentos_restantes > 0:
        letra = input('Introduce una letra: ').lower()
        
        if len(letra) != 1:
            print("Por favor, introduce una única letra.")
            continue
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(letra)

        # Mostrar palabra con letras adivinadas
        palabra_mostrada = mostrar_palabra(palabra, letras_adivinadas)
        print(f'Palabra: {palabra_mostrada}')
        
        # Comprobar si la letra está en la palabra
        if letra not in palabra:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")
        
        # Verificar si el jugador adivinó toda la palabra
        if '_' not in palabra_mostrada:
            print("¡Felicidades! Has adivinado la palabra.")
            break
    else:
        print(f"Lo siento, te has quedado sin intentos. La palabra era '{palabra}'.")
