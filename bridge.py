class Hand:

    def dotstring(self,dots):
        if dots.count('.')!=3:
            self.id = '.'*13
        else:
            self.id = dots

    def __init__(self,id=None):
        if not id:
            self.id = '.' * 13
        elif len(id)==16:
            self.dotstring(id)
        else:
            self.id = id

    def __str__(self):
        return self.id

