from resources.map import maptext
class Item:
  def __init__(self,description:str,movable:bool,extDescription:str):
    self.description = description
    self.movable = movable
    self.extDescription = extDescription

class Location:
  def __init__(self, description:str, items:list):
    self.description = description
    self.items = items
    self.north = None
    self.east = None
    self.south = None
    self.west = None


class World:
  def __init__(self):
    self.entrance = Location('in a grand entrance room',
                        [Item('a welcome mat',
                              False,
                              'So fancy, yet so dusty.')])

    self.hall = Location('in the main hall',[Item('set of armor',False,'Appears to be 16th century genuine chainmail.')])

    self.lounge = Location('in a room with a warm fireplace',[Item('fire poker',True,'If you touch it, your hands will be covered in soot.')])

    self.diningroom = Location('in the ornrate dining room',[Item('Solid oak dining table',False,'beautifully handcarved with elaborate designs'),Item('plate of food',True,'A plate filled with turkey, mashed popatoes and other Thanksgiving specialties.')])

    self.kitchen = Location('in a sparkling clean kitchen that smells like heaven',[Item('silver fork',True,'makes eating a plate of food a little easier'),Item('a cute puppy',True,'The puppy is sniffing the air and looking for food')])

    self.ballroom = Location('in an elegant ballroom',[Item('large pipes',False,'They seem to be connected to the study...')])

    self.mbedroom = Location('in an exquisitely furnished bedroom',[Item('a very sturdy safe',False,'has a keyhole with a familiar pattern')])

    self.library = Location('in a cozy room full of books',[Item('a well-worn book',True,'Looks like a great story. Too bad the last page is missing.')])

    self.study = Location('in the study room',[Item('large pipe organ',False,'The organ takes up almost the entire room.')])

    self.secretroom = Location('in the secret room', [Item('note', True, 'a chard small piece of paper')])

    # Set up exits
    self.entrance.west = self.lounge
    self.entrance.east = self.study
    self.entrance.north = self.hall

    self.lounge.east = self.entrance

    self.study.west = self.entrance

    self.diningroom.east = self.hall
    self.diningroom.north = self.kitchen

    self.hall.west = self.diningroom
    self.hall.east = self.library
    self.hall.north = self.ballroom
    self.hall.south = self.entrance

    self.library.west = self.hall
    self.library.north = self.mbedroom

    self.kitchen.south = self.diningroom

    self.ballroom.south = self.hall
    self.ballroom.east = self.mbedroom

    self.mbedroom.west = self.ballroom
    self.mbedroom.south = self.library

    self.secretroom.south = self.mbedroom

    self.loc = self.mbedroom
    self.inventory = [Item('letter',True,'The letter says: Welcome to the mansion! Feel free to look around and explore!'), Item('map', True, maptext),Item('a golden key',True,'looks like you might be able to unlock something with it')]

  def go(self,dir:str) -> str:
    error = "You can't go that way."
    if dir == 'n':
      if self.loc.north == None:
        return(error)
      self.loc = self.loc.north
    elif dir == "e":
      if self.loc.east == None:
        return(error)
      self.loc = self.loc.east
    elif dir == "s":
      if self.loc.south == None:
        return(error)
      self.loc = self.loc.south
    elif dir == "w":
      if self.loc.west == None:
        return(error)
      self.loc = self.loc.west
    else:
      return "invalid direction. see 'help' for details."
    return (self.look())

  def look(self) -> str:
    seen = "You are {}.".format(self.loc.description)
    return(seen)

  def carrying(self) -> str:
    if self.inventory != []:
      itemlist = 'You are carrying:'
      for i in self.inventory:
        itemlist = itemlist +' '+i.description + ","
      itemlist = itemlist.rstrip(',')
      itemlist += '.'
      return(itemlist)
    return("You aren't carrying anything.")

  def lookaround(self)-> str:
    visitems = 'You see:'
    for i in self.loc.items:
      visitems = visitems+' '+i.description+','
    visitems = visitems.rstrip(',')
    visitems += '.'
    return visitems

  def examine(self,descr:str) -> str:
    if self.inventory != []:
      for i in self.inventory:
        if descr in i.description:
          return i.extDescription
    for i in self.loc.items:
      if descr in i.description:
        return i.extDescription
    return ('There is no ' + descr + ' here.')

  def take(self,descr:str) -> str:
    for i in self.loc.items:
      if descr in i.description:
        if i.movable:
          self.inventory.append(i)
          self.loc.items.remove(i)
          return ('You pick up ' + i.description + '. ' + self.carrying())
        return ("You can't take that!")
    return ('There is no '+ descr + ' here.')

  def drop(self,descr:str) -> str:
    for i in self.inventory:
      if descr in i.description:
          self.loc.items.append(i)
          self.inventory.remove(i)
          return ('You drop ' + i.description + '. ' + self.carrying())
    return ('You are not carrying '+ descr + '.')

  def use(self,items:str)-> str:
    if ',' not in items:
      return("you must call the 'use' command with the syntax 'use item, target item'")
    thing, target = items.split(',')
    thingitem = None
    targetitem = None
    useDictionary = {
        'silver fork plate of food': 'Very tasty; maybe just a little too filling. You should have shared with the dog.',
        'a golden key a very sturdy safe': 'you opened the safe!', 'plate of food a cute puppy': 'You made a new best friend! The puppy is very happy.' }

    for i in self.inventory:
        if thing in i.description:
            thingitem = i
    for j in self.inventory:
        if target in j.description:
            targetitem = j
    for j in self.loc.items:
        if target in j.description:
            targetitem = j
    if thingitem == None:
        return('you are not carrying ' + thing)
    if targetitem == None:
        return('there is no ' + target)
    key = thingitem.description +' '+ targetitem.description
    if key in useDictionary:
      self.mbedroom.north = self.secretroom
      return (useDictionary[key])
    return("You can't use " + thing + ' on ' + target)
