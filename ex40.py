class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def linebreak(self):
        print("*" * 10)

behold_lamb = ["Now behold the lamb", "The precious Lamb of God", "Born into sin that I may live again", "Its the precious lamb of God"]

happy_bday = Song(["Happy birthday to you" , 
                    "I don't want to get sued",
                    "So I'll stop right there."] )

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

now_behold = Song(behold_lamb)

happy_bday.sing_me_a_song()

happy_bday.linebreak()

bulls_on_parade.sing_me_a_song()

bulls_on_parade.linebreak()

now_behold.sing_me_a_song()

now_behold.linebreak()