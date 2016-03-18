#!/bin/sh
set -e

export OS=`uname`

if [[  "${OS}" == "Darwin" ]]; then
    echo "Removing cas db"
    dropdb cas
    echo "Dropping cas_user"
    dropuser cas_user
else
    if [[ $(/usr/bin/id -u) -ne 0 ]]; then
        echo "Please run me as root"
        exit
    fi
    echo "Removing cas db"
    sudo su - postgres -c "dropdb cas"
    echo "Dropping cas_user"
    sudo su - postgres -c "dropuser cas_user"
fi
