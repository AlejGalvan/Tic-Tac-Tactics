import pygame, sys
import random

# will eventuall pass which boss is being faced
# will need to create a function for each boss
# will need a function for each ability

# Work in progress
# def __init__(self, player_abilites, opponent_abilites, bg_surf, fonts):
    #     self.display_surface = pygame.display.get_surface()
    #     self.bg_surf = bg_surf
    #     self.player_abilites = player_abilites
    #     self.opponent_abilites = opponent_abilites
    #     self.fonts = fonts
    #     self.ability_data = {'player': player_abilites, 'opponent': opponent_abilites}

    # #def setup(self):

    # def update(self, dt):
    #     #outputs background, currently don't have background
    #     self.display_surface.blit(self.bg_surf, (0,0))
class Battle:

    # pass a screen to the function
    # should eventually also pass each image so we are not being redundant
    def __init__(self, SCREEN, BOARD, X_IMG, O_IMG, FONT, gametype):
        # load font
        # FONT = pygame.font.Font()
        # load board
        # BOARD = pygame.image.load()
        # load image
        # X_IMG = pygame.image.load()
        # load image
        # O_IMG = pygame.image.load()

        self.SCREEN = SCREEN
        self.BOARD = BOARD
        self.X_IMG = X_IMG
        self.O_IMG = O_IMG
        self.FONT = FONT
        self.BG_COLOR = (214, 201, 227)

        if gametype == "threebythree":
            self.threebythree()
        else:
            self.fivebyfive()

    # need to implement function that clears the board
    def fivebyfive(self):
        self.board = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],
                      [16,17,18,19,10], [21,22,23,24,25]]
        self.graphical_board = [[[None, None] for _ in range(5)] for _ in range(5)]

        self.to_move = 'X'

        self.SCREEN.fill(self.BG_COLOR)
        self.SCREEN.blit(self.BOARD, (64, 64))

        pygame.display.update()
        game_finished = False
        con = True
        escape = True

        while escape:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and con:
                    self.board, self.to_move = self.add_XO_fivebyfive(self.board, self.graphical_board, self.to_move)

                    result = self.check_win_fivebyfive(self.board)
                    if result is not None:
                        game_finished = True
                        if result == "DRAW":
                            print("Game ended in a draw")
                            con = True # stop taking moves
                        else:
                            print(f"{result} wins!")
                            con = False # stop taking moves
                        pygame.display.update()
                        continue

                    # AI's move (if game is not finished)
                    if not game_finished and self.to_move == 'O':
                        self.board, self.to_move = self.ai_move_fivebyfive(self.board, self.graphical_board, self.to_move)

                        result = self.check_win_fivebyfive(self.board)
                        if result is not None:
                            game_finished = True
                            if result == "DRAW":
                                print("Game ended in a draw")
                                con = True
                            else:
                                print(f"{result} wins!")
                                con = False
                        pygame.display.update()

                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    escape = False

    
    # function for 3x3 battles
    def threebythree(self):
        self.board = [[1,2,3], [4,5,6], [7,8,9]]
        self.graphical_board = [[[None, None], [None, None], [None, None]],
                        [[None, None], [None, None], [None, None]],
                        [[None, None], [None, None], [None, None]]]
        
        self.to_move = 'X'

        self.SCREEN.fill(self.BG_COLOR)
        #self.SCREEN.blit(self.BOARD, (-66,-26))

        square_size = 772 // 3  # Each square is about 257 pixels
        x_offset = 100  # Move the grid 100 pixels to the right (adjust as needed)
        for i in range(1, 3):
            # Horizontal lines
            pygame.draw.line(self.SCREEN, (0, 0, 50), (x_offset, i * square_size), (772 + x_offset, i * square_size), 15)
            # Vertical lines
            pygame.draw.line(self.SCREEN, (0, 0, 50), (i * square_size + x_offset, 0), (i * square_size + x_offset, 772), 15)

        

        pygame.display.update()
        # Still want player to be capable of closing the screen while in combat
        game_finished = False
        con = True
        escape = True
        while escape:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and con:
                    self.board, self.to_move = self.add_XO(self.board, self.graphical_board, self.to_move)

                    if game_finished:
                        self.board = [[1,2,3], [4,5,6], [7,8,9]]
                        self.graphical_board = [[[None, None], [None, None], [None, None]],
                                        [[None, None], [None, None], [None, None]],
                                        [[None, None], [None, None], [None, None]]]
        
                        self.to_move = 'X'
                        game_finished = False
    
                        self.SCREEN.fill(self.BG_COLOR)
                        self.SCREEN.blit(self.BOARD, (-66,-26))

                        pygame.display.update()

                    result = self.check_win(self.board)
                    if result is not None:
                        game_finished = True
                        if result == "DRAW":
                            # Handle draw case
                            print("Game ended in a draw")
                            con = True  # Stop taking moves
                        else:
                            # Handle win case
                            print(f"{result} wins!")
                            con = False  # Stop taking moves
                        pygame.display.update()
                        continue

                    #pygame.display.update()
                    # AI's turn (if the game is not finish)
                    if not game_finished and self.to_move == 'O':
                        self.board, self.to_move = self.rand_ai_move(self.board, self.graphical_board, self.to_move)

                        result = self.check_win(self.board)
                        if result is not None:
                            game_finished = True
                            if result == "Draw":
                                print("Game ended in a draw")
                                con = True
                            else:
                                print(f"{result} wins!")
                                con = False
                        pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    escape = False


    def render_board(self, board, ximg, oimg):
        square_size = 772 // 3  # Each square is about 257 pixels
        x_offset = 100  # Move the grid 100 pixels to the right (adjust as needed)

        for i in range(3):
            for j in range(3):
                # Calculate the center of the current square (i, j)
                center_x = j * square_size + square_size // 2 + x_offset
                center_y = i * square_size + square_size // 2

                if board[i][j] == 'X':
                    self.graphical_board[i][j][0] = ximg
                    # Center the X image using get_rect with the calculated center
                    self.graphical_board[i][j][1] = ximg.get_rect(center=(center_x, center_y))
                elif board[i][j] == 'O':
                    self.graphical_board[i][j][0] = oimg
                    # Center the O image using get_rect with the calculated center
                    self.graphical_board[i][j][1] = oimg.get_rect(center=(center_x, center_y))

        # Draw the grid lines with the same offset
        for i in range(1, 3):
            # Horizontal lines
            pygame.draw.line(self.SCREEN, (0, 0, 50), (x_offset, i * square_size), (772 + x_offset, i * square_size), 15)
            # Vertical lines
            pygame.draw.line(self.SCREEN, (0, 0, 50), (i * square_size + x_offset, 0), (i * square_size + x_offset, 772), 15)





    # Adds X or O to board
    def add_XO(self, board, graphical_board, to_move):
        current_pos = pygame.mouse.get_pos()
        
        # Subtract the x_offset (100) before calculating the converted_x position
        converted_x = (current_pos[0] - 100) // (772 // 3)  # Assume board starts at x=100 and size 772px
        converted_y = current_pos[1] // (772 // 3)  # No x_offset for y; y starts from 0

        # Ensure converted_x and converted_y are valid indices
        if 0 <= converted_x < 3 and 0 <= converted_y < 3:
            # Check if the cell is empty (i.e., not 'X' or 'O')
            if board[int(converted_y)][int(converted_x)] not in ['X', 'O']:
                # Place the current move (either 'X' or 'O')
                board[int(converted_y)][int(converted_x)] = to_move
                # Switch turns
                to_move = 'O' if to_move == 'X' else 'X'

        # Render the board after making the move
        self.render_board(board, self.X_IMG, self.O_IMG)

        # Display updated images for X and O
        for i in range(3):
            for j in range(3):
                if graphical_board[i][j][0] is not None:
                    self.SCREEN.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])
                    
        return board, to_move


    # work on reducing redundancy from loading images
    def check_win(self, board):
        winner = None
        for row in range(0,3):
            if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
                winner = board[row][0]
                for i in range(0,3):
                    # add assets to git
                    self.graphical_board[row][i][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
                    self.SCREEN.blit(self.graphical_board[row][i][0], self.graphical_board[row][i][1])
                pygame.display.update()
                return winner
            
        for col in range(0,3):
            if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
                winner = board[0][col]
                print(self.graphical_board[0][col])
                for i in range(0, 3):
                    self.graphical_board[i][col][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
                    self.SCREEN.blit(self.graphical_board[i][col][0], self.graphical_board[i][col][1])
                pygame.display.update()
                return winner
                
        if (board[0][0] == board[1][1] == board[2][2] and (board[0][0]) is not None):
            winner = board[0][0]
            self.graphical_board[0][0][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[0][0][0], self.graphical_board[0][0][1])
            self.graphical_board[1][1][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[1][1][0], self.graphical_board[1][1][1])
            self.graphical_board[2][2][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[2][2][0], self.graphical_board[2][2][1])
            pygame.display.update()
            return winner
            
        if(board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            winner = board[0][2]
            self.graphical_board[0][2][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[0][2][0], self.graphical_board[0][2][1])
            self.graphical_board[1][1][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[1][1][0], self.graphical_board[1][1][1])
            self.graphical_board[2][0][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[2][0][0], self.graphical_board[2][0][1])
            pygame.display.update()
            return winner
            
        if winner is None:
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        return None
            return "DRAW"
        
        return None
    
    # rand_ai_move chooses rand spot on board, will only use for first boss
    def rand_ai_move(self, board, graphical_board, to_move):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ['X', 'O']]

        if empty_cells:
            move = random.choice(empty_cells)
            board[move[0]][move[1]] = 'O'
            to_move = 'X'

        self.render_board(board, self.X_IMG, self.O_IMG)

        for i in range(3):
            for j in range(3):
                if graphical_board[i][j][0] is not None:
                    self.SCREEN.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])

        return board, to_move
    
    def render_fivebyfive(self, board, ximg, oimg):
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'X':
                    self.graphical_board[i][j][0] = ximg
                    self.graphical_board[i][j][1] = ximg.get_rect(center=(j*150+150, i*150+150))
                elif board[i][j] == 'O':
                    self.graphical_board[i][j][0] = oimg
                    self.graphical_board[i][j][1] = oimg.get_rect(center=(j*150+150, i*150+150))

    def add_XO_fivebyfive(self, board, graphical_board, to_move):
        current_pos = pygame.mouse.get_pos()
        converted_x = (current_pos[0] - 64) // (835 // 5)  # Adjust for 5x5 board size
        converted_y = (current_pos[1] - 64) // (835 // 5)

        if 0 <= converted_x < 5 and 0 <= converted_y < 5:
            if board[int(converted_y)][int(converted_x)] not in ['X', 'O']:
                board[int(converted_y)][int(converted_x)] = to_move
                to_move = 'O' if to_move == 'X' else 'X'

        self.render_board(board, self.X_IMG, self.O_IMG)

        for i in range(5):
            for j in range(5):
                if graphical_board[i][j][0] is not None:
                    self.SCREEN.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])

        return board, to_move

    # AI using Minimax algorithm
    def ai_move_fivebyfive(self, board, graphical_board, to_move):
        best_score = float('-inf')
        best_move = None

        for i in range(5):
            for j in range(5):
                if board[i][j] not in ['X', 'O']:
                    board[i][j] = 'O'
                    score = self.minimax(board, 0, False)
                    board[i][j] = i * 5 + j + 1  # Reset to original value
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            board[best_move[0]][best_move[1]] = 'O'
            to_move = 'X'

        self.render_board(board, self.X_IMG, self.O_IMG)

        for i in range(5):
            for j in range(5):
                if graphical_board[i][j][0] is not None:
                    self.SCREEN.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])

        return board, to_move

    # Minimax algorithm to improve AI decision-making
    def minimax(self, board, depth, is_maximizing):
        result = self.check_win(board)
        if result == 'O':
            return 1
        elif result == 'X':
            return -1
        elif result == 'DRAW':
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(5):
                for j in range(5):
                    if board[i][j] not in ['X', 'O']:
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = i * 5 + j + 1
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(5):
                for j in range(5):
                    if board[i][j] not in ['X', 'O']:
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = i * 5 + j + 1
                        best_score = min(score, best_score)
            return best_score

    def check_win_fivebyfive(self, board):
        # Check rows, columns, and diagonals for five in a row
        for row in range(5):
            if all(board[row][col] == board[row][0] for col in range(5)):
                return board[row][0]

        for col in range(5):
            if all(board[row][col] == board[0][col] for row in range(5)):
                return board[0][col]

        if all(board[i][i] == board[0][0] for i in range(5)):
            return board[0][0]

        if all(board[i][4-i] == board[0][4] for i in range(5)):
            return board[0][4]

        # Check for draw
        if all(board[i][j] in ['X', 'O'] for i in range(5) for j in range(5)):
            return "DRAW"

        return None