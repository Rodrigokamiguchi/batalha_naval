# Batalha Naval (Battleship Game)

## Desenvolvimento do Jogo

### Definição do Tema
Um jogo de Batalha Naval desenvolvido em Python, onde o jogador tenta afundar navios adversários em um tabuleiro de 10x10, utilizando coordenadas para disparar.

### Planejamento do Desenvolvimento

#### Cronograma de Desenvolvimento
| Período | Etapa | Descrição | Status |
|---------|-------|-----------|--------|
| 11/11/2024 | Concepção Inicial | Definição do conceito do jogo de Batalha Naval | Concluído |
| 12/11/2024 | Desenvolvimento da Interface Básica | Criação do tabuleiro e mecânicas iniciais | Concluído |
| 13/11/2024 | Implementação de Funcionalidades | 
- Sistema de pontuação
- Mecânicas de jogo
- Tratamento de entrada do jogador | Concluído |
| 14/11/2024 | Adição de Recursos Avançados | 
- Efeitos sonoros
- Animações de acerto e erro
- Refinamento da interface | Concluído |
| 15/11/2024 | Testes Finais e Documentação | 
- Teste completo do jogo
- Documentação final
- Preparação para entrega | Concluído |

#### Contexto de Desenvolvimento
O desenvolvimento deste projeto apresentou características únicas:
- **Abordagem Livre:** O projeto foi construído sem um planejamento inicial rígido
- **Desenvolvimento Orgânico:** As funcionalidades foram adicionadas de forma incremental
- **Desafios:** 
  * Adaptação constante durante o desenvolvimento
  * Implementação de recursos sem um escopo previamente definido
  * Aprendizado na construção do jogo

### Metodologia de Desenvolvimento
- **Abordagem Experimental:** Desenvolvimento iterativo sem um plano detalhado prévio
- **Aprendizado Contínuo:** Cada etapa representou uma oportunidade de descoberta e implementação
- **Flexibilidade:** Capacidade de adaptar e modificar o projeto conforme necessário

### Desenvolvimento
O jogo foi desenvolvido seguindo uma abordagem modular, com classes separadas para:
- `Ship`: Representação dos navios
- `Board`: Gerenciamento do tabuleiro de jogo
- `Scoreboard`: Controle de pontuação e erros
- `Game`: Lógica principal do jogo

### Testes
- Verificação de posicionamento correto dos navios
- Validação das entradas do jogador
- Teste de mecânicas de pontuação
- Verificação de condições de fim de jogo

## Tecnologias Utilizadas

### Linguagens
- **Linguagem Principal:** Python 3

### Bibliotecas e Ferramentas
- **Pygame:** Biblioteca para desenvolvimento de interface gráfica e jogos

## Complexidade do Jogo

### Análise de Algoritmos
- **Geração de Tabuleiro:** 
  * Algoritmo de posicionamento aleatório de navios
  * Complexidade: O(n), com verificações de sobreposição
- **Processamento de Entrada:** 
  * Conversão de coordenadas alfanuméricas
  * Verificação de acerto/erro
  * Complexidade: O(1)

### Gestão da Complexidade
- Uso de classes para modularização
- Métodos específicos para cada funcionalidade
- Tratamento de exceções para entradas inválidas
- Algoritmo de geração de navios com limite de tentativas

## Regras do Jogo (Jogabilidade)

### Objetivo
Afundar todos os navios do tabuleiro com o mínimo de tentativas possível.

### Instruções para Jogadores
1. **Tabuleiro:** Grade 10x10 com coordenadas de A1 a J10
2. **Entrada de Jogada:** 
   - Digite a coordenada desejada (ex: A3)
   - Pressione Enter para confirmar
3. **Feedback:**
   - Acerto: Quadrado fica vermelho, som de explosão
   - Erro: Contagem de erros aumenta, som de erro
4. **Pontuação:**
   - Cada navio afundado: +1 ponto
   - Número de erros registrados
5. **Fim de Jogo:** 
   - Afundar todos os navios
   - Opção de reiniciar após vitória

### Navios no Jogo
- 4 navios de 1 célula
- 1 navio de 2 células

### Limitações
- Máximo de tentativas não definido
- Interface simples, foco na jogabilidade

## Recursos Adicionais
- Efeitos sonoros para acertos e erros
- Animação de explosão ao acertar um navio
- Placar com pontuação e contagem de erros

## Requisitos para Execução
- Python
- Biblioteca Pygame
- Conteúdo do jogo _clonado_ do GitHub

## Como Executar
1. Instale o Python 3
2. Instale Pygame: `pip install pygame`
3. Clone o repositório
4. Execute: `python main.py`

## Referências
De Souza, D. W. (n.d.). Batalha-Naval-Python: Jogo Batalha Naval Feito em Linguagem Python.

PYGAME. Pygame Documentation. 2023. Disponível em: https://www.pygame.org/docs/. Acesso em: 08 nov. 2024.

MATTHES, Eric. Python Crash Course: A Hands-On, Project-Based Introduction to Programming. 2. ed. San Francisco: No Starch Press, 2019.

REAL PYTHON. Create a Battleship Game in Python. Disponível em: https://realpython.com/python-battleship-game/. Acesso em: 08 nov. 2024.

SWEIGART, Al. Invent Your Own Computer Games with Python. 4. ed. San Francisco: No Starch Press, 2016.

UDEMY. Introdução ao Desenvolvimento de Jogos com Pygame. Disponível em: https://www.udemy.com/. Acesso em: 08 nov. 2024.

GEEKSFORGEEKS. Battleship Game Algorithms. Disponível em: https://www.geeksforgeeks.org/battleship-game-algorithms/. Acesso em: 08 nov. 2024.

MCSHAFFRY, Mike; GRAHAM, David. Game Coding Complete. 4. ed. Plano, TX: Paraglyph Press, 2012.

DEV.TO. Game Development with Python. Disponível em: https://dev.to/. Acesso em: 08 nov. 2024.

OPENGAMEART. OpenGameArt.org. Disponível em: https://opengameart.org/. Acesso em: 08 nov. 2024.

FREESOUND. FreeSound.org. Disponível em: https://freesound.org/. Acesso em: 08 nov. 2024.

##PARTICIPANTES
- Rodrigo Guilherme ( https://github.com/Rodrigokamiguchi )
- Leonardo Teodoro ( https://github.com/imponateao )
- Elias Rozal De Carvalho ( https://github.com/Elias-RDC )
- Mateus Rian ( https://github.com/MateuSpatano )
- Maurício ( https://github.com/VinteFaces )
