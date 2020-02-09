from string import Template

class Cart(Template):
	delimiter='$'

class Product:
	def __init__(self,name,price):
		self.name = name
		self.price = price

	def __str__(self):
		return self.name


if __name__=='__main__':
	items = []
	items.append(dict(product=Product('Book', 1000), qty=10))
	items.append(dict(product=Product('Induction', 9000), qty=2))
	items.append(dict(product=Product('Macbook Pro', 8977.6), qty=3))
	total = 0
	tem = Cart('$product X $qty')
	for item in items:
		total += item['product'].price * item['qty']
		print(tem.substitute(item))
	print('Total = {0}'.format(total))