# Author: Amir Aslamov
# Description of Program: This program is designed to stimulate a game of Higher Or Lower,
#                        in which a user is randomly presented with a couple of celebrities, cars, movies, 
#                        or social media platforms and asked to choose which one of the choices has more 
#                        subscribers.
# Date of Creation: /started: 08/28/2021, 5:04 PM/ /finished:    





import random
import art
import game_data






# this function will print the two items to compare
def print_items(item1, item2):
  
  print(f"\n\nCompare A: {item1['name']}, {item1['description']}, from {item1['country']}.")
  print(art.vs)
  print(f"Against B: {item2['name']}, {item2['description']}, from {item2['country']}.")






# this function will compare the number of followers of the two items and accordingly return either 
# True or False, which will eventually define the progression of the program
def compare_items(item1, item2, score):

  user_decision = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # print(f"\n\nA: {item1['follower_count']} VS. B: {item2['follower_count']}")
  if user_decision == 'a':
    if (item1['follower_count'] > item2['follower_count']):
      score += 1
      print(f"You are right! 😁 Your score: {score}.")
    else:
      print("You are wrong! Game over! 😔")
      score = -1   
  elif user_decision == 'b':
    if (item2['follower_count'] > item1['follower_count']):
      score += 1
      print(f"You are right! 😁 Your score: {score}.") 
    else:
      print("You are wrong! Game over! 😔")
      score = -1
  
  return score






# this function will be the main game to recursavily call itslef when needed
def game():

  # printing the logo artwork from the art file in the same directory
  print(art.logo)
  # this variable will keep track of the user's scores along the game
  total_score = 0
  # creating the random index to choose the first item
  rand_index = random.randint(0, len(game_data.data) - 1)
  item1 = game_data.data[rand_index]

  # creating the random index to choose the second item
  # this index must be different from the first open
  rand_index2 = random.randint(0, len(game_data.data) - 1)
  while (rand_index2 == rand_index):
    rand_index2 = random.randint(0, len(game_data.data) - 1)
  item2 = game_data.data[rand_index2]

  print_items(item1, item2)

  # print(f"A: {item1['follower_count']} VS. B: {item2['follower_count']}")
  total_score = compare_items(item1, item2, total_score)

  while (total_score != -1):

    rand_index2 = random.randint(0, len(game_data.data) - 1)
    item1 = item2
    item2 = game_data.data[rand_index2]

    print_items(item1, item2)
    # print(f"A: {item1['follower_count']} VS. B: {item2['follower_count']}")
    total_score = compare_items(item1, item2, total_score)
    


# main 
# start of the program, invoking the game function for the first time 
game()
     
  
