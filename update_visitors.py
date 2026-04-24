import requests, re
r = requests.get('https://hits.dwyl.com/xoptech/xoptech.json')
v = r.json().get('message', '0')
with open('README.md', 'r+') as f:
    t = re.sub(r'visitors: \d+', f'visitors: {v}', f.read())
    f.seek(0)
    f.write(t)
    f.truncate()