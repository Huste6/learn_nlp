import pygame
import sys
import numpy as np

# Kích thước bàn cờ
BOARD_SIZE = 15
CELL_SIZE = 40
WINDOW_SIZE = BOARD_SIZE * CELL_SIZE

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Giá trị ô cờ
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1

# Khởi tạo pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Caro AI - MiniMax")
screen.fill(WHITE)

# Bàn cờ
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# Vẽ bàn cờ
def draw_board():
    screen.fill(WHITE)
    for i in range(BOARD_SIZE):
        pygame.draw.line(screen, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE))
        pygame.draw.line(screen, GRAY, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE))
    
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == PLAYER_X:
                pygame.draw.line(screen, BLACK, (x * CELL_SIZE + 10, y * CELL_SIZE + 10),
                                 ((x + 1) * CELL_SIZE - 10, (y + 1) * CELL_SIZE - 10), 2)
                pygame.draw.line(screen, BLACK, ((x + 1) * CELL_SIZE - 10, y * CELL_SIZE + 10),
                                 (x * CELL_SIZE + 10, (y + 1) * CELL_SIZE - 10), 2)
            elif board[y][x] == PLAYER_O:
                pygame.draw.circle(screen, BLACK, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 5, 2)
    pygame.display.flip()

# Đánh giá bàn cờ
def evaluate():
    # Đây là hàm đơn giản, có thể mở rộng để đánh giá tốt hơn
    return np.random.randint(-10, 10)

# Thuật toán Minimax + Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):
    if depth == 0:
        return evaluate(), None

    best_move = None
    if is_maximizing:
        max_eval = -float('inf')
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if board[y][x] == EMPTY:
                    board[y][x] = PLAYER_X
                    eval, _ = minimax(depth - 1, False, alpha, beta)
                    board[y][x] = EMPTY
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (x, y)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if board[y][x] == EMPTY:
                    board[y][x] = PLAYER_O
                    eval, _ = minimax(depth - 1, True, alpha, beta)
                    board[y][x] = EMPTY
                    if eval < min_eval:
                        min_eval = eval
                        best_move = (x, y)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval, best_move

# Lượt đi của AI
def ai_move():
    _, best_move = minimax(2, True, -float('inf'), float('inf'))  # Độ sâu 2 để giảm tải
    if best_move:
        x, y = best_move
        board[y][x] = PLAYER_X

draw_board()

# Vòng lặp chính
turn = PLAYER_O  # Người chơi đi trước
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and turn == PLAYER_O:
            x, y = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
            if board[y][x] == EMPTY:
                board[y][x] = PLAYER_O
                turn = PLAYER_X
    
    if turn == PLAYER_X:
        ai_move()
        turn = PLAYER_O
    
    draw_board()

pygame.quit()
sys.exit()
