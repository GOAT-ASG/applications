from os import system
from msvcrt import getwch
from random import randrange


class Stats:
    def __init__(self,hp,mn,at,df) -> None:
        self.attributes = {'hp':hp,'mn':mn,'at':at,'df':df}
        for attribute in self.attributes:
            setattr(self,attribute,self.attributes[attribute])

    def stats(self):
        string = ''
        for attribute in self.attributes:
            string += f'| {attribute.upper()} : {str(getattr(self,attribute))} '
        return string + '|\n'

    def take(self, damage):
        actual_damage = max(0, damage - self.df)
        self.hp -= actual_damage

        if self.hp <= 0:
            self.hp = 0
            return "DEATH"
        return f"Took {actual_damage} damage!"
    
    def increase(self):
        for attribute in self.attributes:
            setattr(self,attribute,int(getattr(self,attribute) * 1.5))


class Board:
    def __init__(self, width, height, diff) -> None:
        self.board = [["[ ]" for _ in range(width)] for _ in range(height)]
        self.board[randrange(height)][randrange(width)] = "[C]"
        self.board[0][0] = "[P]"
        self.board[-1][-1] = "[G]"
        self.enemy = [[None for _ in range(width)] for _ in range(height)]
        

        for _ in range(int(width * height / 25) - 1 + diff):
            while True:
                x, y = randrange(height), randrange(width)
                if self.board[x][y] == "[ ]":
                    self.board[x][y] = "[E]"
                    self.enemy[x][y] = Stats(50 * int(diff/2), 20 * int(diff/2), 15 * int(diff/2), 5 * int(diff/2))
                    break

    def show(self):
        print("*  -  ", end="")
        for i in range(len(self.board[0])):
            print(chr(65 + i), "  ", end="")
        print()
        for i, row in enumerate(self.board):
            row_num = f"{i:02d}"
            print(f"{row_num} -", str(row).replace("'", "").replace(",", "").replace("[[", "[").replace("]]", "]"))

    def move_player(self, action, player, current_level):
        direction_map = {"2": (1, 0), "4": (0, -1), "6": (0, 1), "8": (-1, 0)}
        dy, dx = direction_map.get(action, (0, 0))

        for i, row in enumerate(self.board):
            if "[P]" in row:
                j = row.index("[P]")
                new_i, new_j = i + dy, j + dx

                # Check bounds
                if not (0 <= new_i < len(self.board) and 0 <= new_j < len(self.board[0])):
                    print("Move out of bounds!")
                    return current_level

                # Process movement
                target_cell = self.board[new_i][new_j]
                if target_cell == "[ ]":
                    self.board[new_i][new_j] = "[P]"
                    self.board[i][j] = "[ ]"
                elif target_cell == "[E]":
                    enemy = self.enemy[new_i][new_j]
                    print(enemy.stats())
                    result = self.battle_turn(player, enemy)
                    if result == "ENEMY_DEFEATED":
                        self.board[new_i][new_j] = "[P]"
                        self.enemy[new_i][new_j] = None
                        self.board[i][j] = "[ ]"
                elif target_cell == "[C]":
                    player.increase()
                    self.board[i][j] = "[ ]"
                    self.board[new_i][new_j] = "[P]"
                elif target_cell == "[G]":
                    print("Level Up!")
                    return current_level + 1
                break
        return current_level

    @staticmethod
    def battle_turn(player, enemy):
        player.take(enemy.at)
        enemy.take(player.at)

        if enemy.hp <= 0:
            return "ENEMY_DEFEATED"
        if player.hp <= 0:
            print("You died!")
            exit()
        return "BATTLE_CONTINUES"


class Game:
    def __init__(self):
        self.difficulty = 1
        self.player = Stats(100, 50, 20, 10)
        self.level = 0
        self.arena = [Board(5, 5, self.difficulty)]

    def play(self):
        while True:
            system("cls")
            print(self.player.stats())
            print(f"Level: {self.level}")
            self.arena[self.level].show()

            move = getwch()
            if move in "2468":  # Valid inputs
                self.level = self.arena[self.level].move_player(move, self.player, self.level)

                # Level up
                if self.level >= len(self.arena):
                    self.arena.append(Board(5+int(self.level//2), 5+int(self.level//2), self.difficulty+self.level))


# Start the game
if __name__ == "__main__":
    game = Game()
    game.play()

