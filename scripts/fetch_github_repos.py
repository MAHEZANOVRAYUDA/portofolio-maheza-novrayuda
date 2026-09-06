import urllib.request
import json

url = 'https://api.github.com/users/MAHEZANOVRAYUDA/repos?per_page=100&sort=updated'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(f"Total Repos: {len(data)}")
        for r in data:
            desc = r.get('description') or 'No description'
            print(f"- {r['name']} ({r.get('language')}) :: {desc} :: {r['html_url']}")
except Exception as e:
    print('Error:', e)
