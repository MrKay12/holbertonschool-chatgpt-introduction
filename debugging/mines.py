#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set()
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.first_move = True
        self.total_mines = mines
        self.revealed_count = 0

    def generate_mines(self, first_move_x, first_move_y):
        possible_positions = list(range(self.width * self.height))
        first_move_index = first_move_y * self.width + first_move_x
        possible_positions.remove(first_move_index)
        self.mines = set(random.sample(possible_positions, self.total_mines))

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if self.is_mine(x, y):
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def is_mine(self, x, y):
        return (y * self.width + x) in self.mines

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.is_mine(nx, ny):
                        count += 1
        return count

    def reveal(self, x, y):
        if self.first_move:
            self.generate_mines(x, y)
            self.first_move = False

        if self.revealed[y][x]:
            print("This cell is already revealed.")
            return True

        if self.is_mine(x, y):
            return False

        self.revealed[y][x] = True
        self.revealed_count += 1

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)

        return True

    def check_win(self):
        return self.revealed_count == self.width * self.height - self.total_mines

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input(f"Enter x coordinate (0 to {self.width-1}): "))
                y = int(input(f"Enter y coordinate (0 to {self.height-1}): "))

                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    print("Coordinates out of bounds. Please try again.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()