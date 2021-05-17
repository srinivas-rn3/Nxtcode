##########################################################
# Name : CDF_Health_check.sh                             #  
# Desc : To Check the health status of the cdf           #
# Author : Srinivas and Nikitha                          #
# Email : Srinivas.rn2@microfocus.com                    #
#         nikitha.kreddy@microfocus.com                  #
# Type : shell                                           #
# OS supports : Centos 7 ,RHEL 7                         #
##########################################################

#!/bin/bash
#set -x
### Variable Assigments###

MOUNT_LOC="/var/vols/itom"
#DATE=$(date +"%Y-%m-%d")
#FILEPATH="/tmp/"
#FILENAME=CDF_STATUS_${DATE}.txt
#FULL_PATH=$FILEPATH$FILENAME

###Node Status ###

echo "----------------------Nodes Status ----------------------------"
NODES_STATUS=`kubectl get no`
printf "%-30s|%-18s|%-20s|%-20s|%-20s\n" $NODES_STATUS
echo -e "\n"
### Nodes CPU AND Memory Status #####

echo "------------------------- K8's Nodes Memory and CPU Consumption ------------------------------"
NODES_CON=`kubectl top no` 
printf "%-30s|%-18s|%-20s|%-20s|%-20s\n" $NODES_CON 
echo -e "\n"
###### Check for PODs Crash Loop Back Status####
echo "----------------- Crashloop back pods Status ------------------------------"
if [[ ! -z `kubectl get pods --all-namespaces | grep CrashLoopBackOff` ]] ; then
    echo " Crashloopback pods"
    result1=`kubectl get po --all-namespaces | grep CrashLoopBackOff`
    echo $result1
else
    echo "No pods are in CrashLoopBack state"
fi
echo -e "\n"
########## Check for PODs in Error State ######
echo "----------------- Error pods Status ------------------------------"
if  [[ ! -z `kubectl get pods --all-namespaces | grep Error` ]] ; then
    echo "fetching Error pods"
    result2=`kubectl get po --all-namespaces | grep Error`
    echo $result2
else
      echo "No pods are in Error state"
fi
echo -e "\n"
########### Checking Mount Status ######
echo "----------------- Mount Point Status ------------------------------"
if mount | grep $MOUNT_LOC > /dev/null; then
    echo "$MOUNT_LOC Moutned!!!"
else
    echo "$MOUNT_LOC Not Mounted!!!!"
fi
