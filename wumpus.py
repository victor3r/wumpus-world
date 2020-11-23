import random
import sys

def game_over():
  print('Quer jogar novamente S ou N?')
  choice_input = input('> ')
  if choice_input == 'n' or choice_input == 'N':
     sys.exit('Fim de jogo!!!')

def clear_wumpus():
  for i in range(len(rooms)):
    if rooms[i][4] == 1:
      rooms[i - 1][0] = 0
      rooms[i + 1][0] = 0

max_size = 20
rooms = [[0, 0, 0, 0, 0] for i in range(max_size + 1)]
player_location = 0
arrows_number = 1
gold_location = random.randint(1, max_size - 1)
wumpus_location = random.randint(1, max_size - 1)
while wumpus_location == player_location or wumpus_location == gold_location or gold_location == player_location:
  wumpus_location = random.randint(1, max_size - 1)
  gold_location = random.randint(1, max_size - 1)
rooms[gold_location][2] = 1 
rooms[wumpus_location][4] = 1
rooms[wumpus_location - 1][0] = 1
rooms[wumpus_location + 1][0] = 1
for i in range(1, len(rooms) - 1):
  if i != wumpus_location and i != gold_location and random.random() < 0.2:
    rooms[i][3] = 1
    rooms[i - 1][1] = 1
    rooms[i + 1][1] = 1
print('Bem-vindo ao Mundo do Wumpus!')
print('Você pode ver', len(rooms) - 1, 'salas')
print('Para jogar, apenas digite o número da sala que você quer visitar')
while True:
  print('Você está na sala', player_location + 1)
  if rooms[player_location][0] == 1:
    print('Eu sinto o cheiro do Wumpus!!!!')
    print('Você tem', arrows_number, 'flecha(s)')
    if arrows_number > 0:
      print('Quer tentar acertá-lo S ou N?')
      choice_input = input('> ')
      if choice_input == 's' or choice_input == 'S':
        print('Em qual sala você quer mirar?')
        target_input = input('> ')
        if rooms[int(target_input)][4] == 1 and random.random() < 0.6:
          clear_wumpus()
          print('Você matou o Wumpus!!!!')
          game_over()
        else:
          print('Você errou!')
          arrows_number-=1
          print('Seu número de flechas agora é', arrows_number)
  if rooms[player_location][1] == 1:
    print('Eu sinto uma brisa...')
  print('Qual a próxima sala?')
  room_input = input('> ')
  if not room_input.isdigit() or int(room_input) - 1 < 0 or int(room_input) - 1 > 19:
    print(room_input, 'não é uma sala')
  else:
    player_location = int(room_input) - 1
    if rooms[player_location][4] == 1:
      print('Aargh!!! Você foi pego pelo Wumpus!')
      game_over()
    elif rooms[player_location][2] == 1:
      rooms[player_location][2] = 0
      print('Parabéns!!!! Você encontrou o ouro!')
      game_over()
    elif rooms[player_location][3] == 1:
      print('Você caiu no poço!')
      game_over()