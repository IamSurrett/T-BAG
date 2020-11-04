from item import makeItems, jsonifyItems
class Player:
  def __init__(self,playerInfo):
    self.locationName = playerInfo['location']
    self.inventory = makeItems(playerInfo['inventory'])

  def jsonify(self):
    return({
      "location": self.locationName,
      "inventory": jsonifyItems(self.inventory)
    })
