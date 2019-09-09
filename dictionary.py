d ={'Mike' : 95, 'Bob' : 90, 'Tom' : 50}
a = d['Bob']
print(a)


d['New'] = 30
print(d)


d['Mike'] = 5

print('Anna' in d)
print('Mike' in d)


print('result of get:', d.get('Anna'))
print('result of get:', d.get('An', "doesn't exist"))
print('result of get:', d.get('An', -1))
print(d.get('Mike'))