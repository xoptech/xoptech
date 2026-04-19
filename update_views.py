import os, requests, re
repo, token = os.environ['GITHUB_REPOSITORY'], os.environ['PAT_TOKEN']
r = requests.get(f'https://api.github.com/repos/{repo}/traffic/views', headers={'Authorization': f'token {token}'})
v = r.json().get('uniques', 0)
with open('README.md', 'r+') as f:
    t = re.sub(r'visitors: \d+', f'visitors: {v}', f.read())
    f.seek(0); f.write(t); f.truncate()