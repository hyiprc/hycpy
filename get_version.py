
import re
from subprocess import check_output as sh

git_revision = sh(['git','rev-parse','HEAD']).decode('ascii').strip()
git_log = sh(['git','log','--oneline','HEAD']).decode('ascii').splitlines()

major_mark = '!'
keywords = {
'feat': 'minor',
'fix': 'micro',
}

major, minor, micro = 1, 0, 0
for line in git_log[::-1]:
    if not line: continue
    key = re.split(' +|:|\(',line.lower(),2)[1]
    if major_mark in key:
        major += 1
        minor,micro = 0,0
    elif key in keywords:
        ver = keywords[key]
        vars()[ver] += 1
        if ver=='minor': micro = 0
version = short_version = '%d.%d.%d'%(major,minor,micro)
dev,key,*_ = re.split(' +|:|\(',git_log[0].lower(),2)
if not (major_mark in key or key in keywords): version += '.dev'+dev

version_py = '\n'
for s in ('short_version','version','git_revision'):
    version_py += "%s = '%s'\n"%(s,vars()[s])

if __name__ == '__main__':
    print(version_py)
