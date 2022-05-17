
# rock, paper, and scissors -- these are the moves a player can make
# two player game -- players make their moves simultaneously
# each player can either win, lose, or draw during each play

# to win: make a move that beats the opposing player's move
# to lose: make a move that cannot beat the opposing player's move
# to draw: make the same move as the opposing player

# player -> opponent
# to win: scissors -> paper, rock -> scissors, paper -> rock
# to lose: paper -> scissors, scissors -> rock, rock -> paper
# to draw: paper -> paper, scissors -> scissors, rock -> rock

# the two players: (1) the person who gives an input, (2) computer
# this is a two player game, but only one person can use the program, since they are competing against the computer (second player/opponent)
import random

w = 0
l = 0
d = 0

while True:

    player_move = input("Enter a move rock(r), paper(p) or scissors(s) -- or quit(q): ")
    computer_move = random.choice(['r', 'p', 's'])

    # quitting the game
    if player_move == 'q':
        break

    # show what the two players' moves are
    print("Player move: {}, Computer move: {}".format(player_move, computer_move))

    # compare the moves of the player and computer
    if player_move == computer_move:
        d = d + 1 # incrementing the draw statistic; can also use d += 1
        print("Draw")
    elif (player_move == 's' and computer_move == 'p') or (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r'):
        w = w + 1
        print("You win")
    elif (player_move == 'p' and computer_move == 's') or (player_move == 's' and computer_move == 'r') or (player_move == 'r' and computer_move == 'p'):
        l = l + 1
        print("You lose")
    else:
        print("Invalid move, select r, p, s, or q.")

print("Wins: {}, Losses: {}, Draws: {}".format(w, l, d))