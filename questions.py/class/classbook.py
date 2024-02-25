class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def showdetails(self):
        print(self.title)
        print(self.author)
        print(self.price)
    
b1=book('c++','daniel riitchee',500)
b1.showdetails()
        