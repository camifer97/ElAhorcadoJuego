import random
from words import words
import string
from visual import visual_vidas

# Mientras haya "-" o " " dentro de la palabra, sigue iterando hasta obtener otra palabra valida. 
def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) #crea un set con las letras de la palabra elegida.
    alphabet = set(string.ascii_uppercase) #crea un set con todas las letras del abecedario en mayusucula.
    used_letters = set() #almacena todas las letras elegidas por el usuario.

    lives = 7
    print("""
            =========================================
                Bienvenido al juego del ahorcado!
            =========================================""")
    while len(word_letters) > 0 and lives > 0: 
        print(f'Tienes {lives} vidas, y has usado las siguientes letras: ',' '.join(used_letters)) #Muestra todas las letras ingresadas hasta el momento y las une con un join separandolas por un espacio.

        #crea la variable letter para chequear si la letra ingresada por el player se encuentra dentro de la palabra a adivinar.
        #si no la encuentra, entonces reemplaza el espacio por '-'
        word_list = [letter if letter in used_letters else '-' for letter in word] 

        print('Palabra actual: ',' '.join(word_list)) #Muestra los caracteres de la palabra actual (letras y '-') y los une en una lista iterable con join.
        
        
        user_letter = input("Ingrese una letra: ").upper() #Le pido al usuario que ingrese una letra

        if user_letter in alphabet - used_letters: #Si la letra ingresada esta dentro del abecedario y aun NO LA USE (and is not used_letter), entonces la agrego al set de letras ya utilizadas por el usuario.
            used_letters.add(user_letter)

            if user_letter in word_letters: #Si la palabra elegida por el programa contiene la letra ingresada, entonces se elimina de la palabra.
                word_letters.remove(user_letter)
            else:
                print(visual_vidas[lives])
                lives = lives - 1 #Si la letra ingresada no se encuentra en la palabra, entonces el player pierde una vida.
                
                print(f'La letra {user_letter} no se encuentra en la palabra. Has perdido una vida :(')

    
        elif user_letter in used_letters: 
            print("La letra ingresada ya fue utilizada. Intente nuevamente. ")
    
        else:
            print("El caracter ingresado no es valido. Intente nuevamente. ")
    
    if lives == 0:
        print(f"Has perdido el juego! La palabra era {word}.")
    else:
        print(f"Felicitaciones, ganaste el juego! :) la palabra era {word}.")
    
hangman()
