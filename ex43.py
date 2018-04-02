 class Scene(obj ect) :

def enter(self) :
    pass

class Engine(obj ect) :

def __init__(self, scene_map) :
    pass

def play(self) :
    pass

class Death(Scene) :

def enter(self) :
    pass

class CentralCorridor(Scene) :

def enter(self) :
    pass

class LaserWeaponArmory(Scene) :
def enter(self) :
    pass

30 class TheBridge(Scene) :
def enter(self) :
    pass

35 class EscapePod(Scene) :

37 def enter(self) :
    pass

class Map(obj ect) :

43 def __init__(self, start_scene) :
    pass

46 def next_scene(self, scene_name) :
    pass

def opening_scene(self) :
    pass


a_map = Map(' central_corridor' )
a_game = Engine(a_map)
a_game. play()