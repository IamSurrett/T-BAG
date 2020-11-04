class Item:
  def __init__(self,jsonObj):
    self.jsonObj = jsonObj
    self.name = jsonObj["itemName"]
    self.movable = self.isMovable(jsonObj["movable"])
    self.description = jsonObj["description"]

  def isMovable(self,objMovable):
    return(objMovable == "True")

  def jsonify(self):
    return({
    "itemName":self.name,
    "movable":self.movable,
    "description":self.description
  })

def makeItems(jsonItems):
    itemList = []
    for jsonItem in jsonItems:
      itemList.append(Item(jsonItem))
    return itemList

def jsonifyItems(itemList):
  jsonList = []
  for item in itemList:
    jsonList.append(item.jsonify())
  return(jsonList)
