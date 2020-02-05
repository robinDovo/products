products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = int(input('請輸入商品價格： '))
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

with open('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

