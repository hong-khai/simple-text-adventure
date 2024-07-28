print("""Welcome to a simple text adventure game! Where would you like to go?
a) The library
b) The mysterious room you found under your house
c) To your friend's house""")

player_choice = input()

if player_choice == "a":
  print("""You found a few books. Which one would you like to read?
a) A programming book
b) A history book
c) Joke book""")
  if choice == "a":
    print("You learnt some new Python skills!")
  elif choice == "b":
    print("You learn about some historic events!")
  elif choice == "c":
    print("You laugh so hard you dropped your book multiple times!")
  else:
    print("Not an option.")
elif player_choice == "b":
  print("The room is larger that you saw last time. However, there isn't anything intresting. :(")
elif player_choice == "c":
  print("You play some tag in a nearby park with your friends. You had a lot of fun!")
else:
  print("Not an option.")
