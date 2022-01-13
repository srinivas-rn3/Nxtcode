#!/usr/bin/env bash
#
# Moves files from a local directory to an S3 bucket.
#   - Lists the files in the local directory.
#   - Uses aws-cli to copy the file to S3 location.
#   - S3 file is: <base uri>/<date file last modified>/<filename>
#   - If the move is successful the file is deleted from local dir.
#   - Logs to STDOUT
#
# Example: ./move_logs_to_s3.sh /log s3://massive-bucket/log-bkp

DIR=${1:-"/log"}
BASES3URI=${2:-"s3://microfocus-edu-20210505/log-bkp"}
DATESTART=$(date +%F)

function log {
  echo "[$(date --rfc-3339=seconds)]: $*"
}

function move_files {

  for f in `find ${DIR} -type f`
  do
    datepart=$(date +%F -r $f)
    filename=$(basename $f)
    s3uri="${BASES3URI}/$datepart/$filename"
    cmd="aws s3 cp ${f} ${s3uri}"

    log "Moving: $f to $s3uri"
    output="$(${cmd} 2>&1)"

    if [ $? -eq 0 ]; then
      log "Deleting: $f"
      rm -f $f
    else
      log "Failed: $output"
    fi

  done
}

function ensure_only_running {
  if [ "$(pgrep -fn $0)" -ne "$(pgrep -fo $0)" ]; then
    log "Detected multiple instances of $0 running, exiting."
    exit 1
  fi
}

log "Starting to move files ($DATESTART)"
ensure_only_running
move_files
echo "Finished."
