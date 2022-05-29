#!/bin/sh
#DATABASE=pg_database_name
#USERNAME=pg_username
#HOSTNAME=pg_hostname
#export PGPASSWORD=pg_db_password
#psql -h $HOSTNAME -U $USERNAME:$PGPASSWORD $DATABASE << EOF
#select * from table_name
DATABASE=oo
USERNAME=postgres
HOSTNAME =
PASSWORD= 'KinAbAlu20'
psql -h $HOSTNAME -U $USERNAME:$PASSWORD $DATABASE << EOF

EOF