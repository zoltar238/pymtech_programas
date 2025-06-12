#!/bin/bash

# vars
BACKUP_DIR=~/odoo_backups
ODOO_URL=https://sincatel.nibafadigital.com
ODOO_DATABASE=Sincatel
ADMIN_PASSWORD=Argentina1!
KEPT_BACKUPS=7

# create a backup directory
mkdir -p ${BACKUP_DIR}

# create a backup
curl -X POST \
    -F "master_pwd=${ADMIN_PASSWORD}" \
    -F "name=${ODOO_DATABASE}" \
    -F "backup_format=zip" \
    -o ${BACKUP_DIR}/${ODOO_DATABASE}.$(date +%F_%H-%M-%S).zip \
    $ODOO_URL/web/database/backup


# delete old backups
find ${BACKUP_DIR} -type f -mtime +${KEPT_BACKUPS} -name "${ODOO_DATABASE}.*.zip" -delete