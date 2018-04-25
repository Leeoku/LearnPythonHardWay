from sys import exit
from random import randint
from textwrap import dedent

class Scene(object) :

    def enter(self) :
        print("You are exiting the game")
        exit(1)

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
            return 'laser_armory'
        else:
            print("Try choosing another option")
            CentralCorridor()
class LaserWeaponArmory(Scene) :
    def enter(self) :
        print("You run into the Laser room to try and find the bomb to blow up the Gorthons. You see a locked keypad. What do you put?")
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print (code)
        guess = input('>')
        tries = 0
        while tries < 3 and guess!=code:
            print(f"Bzzz, incorrect code. Try again")
            tries+=1 
            guess =input('>')

        if guess == code:
            print(f"The door unlocks and you grab the bomb")
            return 'bridge'
        else:
            return 'death'
class TheBridge(Scene) :
    def enter(self) :
        print(f"You run into the bridge with bomb in hand and see a giant Gothon in the way")
        print(f"What do you do? Throw the bomb or run")
        action = input('>')
        if action == "throw bomb":
            print(dedent("""
            With your only weapon, you hurl the bomb at the Gothon's head. It explodes and sends
            it flying into a large spike, impaling it.
            """))
            return 'escape_pod'
        elif action =='run':
            print(f"The Gothon jumps onto you and eats your head!")
            return 'death'
        else:
            print(f"Try another option!")

class EscapePod(Scene) :

    def enter(self) :
        print(f"You run into the escape pod room and sees three ships ready to go out. Which do you choose?")
        working_pod = randint(1,3)
        pod_guess = input('>')
        if pod_guess == working_pod:
            print("You hop into the pod and successfully escape!")
            return 'finished'
        else:
            print("You jump into the pod and fly out, but hear a clunking sound. The engine explodes and you die!")
            return 'death'
class Finished(Scene):
    def enter(self):
        print('You won! GG')
        return 'finished'


class Map(object) :
    scenes = {
        'death': Death(),
        "central_corridor": CentralCorridor(),
        'laser_armory': LaserWeaponArmory(),
        'bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'finished': Finished()
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