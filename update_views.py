import os, requests, re, sys
repo = os.environ.get('GITHUB_REPOSITORY')
token = os.environ.get('PAT_TOKEN')
r = requests.get(f'https://api.github.com/repos/{repo}/traffic/views', headers={'Authorization': f'token {token}'})
print('status:', r.status_code)
print('response:', r.text)
if r.status_code != 200:
    sys.exit(1)
v = r.json().get('count', 0)
with open('README.md') as f:
    c = f.read()
with open('README.md', 'w') as f:
    f.write(re.sub(r'views: \d+', f'views: {v}', c))