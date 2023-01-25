import os, platform

os.system('git pull')

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from SxS2 import login

    login()

elif bit == '32bit':

    from SxS1 import login

    login()
