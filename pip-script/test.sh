#!/bin/bash
SERVERIP=104.210.8.183
##NOTIFYEMAIL=test@example.com

ping -c 3 $SERVERIP > /dev/null 2>&1
if [ $? -ne 0 ]
then
   # Use your favorite mailer here:
   #mailx -s "Server $SERVERIP is down" -t "$NOTIFYEMAIL" < /dev/null 
   echo "Server Online !!!!!!!!!"
   echo "cool"
fi
