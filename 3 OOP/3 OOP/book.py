class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = None
        
    def set_discount(self, discount):
        self.__discount = discount
    
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
    
    def __repr__(self):
        return f"Titulo:'{self.title}', Cantidad: {self.quantity}, Autor: {self.author}', Precio:{self.price}"
        
book1 = Book('El Señor de los Anillos', 30, 'J.R.R. Tolkien', 22)
book2 = Book('El cuento de la Criada', 20, 'Margaret Atwood', 30)
book3 = Book('Reina Roja', 25, 'Juan Gómez Jurado', 28)

print(book1) 
print(book2)  
print(book3)  