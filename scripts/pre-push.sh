#!/bin/sh

# Verifies what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local sha1> <remote ref> <remote sha1>

# Activate cas environment. Certain checks require programs and packages
# that are guaranteed to be available in this environment.
source ~/.conda_profile
source activate cas &>/dev/null
if [ $? -ne 0 ]; then
	echo "Error while activating cas environment for checks."
	exit 1
fi

# Ensure that project files pass lint checks.
cd $(git rev-parse --show-toplevel)
python scripts/linter.py
with_error_sum+=$?

exit $with_error_sum
