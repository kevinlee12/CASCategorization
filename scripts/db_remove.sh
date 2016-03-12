#!/bin/sh
set -e

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Please run me as root"
    exit
fi

echo "Removing cas db"
sudo su - postgres -c "dropdb cas"
echo "Dropping cas_user"
sudo su - postgres -c "dropuser cas_user"
