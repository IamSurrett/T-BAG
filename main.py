from world import World
from command import Command
from helptext import helpText

def main():
    print("Welcome to T-BAG, your friendly neighborhood Text-Based Adventure Game!")
    gameName = input("Please enter game folder name (ClueHouse, or custom save folder)")
    w = World(gameName)
    currentInput = ""

    commands = {
      "go": Command(w.go,1),
      "look": Command(w.look,0),
      "whereami": Command(w.whereami,0),
      "carrying": Command(w.carrying,0),
      "lookaround": Command(w.lookaround,0),
      "examine": Command(w.examine,1),
      "take": Command(w.take,1),
      "drop": Command(w.drop,1),
      "save": Command(w.save, 0)
      # "use": Command(w.use,1)
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
        print("Thanks for playing!")
      else:
      # execute regular command
        try:
          print(commands[command].useCommand(params))
        except KeyError:
          print("command '"+ currentInput + "' not recognized. type 'help' for a list of commands")


if __name__ == "__main__":
    main()
