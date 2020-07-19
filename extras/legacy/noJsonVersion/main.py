from resources import tba

class Command:
  def __init__(self,method,hasParams:int):
    self.method = method
    self.hasParams = hasParams

  def useCommand(self,params):
    if self.hasParams == 1:
      return(self.method(params))
    else:
      return(self.method())

def main():
    print("Welcome to T-BAG, your friendly neighborhood Text-Based Adventure Game!")
    w = tba.World()
    currentInput = ""
    helpText = """
    go (direction):
      moves you in the direction you choose.
      directions are n,s,e,w. Example: 'go n'.

    look:
      gives you a description of your current location.

    carrying:
      lists the items in your inventory.

    lookaround:
      gives you a list of items in your current location.

    examine (item):
      returns the description of item. Example: 'examine key'.

    take (item):
      adds item to your inventory.

    drop (item):
      removes item from your inventory and leaves it in your current location.

    use (item,target item):
      attempts to use the item on the target item. Example: 'use key,lock'

    exit:
      ...i'm sure you can figure this one out...
    """
    commands = {
      "go": Command(w.go,1),
      "look": Command(w.look,0),
      "carrying": Command(w.carrying,0),
      "lookaround": Command(w.lookaround,0),
      "examine": Command(w.examine,1),
      "take": Command(w.take,1),
      "drop": Command(w.drop,1),
      "use": Command(w.use,1)
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
