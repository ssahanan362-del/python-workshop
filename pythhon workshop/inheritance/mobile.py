class mobile:
    def __init__(self):
        pass
    def callings(self):
        print("invoking calling function")

    def sms(self):
        print("invoking sms method")

    def games(self):
        print("invoking games")

class samsungfold(mobile):
    def camera(self):
        print("capturing")

    def music(self):
        print("invoking the music method")

    def vedio_call(self):
        print("invoking the vedio call method")

samsung=samsungfold()
samsung.music()
