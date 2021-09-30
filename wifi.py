import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')


profile = [i.split(":")[1][1:-1] for i in data if "all user profile" in i]

for i in profile:
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')

    result = [b.split(":")[1][1:-1] for b in result if "key content" in b]

    try:
        print("{:<30}| {:<}".format(i, result[0]))

    except IndexError:
        print("{:30}| {:<}".format(i, ""))


input("")



