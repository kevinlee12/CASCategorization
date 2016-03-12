#!/bin/sh
set -e

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Please run me as root"
    exit
fi

echo "Removing cas db"
sudo su - postgres -c "dropdb cas"
echo "Creating test_cas db (for testing)"
sudo su - postgres -c "dropdb test_cas"
echo "Dropping cas_user"
sudo su - postgres -c "psql -c 'DROP USER cas_user;'"
