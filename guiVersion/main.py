#!/usr/bin/env python3
from world import World
from command import Command
from helptext import helpText
import PySimpleGUI as sg
from time import sleep
from os import getcwd

def main():
  ### GUI SETUP ###
  sg.theme('DarkBrown')
  layout = [[sg.Text('Welcome to T-BAG, your favorite Text-Based Adventure Game!', background_color=sg.theme_text_color(), text_color=sg.theme_background_color(), font='Courier 18 underline')],
            [sg.Text(size=(60,1), key='-OUTPUT-', font='Courier 18 bold')],
            [sg.Text('Enter \'start\' to get started, and \'help\' at any time to see the list of avaliable commands',size=(60,15), key='-MAIN-', font='Courier 18')],
            [sg.Input(key='-IN-', do_not_clear=False, font='Courier 18')],
            [sg.Button('Show', bind_return_key=True, visible=False), sg.Button('Exit', font='Courier 18')]]

  window = sg.Window('T-BAG', layout, use_default_focus=False)
  window.read()

  ### WORLD & GAME SETUP ###
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

  ### MAIN EVENT LOOP ###
  while True:  # Event Loop
      event, values = window.read()
      if event == sg.WIN_CLOSED or event == 'Exit':
          break
      if event == 'Show':
          currentInput = values['-IN-']
          returnValue = doGameLoop(currentInput,commands)
          # Update the "output" text element to be the value of "input" element
          window['-OUTPUT-'].update(values['-IN-'])
          window['-MAIN-'](returnValue)

  window.close()


def loadGameWorld():
  gameName = sg.popup_get_folder('Select game to load', default_path=getcwd() + '/Games/ClueHouse', initial_folder=getcwd() + '/Games')
  #gameName = 'ClueHouse'
  w = None
  while w == None:
    try:
      w = World(gameName)
    except:
      print(gameName + " not found.")
      gameName = sg.popup_get_folder('Select game to load', default_path=getcwd() + '/Games/ClueHouse', initial_folder=getcwd() + '/Games')
  print(gameName + " game loaded!")
  return w

def doGameLoop(currentInput, commands):
  # format input
  if ' ' in currentInput:
    command,params = currentInput.split(None, 1)
  else:
    command = currentInput
    params = ""
  # check for special command
  if command == 'help':
    sg.popup_scrolled(helpText,
    font='Courier 18',
    title='Help',
    non_blocking=True
    )
    return("See popup for list of commands")
  elif command == "exit":
    exitProtocol(commands)
    exit()
  else:
  # execute regular command
    try:
      return(commands[command].useCommand(params))
    except KeyError:
      return("command '"+ currentInput + "' not recognized. type 'help' for a list of commands")

def exitProtocol(commands):
  shouldSaveGame = sg.popup_yes_no('Would you like to save this game before you leave?')
  if(shouldSaveGame == "Yes"):
    return(commands["save"].useCommand(None))
  print("Thanks for playing!")
  exit()

if __name__ == "__main__":
    main()
