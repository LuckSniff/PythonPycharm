import hashlib
md5 = hashlib.md5()
md5.update(b'1024')
md5.update(b'alex')

print(md5.hexdigest())