#!/bin/bash

# Stop Odoo service
sudo systemctl stop odoo

# Remove Odoo directory
cd /opt/
sudo rm -r odoo

# Remove odoo user
sudo userdel -r odoo

# Remove postgres installation
sudo apt-get --purge remove postgresql\*
sudo rm -r /etc/postgresql/
sudo rm -r /etc/postgresql-common/
sudo rm -r /var/lib/postgresql/

# Remove remaining odoo dependencies
sudo apt-get remove --auto-remove odoo

# Clean up
sudo apt-get update
sudo apt-get autoremove

