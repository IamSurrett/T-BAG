from item import Item, makeItems, jsonifyItems
class Location:
  def __init__(self, jsonObj, name):
    self.name = name
    self.description = jsonObj["description"]
    self.items = makeItems(jsonObj["itemlist"])
    self.forward = jsonObj["neighbors"]["f"]
    self.right =   jsonObj["neighbors"]["r"]
    self.back =    jsonObj["neighbors"]["b"]
    self.left =    jsonObj["neighbors"]["l"]

  def jsonify(self):
    return({
      "name": self.name,
      "description": self.description,
      "itemlist": jsonifyItems(self.items),
      "neighbors": {
        "f": self.forward,
        "b": self.back,
        "l": self.left,
        "r": self.right
      }
    })
