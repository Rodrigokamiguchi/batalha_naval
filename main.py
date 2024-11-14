import pygame
import random

# Inicialização do Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
GRID_OFFSET = 50  # Espaço adicional para mostrar letras e números fora do tabuleiro
screen = pygame.display.set_mode((WIDTH + GRID_OFFSET, HEIGHT + GRID_OFFSET))
pygame.display.set_caption("Batalha Naval")
icon = pygame.image.load("imagen/icon.png")
pygame.display.set_icon(icon)

# Cores
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
COLOR_TEXT = (0, 0, 0)  # Cor para letras e números

class Ship:
    """Classe que representa um navio.""" 
    def __init__(self, position):
        self.position = position

class Board:
    """Classe que representa o tabuleiro do jogo.""" 
    def __init__(self):
        self.grid_size = 10
        self.cell_size = WIDTH // self.grid_size
        self.ships = []
        self.hit_ships = []  # Armazena as posições dos navios acertados
        self.place_ships()

    def draw(self):
        """Desenha o tabuleiro e os navios.""" 
        font = pygame.font.Font(None, 36)

        # Desenha letras ao lado do tabuleiro (lado esquerdo)
        for y in range(self.grid_size):
            letter_text = font.render(chr(65 + y), True, COLOR_TEXT)  # 'A' é 65 em ASCII
            screen.blit(letter_text, (5, y * self.cell_size + self.cell_size // 2 - letter_text.get_height() // 2))

        # Desenha o tabuleiro
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, BLACK, rect, 1)  # Desenha a grade

                if (x, y) in self.hit_ships:  # Se a posição está na lista de acertos
                    pygame.draw.rect(screen, RED, rect)  # Marca como atingido

        # Desenha números abaixo do tabuleiro
        for x in range(self.grid_size):
            number_text = font.render(str(x + 1), True, COLOR_TEXT)
            screen.blit(number_text, (x * self.cell_size + self.cell_size // 2 - number_text.get_width() // 2, HEIGHT - GRID_OFFSET + 10))

    def can_place_ship(self, col, row, length, orientation):
        """Verifica se um navio pode ser colocado na posição especificada.""" 
        if orientation == 'horizontal':
            if col + length > self.grid_size:
                return False
            for i in range(length):
                if (col + i, row) in [(s.position) for s in self.ships]:
                    return False
        else:  # vertical
            if row + length > self.grid_size:
                return False
            for i in range(length):
                if (col, row + i) in [(s.position) for s in self.ships]:
                    return False
        return True

    def place_ships(self):
        """Coloca os navios no tabuleiro.""" 
        ship_lengths = [1, 1, 1, 1, 2]  # Comprimentos dos navios: 4 navios de tamanho 1 e 1 navio de tamanho 2
        for length in ship_lengths:
            placed = False
            attempts = 0  # Tenta várias vezes colocar um navio
            while not placed and attempts < 100:  # Limitar tentativas para evitar loop infinito
                orientation = random.choice(['horizontal', 'vertical'])
                col = random.randint(0, self.grid_size - 1)
                row = random.randint(0, self.grid_size - 1)

                if self.can_place_ship(col, row, length, orientation):
                    if orientation == 'horizontal':
                        for i in range(length):
                            self.ships.append(Ship((col + i, row)))
                    else:  # vertical
                        for i in range(length):
                            self.ships.append(Ship((col, row + i)))
                    placed = True
                attempts += 1

class Scoreboard:
    """Classe que representa o placar e o temporizador do jogo.""" 
    def __init__(self):
        self.score = 0
        self.errors = 0  # Contador de erros
        self.font = pygame.font.Font(None, 36)

    def update_score(self, increment):
        """Atualiza a pontuação do jogador.""" 
        self.score += increment

    def update_errors(self):
        """Incrementa o contador de erros.""" 
        self.errors += 1

    def draw(self, surface):
        """Desenha a pontuação e o tempo no surface fornecido.""" 
        score_text = self.font.render(f"Pontos: {self.score}", True, COLOR_TEXT)
        error_text = self.font.render(f"Erros: {self.errors}", True, COLOR_TEXT)

        surface.blit(score_text, (WIDTH + GRID_OFFSET - 200, 60))
        surface.blit(error_text, (WIDTH + GRID_OFFSET - 200, 100))  # Exibe o contador de erros

class Game:
    """Classe que representa o jogo em si.""" 
    def __init__(self):
        self.board = Board()
        self.font = pygame.font.Font(None, 36)
        self.player_input = ""  # Armazena a resposta digitada pelo jogador
        self.game_over = False  # Variável para controlar o estado do jogo
        self.scoreboard = Scoreboard()  # Instância do placar

    def show_victory_message(self):
        """Mostra uma mensagem de vitória ao jogador.""" 
        victory_text = self.font.render("Você venceu!", True, GREEN)
        screen.blit(victory_text, (WIDTH // 2 - victory_text.get_width() // 2, HEIGHT // 2))

    def display_player_input(self):
        """Exibe a entrada do jogador na tela.""" 
        input_text = self.font.render(f"Entrada do Jogador: {self.player_input}", True, COLOR_TEXT)
        screen.blit(input_text, (WIDTH + GRID_OFFSET - 300, 150))  # Ajuste a posição conforme necessário

    def process_player_input(self):
        """Processa a entrada do jogador.""" 
        if self.player_input:
            try:
                # Converte a entrada para índices de grade
                column = ord(self.player_input[0].upper()) - ord('A')
                row = int(self.player_input[1]) - 1

                if 0 <= column < self.board.grid_size and 0 <= row < self.board.grid_size:
                    if (column, row) in [(s.position) for s in self.board.ships]:
                        self.board.hit_ships.append((column, row))  # Adiciona a posição do navio acertado
                        self.board.ships = [s for s in self.board.ships if s.position != (column, row)]
                        self.scoreboard.update_score(1)  # Adiciona um ponto por acerto
                        if len(self.board.ships) == 0:
                            self.game_over = True  # Finaliza o jogo
                    else:
                        self.scoreboard.update_errors()  # Atualiza o contador de erros
                else:
                    print("Entrada inválida.")
            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente com formato correto (ex: A1).")

        self.player_input = ""  # Reseta a entrada após o processamento

    def run(self):
        """Executa o loop principal do jogo.""" 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if self.game_over:
                        self.reset_game()  # Reinicia o jogo se estiver finalizado
                    elif event.key == pygame.K_RETURN:
                        self.process_player_input()  # Processa a entrada do jogador
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_input = self.player_input[:-1]  # Apaga o último caractere
                    else:
                        self.player_input += event.unicode.upper()  # Adiciona o caractere pressionado à entrada

            screen.fill(BLUE)  # Preenche a tela com a cor de fundo
            self.board.draw()  # Desenha o tabuleiro
            self.scoreboard.draw(screen)  # Desenha a pontuação e erros
            self.display_player_input()  # Exibe a entrada do jogador
            if self.game_over:
                self.show_victory_message()  # Exibe a mensagem de vitória
            pygame.display.flip()  # Atualiza a tela

    def reset_game(self):
        """Reseta o estado do jogo para a próxima partida.""" 
        self.board = Board()
        self.scoreboard = Scoreboard()
        self.game_over = False

# Instanciando o jogo e rodando
game = Game()
game.run()

pygame.quit()
