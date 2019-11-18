class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None):
      self.total = 0
      self.employee_discount = employee_discount
      self.items = []
      
    def add_item(self, name=None, price=None, quantity=1):
      for num in range(quantity):
        self.total += price
        self.items.append({'name' : name, 'price' : price})
      return self.total
     
    def mean_item_price(self):
      return self.total / len(self.items)

    def median_item_price(self):
      numbers = []
        
      for item in self.items:
        numbers.append(item['price'])
      
      numbers.sort()
      
      half = len(numbers)/2
      if half%2 == 0:
        return (numbers[half] + numbers[half + 1])/2
      else:
        return numbers[int(half + 0.5)]
          

    def apply_discount(self):
      if self.employee_discount == None:
        return 'Sorry, there is no discount to apply to your cart :('
      else:
        return self.total * ((100 - self.employee_discount)/100)
       

    def void_last_item(self):
      if self.items == []:
        return 'There are no items in your cart!'
      else:
        self.total -= self.items[-1]['price']
        del self.items[-1]
      
      
