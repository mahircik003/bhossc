import os
import subprocess
# import time

x = subprocess.getoutput(["git fetch"])
# x = os.popen('git fetch').read()

if x != "":
    os.system("git pull")
    print(1)
#     time.sleep(7)

    os.system("python3.9 -m pip install -r /root/project--B/requirements.txt")
    os.system("python3.9 manage.py migrate")
    os.system("systemctl daemon-reload")
    os.system("systemctl restart bhossc")
