import os, requests, re
repo, token = os.environ['GITHUB_REPOSITORY'], os.environ['PAT_TOKEN']
url = f'https://api.github.com/repos/{repo}/traffic/views'
r = requests.get(url, headers={'Authorization': f'token {token}'})
v = r.json().get('count', 0)
print(f'Fetched views: {v}')
with open('README.md', 'r+') as f:
    text = re.sub(r'views: \d+', f'views: {v}', f.read())
    f.seek(0)
    f.write(text)
    f.truncate()