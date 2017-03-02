#!/bin/bash

home_dir=/home/teamspeak/teamspeak3-server_linux_amd64/tsdns

cd ${home_dir}

echo ">> Starting TSDNS server..."
exec gosu teamspeak "$@"
