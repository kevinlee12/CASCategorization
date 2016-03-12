#!/bin/sh
set -e

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Please run me as root"
    exit
fi

echo "Creating cas db"
sudo su - postgres -c "createdb cas"
echo "Creating test_cas db (for testing)"
sudo su - postgres -c "createdb test_cas"
echo "Creating cas_user"
sudo su - postgres -c "createuser cas_user"
echo "Granting permissions"
sudo su - postgres -c "psql -c 'GRANT ALL PRIVILEGES ON DATABASE cas TO cas_user;'"
sudo su - postgres -c "psql -c 'GRANT ALL PRIVILEGES ON DATABASE test_cas TO cas_user;'"
