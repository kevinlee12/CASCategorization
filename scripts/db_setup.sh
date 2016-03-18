#!/bin/sh
set -e

export OS=`uname`

if [[ "${OS}" == "Darwin" ]]; then
    echo "Creating cas db"z
    createdb cas
    echo "Creating cas_user"
    createuser --createdb -R -S cas_user
else
    if [[ $(/usr/bin/id -u) -ne 0 ]]; then
        echo "Please run me as root"
        exit
    fi
    echo "Creating cas db"
    sudo su - postgres -c "createdb cas"
    echo "Creating cas_user"
    sudo su - postgres -c "createuser --createdb -R -S cas_user"
fi
