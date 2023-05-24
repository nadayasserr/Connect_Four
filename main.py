import random
import numpy as np
import pygame
import sys
import math
from tkinter import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED= (255, 0, 0)
YELLOW= (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

COMPUTER = 0
AI = 1

PLAYER_PIECE = 1
AI_PIECE = 2

window_length = 4

empty = 0

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)

frame = Tk()
frame.title("Connect Four")
frame.minsize(430, 250)

label1 = Label(text="Please Choose the algorithm type with the difficulty level of the game", fg="red")
label1.pack()


def minimax_easy():
    board = create_board()
    print_board(board)
    game_over = False

    pygame.init()

    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(COMPUTER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if event.type == pygame.MOUSEMOTION:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     posx = event.pos[0]
            #     if turn == COMPUTER:
            #         pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            #
            # pygame.display.update()
            #
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     # print(event.pos)

        #  Ask for COMPUTER Input
        if turn == COMPUTER:
            col = random.randint(0, COLUMN_COUNT -1)
            # posx = event.pos[0]
            # col = int(math.floor(posx / SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)

                if winning_move(board, PLAYER_PIECE):
                    label = myfont.render("COMPUTER wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True

                turn += 1
                turn = turn % 2

                print_board(board)
                draw_board(board)

        # Ask for AI Input
        if turn == AI and not game_over:
            # col = random.randint(0,COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            col, minimax_score = minimax(board, 3, True)

            if is_valid_location(board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = myfont.render("AI wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)


def minimax_medium():
    board = create_board()
    print_board(board)
    game_over = False

    pygame.init()

    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(COMPUTER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if event.type == pygame.MOUSEMOTION:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     posx = event.pos[0]
            #     if turn == COMPUTER:
            #         pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            #
            # pygame.display.update()
            #
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     # print(event.pos)

        #  Ask for COMPUTER Input
        if turn == COMPUTER:
            col = random.randint(0, COLUMN_COUNT - 1)
            # posx = event.pos[0]
            # col = int(math.floor(posx / SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)

                if winning_move(board, PLAYER_PIECE):
                    label = myfont.render("COMPUTER wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True

                turn += 1
                turn = turn % 2

                print_board(board)
                draw_board(board)

        # Ask for AI Input
        if turn == AI and not game_over:
            # col = random.randint(0,COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            col, minimax_score = minimax(board, 5, True)

            if is_valid_location(board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = myfont.render("AI wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)


def minimax_hard():
    board = create_board()
    print_board(board)
    game_over = False

    pygame.init()

    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(COMPUTER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if event.type == pygame.MOUSEMOTION:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     posx = event.pos[0]
            #     if turn == COMPUTER:
            #         pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            #
            # pygame.display.update()
            #
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     # print(event.pos)

        #  Ask for COMPUTER Input
        if turn == COMPUTER:
            col = random.randint(0, COLUMN_COUNT - 1)
            # posx = event.pos[0]
            # col = int(math.floor(posx / SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)

                if winning_move(board, PLAYER_PIECE):
                    label = myfont.render("COMPUTER wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True

                turn += 1
                turn = turn % 2

                print_board(board)
                draw_board(board)

        # Ask for AI Input
        if turn == AI and not game_over:
            # col = random.randint(0,COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            col, minimax_score = minimax(board, 6, True)

            if is_valid_location(board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = myfont.render("AI wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)


def alphabeta_easy():
    board = create_board()
    print_board(board)
    game_over = False

    pygame.init()

    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(COMPUTER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if event.type == pygame.MOUSEMOTION:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     posx = event.pos[0]
            #     if turn == COMPUTER:
            #         pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            #
            # pygame.display.update()
            #
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     # print(event.pos)

        # Ask for COMPUTER Input
        if turn == COMPUTER:
            col = random.randint(0, COLUMN_COUNT - 1)
            # posx = event.pos[0]
            # col = int(math.floor(posx / SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)

                if winning_move(board, PLAYER_PIECE):
                    label = myfont.render("COMPUTER wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True

                turn += 1
                turn = turn % 2

                print_board(board)
                draw_board(board)

        # Ask for AI Input
        if turn == AI and not game_over:
            # col = random.randint(0,COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            col, alphabeta_score = alpha_beta_pruning(board, 3, -math.inf, math.inf, True)

            if is_valid_location(board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = myfont.render("AI wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)


def alphabeta_medium():
    board = create_board()
    print_board(board)
    game_over = False

    pygame.init()

    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(COMPUTER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if event.type == pygame.MOUSEMOTION:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     posx = event.pos[0]
            #     if turn == COMPUTER:
            #         pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            #
            # pygame.display.update()
            #
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     # print(event.pos)

        #  Ask for COMPUTER Input
        if turn == COMPUTER:
            col = random.randint(0, COLUMN_COUNT - 1)
            # posx = event.pos[0]
            # col = int(math.floor(posx / SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)

                if winning_move(board, PLAYER_PIECE):
                    label = myfont.render("COMPUTER wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True

                turn += 1
                turn = turn % 2

                print_board(board)
                draw_board(board)

        # Ask for AI Input
        if turn == AI and not game_over:
            # col = random.randint(0,COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            col, alphabeta_score = alpha_beta_pruning(board, 5, -math.inf, math.inf, True)

            if is_valid_location(board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = myfont.render("AI wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)


def alphabeta_hard():
    board = create_board()
    print_board(board)
    game_over = False

    pygame.init()

    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(COMPUTER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # if event.type == pygame.MOUSEMOTION:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     posx = event.pos[0]
            #     if turn == COMPUTER:
            #         pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            #
            # pygame.display.update()
            #
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #     # print(event.pos)

        # Ask for COMPUTER Input
        if turn == COMPUTER:
            col = random.randint(0, COLUMN_COUNT - 1)
            # posx = event.pos[0]
            # col = int(math.floor(posx / SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)

                if winning_move(board, PLAYER_PIECE):
                    label = myfont.render("COMPUTER wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True

                turn += 1
                turn = turn % 2

                print_board(board)
                draw_board(board)

        # Ask for AI Input
        if turn == AI and not game_over:
            # col = random.randint(0,COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            col, alphabeta_score = alpha_beta_pruning(board, 7, -math.inf, math.inf, True)

            if is_valid_location(board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = myfont.render("AI wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)


radiovar = IntVar()
Radiobutton(frame, text="Minimax Easy", variable=radiovar, value=1, fg="blue").pack()
Radiobutton(frame, text="Minimax Medium", variable=radiovar, value=2, fg="blue").pack()
Radiobutton(frame, text="Minimax Hard", variable=radiovar, value=3, fg="blue").pack()
Radiobutton(frame, text="Alpha-Beta Pruning Easy", variable=radiovar, value=4, fg="blue").pack()
Radiobutton(frame, text="Alpha-Beta Pruning Medium", variable=radiovar, value=5, fg="blue").pack()
Radiobutton(frame, text="Alpha-Beta Pruning Hard", variable=radiovar, value=6, fg="blue").pack()


def selected():
    if radiovar.get() == 1:
        minimax_easy()
    elif radiovar.get() == 2:
        minimax_medium()
    elif radiovar.get() == 3:
        minimax_hard()
    elif radiovar.get() == 4:
        alphabeta_easy()
    elif radiovar.get() == 5:
        alphabeta_medium()
    elif radiovar.get() == 6:
        alphabeta_hard()


btn = Button(text='Choose', fg="red", command=selected)
btn.pack()

# btn1 = Radiobutton(text='Minimax Easy', command=minimax_easy)
# btn1.pack()
#
# btn2 = Radiobutton(text='Minimax Medium', command=minimax_medium)
# btn2.pack()
#
# btn3 = Radiobutton(text='Minimax Hard', command=minimax_hard)
# btn3.pack()
#
# btn4 = Radiobutton(text='Alpha-beta pruning Easy', command=alphabeta_easy)
# btn4.pack()
#
# btn5 = Radiobutton( text='Alpha-beta pruning Medium', command=alphabeta_medium)
# btn5.pack()
#
# btn6 = Radiobutton(text='Alpha-beta pruning Hard', command=alphabeta_hard)
# btn6.pack()


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


def evaluate_window(window, piece):
    # opponent piece
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    score = 0
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(empty) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(empty) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(empty) == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0
    # score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+window_length]
            score += evaluate_window(window, piece)

    # score vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+window_length]
            score += evaluate_window(window, piece)

    # score positive sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+i][c+i] for i in range(window_length)]
            score += evaluate_window(window, piece)

    # score negative sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(window_length)]
            score += evaluate_window(window, piece)
    return score


def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0


def minimax(board, depth, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 1000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -1000000000000)
            else:  # game is over , no more valid moves
                return (None, 0)
        else:  # depth is zero
            return (None, score_position(board, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            # new_score = max(value, minimax(b_copy, depth-1, True))
            new_score = minimax(b_copy, depth-1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value

    else:  # minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            # new_score = min(value, minimax(b_copy, depth-1, True))
            new_score = minimax(b_copy, depth-1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value


def alpha_beta_pruning(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 1000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -1000000000000)
            else:  # game is over , no more valid moves
                return (None, 0)
        else:  # depth is zero
            return (None, score_position(board, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            # new_score = max(value, minimax(b_copy, depth-1, True))
            new_score = alpha_beta_pruning(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            # new_score = min(value, minimax(b_copy, depth-1, True))
            new_score = alpha_beta_pruning(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def pick_best_move(board, piece):
    best_score = -10000
    valid_locations = get_valid_locations(board)
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


frame.mainloop()
