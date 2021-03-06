# -*- coding: utf-8 -*-
"""s18579_gr12c_PRO1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fK0clguTWXU6rZ3HRgJkeR1wS5amczCZ

#Projekt 1
##1. Napisz program, uczący się gry “papier, kamień, nożyce”. Jako algorytm uczący zastosuj łańcuch Markowa z macierzą przejść pomiędzy trzema stanami (Papier, Kamień, Nożyce). Nauka gry polega na korekcie macierzy przejść (prawdopodobieństwa warunkowe zmiany stanu),
##2. Wartość wypłaty: 1 w przypadku wygranej, −1 w przypadku przegranej i 0 w przypadku remisu,
##3. Przeprowadź ciąg kilkudziesięciu gier “kamień, papier, nożyce”. Sporząź wykres jak zmienia się stan kasy w każdym kroku gry.
"""

import numpy as rand
import matplotlib.pyplot as graph

def increaseLearningRateForRock(array2D, rate, index):
  array2D[index][0] += rate    #Kamien
  array2D[index][1] -= rate/2  #Papier
  array2D[index][2] -= rate/2  #Nozyce

def increaseLearningRateForPaper(array2D, rate, index):
  array2D[index][0] -= rate/2   #Kamien
  array2D[index][1] += rate     #Papier
  array2D[index][2] -= rate/2   #Nozyce

def increaseLearningRateForScissors(array2D, rate, index):
  array2D[index][0] -= rate/2   #Kamien
  array2D[index][1] -= rate/2   #Papier
  array2D[index][2] += rate     #Nozyce

rps = [
    #Kamien Papier Nozyce   
    [ 'r',  'p',    's'   ],# Skrot
    [ 0.33,  0.33,  0.34  ] # Prawdopodobieństwo
]

matrix = [
   #Kamien Papier Nozyce                 
    [0.33, 0.33,  0.34], # Kamien
    [0.33, 0.33,  0.34], # Papier
    [0.33, 0.33,  0.34]  # Nozyce
]

state= [ 'Win! : )\n', 'Draw : |\n', 'Lose : (\n']

player_points_per_iteration = []
learning_rate = 0.01
points = 0
count = 30

user_decision = input('Select a game mode (auto, manual): ')
past_action = rand.random.choice(rps[0], p=rps[1])
for i in range(0, count):
 if user_decision == 'auto': user_action = rand.random.choice(rps[0], p=rps[1])
 elif user_decision == 'manual': user_action = input("Choose between rock paper and scissors (r, p, s): ")
 else:
   print('Error: Wrong string')
   break

 if past_action == 'r': computer_action = rand.random.choice(rps[0], p=matrix[0])
 elif past_action == 'p': computer_action = rand.random.choice(rps[0], p=matrix[1])
 else: computer_action = rand.random.choice(rps[0], p=matrix[2])

 print("User: "+str(user_action))
 print("Computer: "+str(computer_action))

 if computer_action == 'r': # Komputer: Kamień 
   if user_action == 'r':   # Uzytkownik: Kamień 
     if matrix[0][0] - learning_rate/2 >= 0 and matrix[0][2] - learning_rate/2 >= 0: increaseLearningRateForPaper(matrix, learning_rate, 0)
     print(state[1])

   elif user_action == 'p': # Uzytkownik: Papier 
     points +=1
     if matrix[0][0] - learning_rate/2 >= 0 and matrix[0][1] - learning_rate/2 >= 0: increaseLearningRateForScissors(matrix, learning_rate, 0)
     print(state[0])

   else:                    # Uzytkownik: Nozyce 
     points -=1
     print(state[2])


 elif computer_action == 'p':         # Komputer: Papier 
   if user_action == 'r':   # Uzytkownik: Kamień 
     points -=1
     print(state[2])

   elif user_action == 'p':   # Uzytkownik: Papier 
     if matrix[1][0] - learning_rate/2 >= 0 and matrix[1][1] - learning_rate/2 >= 0: increaseLearningRateForScissors(matrix, learning_rate, 1)
     print(state[1])

   else:                      # Uzytkownik: Nozyce 
    points +=1
    if matrix[1][1] - learning_rate/2 >= 0 and matrix[1][2] - learning_rate/2 >= 0:increaseLearningRateForRock(matrix, learning_rate, 1)
    print(state[0])


 else:                        # Komputer: Nozyce 
  if user_action == 'r':      # Uzytkownik: Kamień 
    points +=1
    if matrix[2][0] - learning_rate/2 >= 0 and matrix[2][2] - learning_rate/2 >= 0: increaseLearningRateForPaper(matrix, learning_rate, 2)
    print(state[0])

  elif user_action == 'p':    # Uzytkownik: Papier 
    points -=1
    print(state[2])

  else:                       # Uzytkownik: Nozyce 
    if matrix[2][1] - learning_rate/2 >= 0 and matrix[2][2] - learning_rate/2 >= 0: increaseLearningRateForRock(matrix, learning_rate, 2)
    print(state[1])

 past_action = user_action
 player_points_per_iteration.append(points)


print('Number of games: '+str(count))
print('User points: '+str(points)+"     Computer points: "+str(points*-1))
print('Matrix: '+str(matrix))
graph.plot(player_points_per_iteration, 'rd')
graph.ylabel('Player Points')
graph.xlabel('Games played')
graph.show()