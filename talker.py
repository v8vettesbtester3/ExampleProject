# Simple class
class Talker(object):
    def __init__(self):
        self.msg = ""

    def speak(self, phrase, loudly = False):
        if loudly:
            # speaking loudly using uppercase
            self.msg = phrase
            self.yell(self.msg)
        else:
            # speaking not loudly, normal case
            self.msg = phrase
        print(self.msg)

    def yell(self, phrase):
        print(phrase.upper())

