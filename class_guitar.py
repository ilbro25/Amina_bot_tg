class Guitar:
    def __init__(self,brand = 'Fender',form = 'LesPoul', price = '30000'):
        self.brand = brand
        self.form = form
        self.price = price
        
    
    def play(self):
        print('Играет')
    def tune(self):
        print('Настроена')
    def info(self):
        guitar_info = ('Бренд гитары: '+ self.brand+',\nФорма гитары: '+ self.form)
        return guitar_info

