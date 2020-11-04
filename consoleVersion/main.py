from os import listdir
from world import World
from command import Command
from helptext import helpText

def main():
    print("Welcome to T-BAG, your friendly neighborhood Text-Based Adventure Game!")
    w = loadGameWorld()
    currentInput = ""

    commands = {
      "go": Command(w.go,True),
      "look": Command(w.look,False),
      "whereami": Command(w.whereami,False),
      "carrying": Command(w.carrying,False),
      "lookaround": Command(w.lookaround,False),
      "examine": Command(w.examine,True),
      "take": Command(w.take,True),
      "drop": Command(w.drop,True),
      "save": Command(w.save, False)
      # "use": Command(w.use,True)
    }
    # MAIN GAME INPUT LOOP
    while(currentInput != 'exit'):
      currentInput = input("- ")
      # format input
      if ' ' in currentInput:
        command,params = currentInput.split(None, 1)
      else:
        command = currentInput
        params = ""
      # check for special command
      if command == 'help':
        print(helpText)
      elif command == "exit":
        shouldSaveGame = input("Would you like to save before you leave? y or n: ")
        if(shouldSaveGame == "y" or shouldSaveGame == "yes"):
          print(commands["save"].useCommand(None))
        print("Thanks for playing!")
        exit()
      else:
      # execute regular command
        try:
          print(commands[command].useCommand(params))
        except KeyError:
          print("command '"+ currentInput + "' not recognized. type 'help' for a list of commands")

def loadGameWorld():
  print("Please enter game folder name from list below\n" + listGames())
  gameName = input("")
  w = None
  while w == None:
    try:
      w = World(gameName)
    except:
      print(gameName + " not found.")
      print("Please enter game folder name from list below\n" + listGames())
      gameName = input("")
  print("Game loaded!")
  return w

def listGames():
  gameList = listdir('./Games')
  listString = ""
  for game in gameList:
    if(game[0] != '.'):
      listString +=("- " + game + "\n")
  return listString

if __name__ == "__main__":
    try:
      main()
    except(KeyboardInterrupt):
      print("\nExiting game...")
      exit()
