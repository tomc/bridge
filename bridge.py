import string

class Hand:

    cardoffsets = {'A':0,'K':1,'Q':2,'J':3,'T':4,'9':5,'8':6,
                   '7':7,'6':8,'5':9,'4':10,'3':11,'2':12,'x':12}

    def dots2id(self, dots):


        suits = dots.split('.')
        tempid = ''
        for i in range(len(suits)):
            for j in suits[i]:
                tempid += string.ascii_letters[i*13 + self.cardoffsets[j]]

        return tempid

    def dotstring(self,dots):
        if dots.count('.')!=3:
            self.id = '.'*13
        else:
            dots = dots.upper()
            mytrans = str.maketrans('+-*/01','AKQJTx')
            dots = dots.translate(mytrans)
            self.id = self.dots2id(dots)

    def __init__(self,id=None):
        self.hcpvalue = None
        if not id:
            self.id = '.' * 13
        elif len(id)==16:
            self.dotstring(id)
        else:
            self.id = id

    def __str__(self):
        return self.id

    def hcp(self):
        if not self.hcpvalue:

            hcpmap = {'a':4,'n':4,'A':4,'N':4,'b':3,'o':3,'B':3,'O':3,
                      'c':2,'p':2,'C':2,'P':2,'d':1,'q':1,'D':1,'Q':1}

            count = 0
            for i in self.id:
                if i in hcpmap:
                    count += hcpmap[i]

            self.hcpvalue = count

        return self.hcpvalue





