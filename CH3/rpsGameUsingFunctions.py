
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


def print_moves(p1_move, p2_move):
    print("Player 1 move: {}, Player 2 move: {}".format(p1_move, p2_move))

def get_player_move():
    acceptable_moves = ['r', 'p', 's', 'q']
    move = input("Enter a move rock(r), paper(p) or scissors(s) -- or quit(q): ")
    
    while move not in acceptable_moves:
        move = input("Invalid selection. Please enter a valid move [r, p, s, q]: ")

    return move

def evaluate_moves(p1_move, p2_move, stats):
    if p1_move == p2_move:
        stats['d'] += 1
        print("Draw")
    elif (p1_move == 's' and p2_move == 'p') or (p1_move == 'r' and p2_move == 's') or (p1_move == 'p' and p2_move == 'r'):
        stats['w'] += 1
        print("You win")
    elif (p1_move == 'p' and p2_move == 's') or (p1_move == 's' and p2_move == 'r') or (p1_move == 'r' and p2_move == 'p'):
        stats['l'] += 1
        print("You lose")

def print_statistics(stats):
    w = stats['w']
    l = stats['l']
    d = stats['d']
    print("Wins: {}, Losses: {}, Draws: {}".format(w, l, d))

# dictionary to keep track of game statistics
stats = {'w': 0, 'l': 0, 'd': 0}

while True:

    player_move = get_player_move()
    computer_move = random.choice(['r', 'p', 's'])

    # quitting the game
    if player_move == 'q':
        break

    # show what the two players' moves are
    print_moves(player_move, computer_move)

    # compare the moves of the player and computer
    evaluate_moves(p1_move=player_move, p2_move=computer_move, stats=stats)

print_statistics(stats)