#!/bin/bash

home_dir=/home/teamspeak/teamspeak3-server_linux_amd64/tsdns

cd ${home_dir}

curl ${MEH_MAP_URL} > /home/teamspeak/teamspeak3-server_linux_amd64/tsdns/tsdns_settings.ini

nohup ./updater.py &

echo ">> Starting TSDNS server..."
exec gosu teamspeak "$@"
