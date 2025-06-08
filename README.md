# issues to blog

# ---WIP -----
### Build your own 
1. change in file `scripts/export_issues.py` 
   ```
   REPO = "XuperX/blog"
   TOKEN = os.getenv("GH_TOKEN")
   ```
2. change in file index.html
   ```
   # 1
   owner: 'xuperx',
   repo: 'blog',
   });
   
   #2 
   .filter(issue => issue.user.login === 'xuperx')
   ```
### Update your site
```
GH_TOKEN=$(cat ~/TOKEN/gh_token) python scripts/export_issues.py
git add .
git commit -m "update issues"
git push
```

# notes:
1. currrently, it shows all issues. 
   to show selected issues only change `.filter(issue => issue.user.login === 'xuperx')`

# todo 
1. the github action is not setup properly yet. 
   needs to manually update it. 
2. test for issue delete and other changes