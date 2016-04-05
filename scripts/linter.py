import subprocess
import sys

def run_py_lint(config):
    print('Running Python linter')
    options = '--rcfile='.format(config)
    journal = subprocess.run(['pylint', 'journal/', options],
                             stderr=subprocess.PIPE)
    cas = subprocess.run(['pylint', 'cas/', options], stderr=subprocess.PIPE)
    if journal.returncode or cas.returncode:
        print('There are 1 (or more) python linting error(s).')
        sys.exit(1)
    return

if __name__ == '__main__':
    run_py_lint('.pylintrc')
    print('Lint check complete.')
