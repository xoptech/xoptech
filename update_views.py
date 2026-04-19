import os
import requests
import json
import re

token = os.environ.get('GITHUB_TOKEN')
repo = os.environ.get('GITHUB_REPOSITORY')

if not token or not repo:
    print('missing token or repo')
    exit(1)

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

url = f'https://api.github.com/repos/{repo}/traffic/views'
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f'error fetching views: {response.text}')
    exit(1)

data = response.json()
total_views = data.get('count', 0)

try:
    with open('README.md', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = '<!-- views_start -->0<!-- views_end -->'

new_content = re.sub(
    r'<!-- views_start -->.*?<!-- views_end -->',
    f'<!-- views_start -->{total_views}<!-- views_end -->',
    content,
    flags=re.DOTALL
)

with open('README.md', 'w') as f:
    f.write(new_content)
