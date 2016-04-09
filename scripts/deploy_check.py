import subprocess
import sys
import os

def run_deploy_checklist():
    print('Running deployment checklist')
    os.environ['TOGGLE_PROD_SETTING'] = 'True'
    results = subprocess.run(['python', 'manage.py', 'check', '--deploy'],
                             stdout=subprocess.PIPE)
    if results.stdout != b'System check identified no issues (0 silenced).\n':
        sys.exit(1)

if __name__ == '__main__':
    run_deploy_checklist()
    print('Deployment Checklist successful')
