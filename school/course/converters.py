

class FourDigitYeatConverter():

    regex='[0-9]{4}'

    def to_python(self,vlaue):
        return int(vlaue)

    def to_url(self,value):
        # return f'%04d'% value ["can be writen as"]
        return f'{value:4d}'