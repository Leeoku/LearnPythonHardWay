from sys import exit
from random import randint

class Scene(object) :

    def enter(self) :
        print("You are exiting the game")
        exit(0)

class Engine(object) :

    def __init__(self, scene_map) :
        self.scene_map = scene_map

    def play(self) :
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene!=last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()
class Death(Scene) :

    def enter(self) :
        print(f"You are unsuccessful! Try again")
        exit(0)

class CentralCorridor(Scene) :

    def enter(self) :
        print("You hear a crash on your ship and the alarms go off. A large Gorthon army appears!")
        print("What do you decide to do? Fight, run or tell a joke")
        action = input('> ')
        if action == "fight":
            print("You fire your plasma gun at him. It just reflects off. He smashes you with his fists")
            return 'death'
        elif action == "run":
            print("The Gorthon chases after you, grabs you and eats you :(")
            return 'death'
        elif action == "tell a joke":
            print("Who holds the door? HODOR!")
            print("The Gorthon scratches his head, then walks away")
        else:
            print("Try choosing another option")
            CentralCorridor()
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
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor' )
a_game = Engine(a_map)
a_game.play()