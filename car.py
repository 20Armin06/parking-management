from datetime import *
class Car :
    def __init__(self,pelak,rang,model):
        self.pelak =pelak
        self.rang = rang
        self.model = model
        self.time = datetime.now()
    def info_mashin(self):
        return f"مدل = {self.model} و پلاک خودرو ={self.pelak} و رنگ خودرو ={self.rang} و زمان ورود خودرو ={self.time.strftime("%Y-%m-%d %H:%m")}"


