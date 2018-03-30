class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
"With pockets full of shells"])

hot_cross_buns = Song(["One a penny", 
two a penny", 
hot cross buns"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

hot_cross_buns()
