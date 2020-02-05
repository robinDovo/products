import os
#讀取檔案 
def read_file(filename):
	products = []
	with open(filename, 'r' ,encoding='utf-8') as f:#讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
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
	return products

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main(): 
	filename = 'products.csv'
	if os.path.isfile(filename):#檢察檔案是否存在
		print(filename + '檔執行！') 
		products = read_file(filename)
	else:
		print('檔案不存在....建立中...')

	products = user_input(products)
	write_file('products.csv', products)

main()

