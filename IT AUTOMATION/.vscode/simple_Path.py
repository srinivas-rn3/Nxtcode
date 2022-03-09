import sys
import time
import os
#To get date & time
timert = time.strftime("%Y%m%d%H%M%S")
#creation of the directory for csv
dir = '/opt/nfs/UCMDB-SMAX-ETL/etl-output-csv/'
filename = timert
mode = 0o755
path = os.path.join(dir, filename)
os.mkdir(path, mode)
print(path)