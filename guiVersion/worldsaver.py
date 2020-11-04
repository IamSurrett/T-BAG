import os
import json
from location import Location
import PySimpleGUI as sg

def saveTheWorld(world):
  savename = 'Games/' + sg.popup_get_text('Enter a save name:')
  if savename == world.game:
    return("Cannot save game as original game name. Please choose another name.")
  try:
      os.makedirs(savename + '/rooms')
  except OSError as error:
      print(error)
      return("Save failed. Please try again with another save name.")

  print("saving locations...")
  for roomName in world.locations.keys():
    with open(savename + "/rooms/" + roomName + ".json",'w') as F:
      F.write(json.dumps(world.locations[roomName].jsonify()))

  with open(savename + "/player.json","w") as F:
    F.write(json.dumps(world.player.jsonify()))
    print("saving player...")

  sg.popup_ok('Game saved!')
  return("Game saved!")
