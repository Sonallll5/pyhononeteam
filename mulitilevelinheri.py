class Baseclass:
    def msg(self):
        return "hi"
    
class Childclass(Baseclass):
    def msg2(self):
        print("hi child")
class Grandchild(Childclass):
    def msg3(self):
        print("hi grandchild")
obj=Grandchild()
