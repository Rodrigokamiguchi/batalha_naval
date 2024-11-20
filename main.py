import pygame
import random

# Inicialização do Pygame e mixer para sons
pygame.init()
pygame.mixer.init()

# Obtém o tamanho da tela do usuário
USER_SCREEN_INFO = pygame.display.Info()
SCREEN_WIDTH = USER_SCREEN_INFO.current_w
SCREEN_HEIGHT = USER_SCREEN_INFO.current_h

# Calcula o tamanho do tabuleiro baseado no menor lado da tela
GRID_SIZE = 10
GRID_OFFSET = 50  # Espaço adicional para mostrar letras e números fora do tabuleiro
BOARD_SIZE = min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.8  # Usa 80% do menor lado da tela
CELL_SIZE = int(BOARD_SIZE / GRID_SIZE)

# Ajusta o tamanho total da janela
WIDTH = int(BOARD_SIZE) + GRID_OFFSET
HEIGHT = int(BOARD_SIZE) + GRID_OFFSET

# Configura a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Batalha Naval")

# Tenta carregar o ícone, com fallback se não encontrar
try:
    icon = pygame.image.load("imagen/icon.png")
    pygame.display.set_icon(icon)
except:
    print("Ícone não encontrado. Usando ícone padrão.")

# Cores
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
COLOR_TEXT = (0, 0, 0)  # Cor para letras e números

# Sons (com tratamento de erro)
try:
    sound_hit = pygame.mixer.Sound("sons/background_music.mp3")
    sound_miss = pygame.mixer.Sound("sons/miss.mp3")
except:
    print("Erro ao carregar sons. Continuando sem efeitos sonoros.")
    # Cria sons nulos se os arquivos não forem encontrados
    sound_hit = pygame.mixer.Sound(buffer=bytearray())
    sound_miss = pygame.mixer.Sound(buffer=bytearray())

class Ship:
    """Classe que representa um navio.""" 
    def __init__(self, position):
        self.position = position

