from sys import exit
from random import randint

class Scene(object) :

    def enter(self) :
        print("You are exiting the game")
        exit(0)

class Engine(object) :

    def __init__(self, scene_map) :
        pass

    def play(self) :
        pass

class Death(Scene) :

    def enter(self) :
        print(f"You are unsuccessful! Try again")
        exit(0)

class CentralCorridor(Scene) :

    def enter(self) :
        print("You hear a crash on your ship and the alarms go off. A large Gorthon army appears!")
    def joke(self):
        print("What joke should you ask the Gorthon? ")

class LaserWeaponArmory(Scene) :
    def enter(self) :
        pass

class TheBridge(Scene) :
    def enter(self) :
        pass

class EscapePod(Scene) :

    def enter(self) :
        pass
    
class Map(object) :
    scenes = {
        'death': Death(),
        "central_corridor": CentralCorridor(),
        'laser_armory': LaserWeaponArmory(),
        'bridge': TheBridge(),
        'escape_pod': EscapePod()
    }
    def __init__(self, start_scene) :
        self.start_scene = start_scene
        print(start_scene)

    def next_scene(self, scene_name) :
        newroom = Map.scenes.get(scene_name)
        return newroom

    def opening_scene(self) :
        return self.next_scene(scene_name)


a_map = Map('central_corridor' )
#a_game = Engine(a_map)
#a_game.play()