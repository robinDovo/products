import os
products = []
if os.path.isfile('products.csv'):
	print('檔案存在！')
	with open('products.csv', 'r' ,encoding='utf-8') as f:#讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = int(input('請輸入商品價格： '))
#	p = []
#	p.append(name)
#	p.append(price)
	products.append([name, price])
print(products)

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