class Board:
    """Classe que representa o tabuleiro do jogo.""" 
    def __init__(self, cell_size):
        self.grid_size = 10
        self.cell_size = cell_size
        self.ships = []
        self.hit_ships = []  # Armazena as posições dos navios acertados
        self.place_ships()

    def draw(self, surface):
        """Desenha o tabuleiro e os navios.""" 
        font = pygame.font.Font(None, max(12, int(self.cell_size * 0.5)))

        # Desenha letras ao lado do tabuleiro (lado esquerdo)
        for y in range(self.grid_size):
            letter_text = font.render(chr(65 + y), True, COLOR_TEXT)
            surface.blit(letter_text, (5, y * self.cell_size + self.cell_size // 2 - letter_text.get_height() // 2))

        # Desenha o tabuleiro
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(surface, BLACK, rect, 1)

                if (x, y) in self.hit_ships:
                    pygame.draw.rect(surface, RED, rect)

        # Desenha números abaixo do tabuleiro
        for x in range(self.grid_size):
            number_text = font.render(str(x + 1), True, COLOR_TEXT)
            surface.blit(number_text, (x * self.cell_size + self.cell_size // 2 - number_text.get_width() // 2, HEIGHT - GRID_OFFSET + 10))

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
        ship_lengths = [1, 1, 1, 1, 2]
        for length in ship_lengths:
            placed = False
            attempts = 0
            while not placed and attempts < 100:
                orientation = random.choice(['horizontal', 'vertical'])
                col = random.randint(0, self.grid_size - 1)
                row = random.randint(0, self.grid_size - 1)

                if self.can_place_ship(col, row, length, orientation):
                    if orientation == 'horizontal':
                        for i in range(length):
                            self.ships.append(Ship((col + i, row)))
                    else:
                        for i in range(length):
                            self.ships.append(Ship((col, row + i)))
                    placed = True
                attempts += 1

class Scoreboard:
    """Classe que representa o placar e o temporizador do jogo.""" 
    def __init__(self, font_size):
        self.score = 0
        self.errors = 0
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)

    def update_score(self, increment):
        """Atualiza a pontuação do jogador.""" 
        self.score += increment

    def update_errors(self):
        """Incrementa o contador de erros.""" 
        self.errors += 1

    def draw(self, surface, width):
        """Desenha a pontuação e o tempo no surface fornecido.""" 
        score_text = self.font.render(f"Pontos: {self.score}", True, COLOR_TEXT)
        error_text = self.font.render(f"Erros: {self.errors}", True, COLOR_TEXT)

        # Posiciona os textos à direita
        surface.blit(score_text, (width + GRID_OFFSET - 200, 60))
        surface.blit(error_text, (width + GRID_OFFSET - 200, 100))

class Game:
    """Classe que representa o jogo em si.""" 
    def __init__(self, screen_width, screen_height):
        # Calcula tamanhos dinâmicos
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = 10
        self.cell_size = int(min(screen_width, screen_height) * 0.8 / self.grid_size)
        
        # Inicializa componentes do jogo com tamanhos dinâmicos
        self.board = Board(self.cell_size)
        font_size = max(12, int(self.cell_size * 0.5))
        self.font = pygame.font.Font(None, font_size)
        self.player_input = ""
        self.game_over = False
        self.scoreboard = Scoreboard(font_size)

    def show_victory_message(self, surface):
        """Mostra uma mensagem de vitória ao jogador.""" 
        victory_text = self.font.render("Você venceu!", True, GREEN)
        surface.blit(victory_text, (self.screen_width // 2 - victory_text.get_width() // 2, self.screen_height // 2))

    def display_player_input(self, surface):
        """Exibe a entrada do jogador na tela.""" 
        input_text = self.font.render(f"Entrada do Jogador: {self.player_input}", True, COLOR_TEXT)
        surface.blit(input_text, (self.screen_width - 300, 150))

    def process_player_input(self):
        """Processa a entrada do jogador com sons e animação.""" 
        if self.player_input:
            try:
                column = ord(self.player_input[0].upper()) - ord('A')
                row = int(self.player_input[1]) - 1

                if 0 <= column < self.board.grid_size and 0 <= row < self.board.grid_size:
                    if (column, row) in [(s.position) for s in self.board.ships]:
                        self.board.hit_ships.append((column, row))
                        self.board.ships = [s for s in self.board.ships if s.position != (column, row)]
                        self.scoreboard.update_score(1)
                        sound_hit.play()

                        self.show_explosion((column, row))

                        if len(self.board.ships) == 0:
                            self.game_over = True
                    else:
                        self.scoreboard.update_errors()
                        sound_miss.play()
                else:
                    print("Entrada inválida.")
            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente com formato correto (ex: A1).")

        self.player_input = ""

    def show_explosion(self, position):
        """Exibe uma animação de explosão na posição fornecida.""" 
        try:
            explosion_img = pygame.image.load("imagen/explosao.jpg")
            rect = pygame.Rect(position[0] * self.cell_size, position[1] * self.cell_size, self.cell_size, self.cell_size)
            for i in range(10):
                screen.blit(explosion_img, rect)
                pygame.display.flip()
                pygame.time.delay(50)
        except:
            print("Imagem de explosão não encontrada.")

    def run(self):
        """Executa o loop principal do jogo.""" 
        global screen  # Usa a variável global screen
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Lida com redimensionamento da janela
                if event.type == pygame.VIDEORESIZE:
                    # Recalcula tamanhos baseados no novo tamanho da janela
                    self.screen_width, self.screen_height = event.size
                    # Atualiza o tamanho da janela
                    screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
                    
                    # Recalcula tamanhos dos componentes
                    self.cell_size = int(min(self.screen_width, self.screen_height) * 0.8 / self.grid_size)
                    self.board = Board(self.cell_size)
                    font_size = max(12, int(self.cell_size * 0.5))
                    self.font = pygame.font.Font(None, font_size)
                    self.scoreboard = Scoreboard(font_size)

                if event.type == pygame.KEYDOWN:
                    if self.game_over:
                        self.reset_game()
                    elif event.key == pygame.K_RETURN:
                        self.process_player_input()
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_input = self.player_input[:-1]
                    else:
                        self.player_input += event.unicode.upper()

            screen.fill(BLUE)
            self.board.draw(screen)
            self.scoreboard.draw(screen, self.screen_width)
            self.display_player_input(screen)
            if self.game_over:
                self.show_victory_message(screen)
            pygame.display.flip()

    def reset_game(self):
        """Reseta o estado do jogo para a próxima partida.""" 
        self.board = Board(self.cell_size)
        self.scoreboard = Scoreboard(max(12, int(self.cell_size * 0.5)))
        self.game_over = False

# Instanciando o jogo e rodando
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
game.run()

pygame.quit()
