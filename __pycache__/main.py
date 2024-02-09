import random
import time
from Juego import cargar_laberintos, string_to_matrix
from Juego import Juego

def main():
    playerName = input("Hi, waht's your name? ").upper()
    map_dir = "Utils/maps"
    laberintos = cargar_laberintos(map_dir)
    
    if not laberintos:
        print("No mazes were found in the 'maps' folder.")
        return
    chosen_map_data = random.choice(laberintos)
    map_matrix = string_to_matrix(chosen_map_data)

    start_pos = (0, 0)
    end_pos = (len(map_matrix[0]) - 1, len(map_matrix) - 1)

    game = Juego(map_matrix, start_pos, end_pos, playerName)
    game.greet()
    time.sleep(2)
    game.play()

if __name__ == "__main__":
    main()