book = {'书名': '三体', '价格': 20, '作者': '刘慈欣'}
books = []
books.append({'书名': '红楼梦', '价格': 30, '作者': '曹雪芹'})
books.append({'书名': '三体', '价格': 20, '作者': '刘慈欣'})
books.append({'书名': '流浪地球', '价格': 40, '作者': '刘慈欣'})
print(books)
for b in books:
    b.pop('作者')
    print(b)
print(book.keys())
print(book.values())
print(book.items())
for k, v in book.items():
    print(k)
    print(v)
for i in book.items():
    print(i)
dict1 = {'a': 10, 'b': 20}
book.update(dict1)
print(book)
print(dict.fromkeys(['c', 'd'], 3))

