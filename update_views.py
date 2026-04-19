import os, requests, re

v = requests.get(f'https://api.github.com/repos/{os.environ.get("GITHUB_REPOSITORY")}/traffic/views', headers={'Authorization': f'token {os.environ.get("PAT_TOKEN")}'}).json().get('count', 0)
c = open('README.md').read()
open('README.md', 'w').write(re.sub(r'views: \d+', f'views: {v}', c))
