import pygame, sys

pygame.init()

WIDTH, HEIGHT = 700, 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Connect 4')

BOARD = pygame.image.load('board.png')
GREEN = pygame.image.load('green.png')
RED = pygame.image.load('red.png')
FONT = pygame.font.SysFont('comicsans',64)

GREEN = pygame.transform.scale(GREEN, (60,60))
RED = pygame.transform.scale(RED, (60,60))

BG_COLOR = (214, 201, 227)
SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (60,50))

pygame.display.update()

#initial point (top-left 83,103)
# -> 81
#| 80
#y difference is 80
#x difference is 81

# event keys 1 to 7

board_list = [[True, True, True, True, True, True, True],
              [True, True, True, True, True, True, True],
              [True, True, True, True, True, True, True],
              [True, True, True, True, True, True, True],
              [True, True, True, True, True, True, True],
              [True, True, True, True, True, True, True]]

def display_button(turn, board_list,column):
    for i in range(6,0, -1):
        if board_list[5][column - 1] == True:
            board_list[5][column - 1] = turn
            x = 83 +81*(column - 1) 
            y = 103 + 80*(i -1) + 0.6 *(i-1)
            SCREEN.blit(turn,(x,y))
            pygame.display.update()
            break
    if turn == RED:
        turn == GREEN
    else:
        turn = RED
    return board_list

def display_text(turn):
    text = f'{turn.txt} has won!!'
    render_text = FONT.render(text, 1, (0,0,0))
    SCREEN.blit(render_text, (150,150))
    pygame.display.update()

def check_winner(board_list, turn):
    board_list = [[True, True, True, True, True, True, True],
                  [True, True, True, True, True, True, True],
                  [True, True, True, True, True, True, True],
                  [True, True, True, True, True, True, True],
                  [True, True, True, True, True, True, True],
                  [True, True, True, True, True, True, True]]
    turn_txt = ''
    if turn == RED:
        turn_txt = 'GREEN'
    else:
         turn_txt = 'RED'
         
    for i in range (6):
        for j in range (7):
            # HORIZONTAL CHECK
            if (j<=3):
                if (board_list[i][j] == board_list[i][j+1] == board_list[i][j+2] == board_list[i][j+3] and board_list[i][j] != True):
                    display_text(turn)
                    pygame.time.delay(10000)
                    return False

            #VERTICAL CHECK
            if (i<=2):
                if board_list[i][j] == board_list[i+1][j] == board_list[i+2][j] == board_list[i+3][j] and board_list[i][j] != True:
                    display_text(turn)
                    pygame.time.delay(10000)
                    return False

            # FIRST DIAGONAL CHECK
            if (i<=2) and (j<=3):
                if (board_list [i][j] == board_list[i+1][j+1] == board_list[i+2][j+2] == board_list == [i+3][j+3] and board_list != True):
                        display_text(turn)
                        pygame.time.delay(10000)
                        return False

            # SECOND DIAGONAL CHECK
            k = 6 - j
            if () and (k<=3):
                if (board_list [i][k] == board_list[i+1][k+1] == board_list[i+2][k+2] == board_list == [i+3][k+3] and board_list != True):
                        display_text(turn)
                        pygame.time.delay(10000)
                        return False





                

def main():
    turn = RED
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    turn,board_list = display_button (turn, board_list, 1)
                    status = check_winner(board_list, turn)
                if event.key == pygame.K_2:
                    turn,board_list = display_button (turn, board_list, 2)
                    status = check_winner(board_list, turn)
                if event.key == pygame.K_3:
                    turn,board_list = display_button (turn, board_list, 3)
                    status = check_winner(board_list, turn)
                if event.key == pygame.K_4:
                    turn,board_list = display_button (turn, board_list, 4)
                    status = check_winner(board_list, turn)
                if event.key == pygame.K_5:
                    turn,board_list = display_button (turn, board_list, 5)
                    status = check_winner(board_list, turn)
                if event.key == pygame.K_6:
                    turn,board_list = display_button (turn, board_list, 6)
                    status = check_winner(board_list, turn)
                if event.key == pygame.K_7:
                    turn,board_list = display_button (turn, board_list, 7)
                    status = check_winner(board_list, turn)

if __name__ == '__main__':
    main()
