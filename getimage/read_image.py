import urllib.request
for i in range(80):
	response = urllib.request.urlopen('http://101.110.118.61/p0.xiaoshidi.net/2012/04/26043426'+str(i)+'.jpg')
	cat_img = response.read()
	with open('C:/Users/iamgeek/Desktop/comic/'+str(207+i)+'.jpg','wb') as f:
		f.write(cat_img)