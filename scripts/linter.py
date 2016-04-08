from subprocess import run, PIPE
from sys import exit

def run_py_lint(config):
    print('Running Python linter')
    options = '--rcfile={0}'.format(config)
    journal = run(['pylint', 'journal/', options],
                             stderr=PIPE)
    cas = run(['pylint', 'cas/', options], stderr=PIPE)
    if journal.returncode or cas.returncode:
        print('There are 1 (or more) python linting error(s).')
        exit(1)
    return

if __name__ == '__main__':
    run_py_lint('.pylintrc')
    print('Lint check complete.')
