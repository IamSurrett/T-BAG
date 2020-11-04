import os
import json
from location import Location
from item import Item, makeItems
from player import Player
from worldsaver import saveTheWorld

class World:
  def __init__(self, game):
    self.game = game
    self.location = None
    self.locations = self.loadLocations()
    self.player = self.createPlayer()

  def createPlayer(self):
    with open(self.game + "/player.json","r") as F:
      playerInfo = json.loads(F.read())
      self.location = self.locations[playerInfo['location']]
      return(Player(playerInfo))


  def loadLocations(self):
    locationsDict = {}
    with os.scandir(self.game + '/rooms/') as locationObjects:
      for locationObjFile in locationObjects: # for each file in rooms folder
        with open(self.game + "/rooms/" + locationObjFile.name, "r") as F:
            jsontext = F.read()
            d = json.loads(jsontext)
            locationsDict[d["name"]] = Location(d,d["name"])
    return(locationsDict)


  def look(self) -> str:
    return(self.location.description)

  def whereami(self) -> str:
    return(self.player.locationName)

  def go(self,dir:str) -> str:
    directionObj = {
      'f': self.location.forward,
      'b': self.location.back,
      'l': self.location.left,
      'r': self.location.right
    }
    if(directionObj[dir] != "None"):
      self.player.locationName = directionObj[dir]
      self.location = self.locations[self.player.locationName]
      return(self.look())
    else:
      return("You can't go that way.")

  def carrying(self) -> str:
    return(self.itemLister(
      self.player.inventory,
      "You aren't carrying anything now.",
      "You are carrying:\n"
    ))

  def lookaround(self) -> str:
    return(self.itemLister(
      self.location.items,
      "There is nothing to see here.",
      "You see:\n"
    ))

  def examine(self,description):
    if self.player.inventory != []:
      for item in self.player.inventory:
        if description in item.name:
          return item.description
    for item in self.location.items:
      if description in item.name:
        return item.description
    return ('There is no ' + description + ' here.')

  def take(self,description):
    item = self.itemFinder(self.location.items, description)
    if(item != None):
      self.location.items.remove(item)
      self.player.inventory.append(item)
      return("You picked up " + item.name + ".\n" + self.carrying())
    return("There is no " + description + " to take.")

  def drop(self,description):
    item = self.itemFinder(self.player.inventory, description)
    if (item != None):
      self.player.inventory.remove(item)
      self.location.items.append(item)
      return("You dropped " + item.name + ".\n" + self.carrying())
    return("There is no " + item.name + " to drop.")

  def save(self):
    saveStatus = "Save failed. Please try again with another save name."
    failedStatus = "Save failed. Please try again with another save name."
    while saveStatus == failedStatus:
      saveStatus = saveTheWorld(self)
    return(saveStatus)

  def itemLister(self,itemList,nothingMessage,carryingMessage):
    if itemList == []:
      return(nothingMessage)
    message = carryingMessage
    for item in itemList:
      message += item.name + "\n"
    return(message)

  def itemFinder(self,itemList,description):
    for item in itemList:
      if description in item.name:
        return item
    return None
