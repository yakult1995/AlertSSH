#!/bin/bash

source ~/.bash_profile
cd ~/AlertSSH
pipenv run python ssh_slack.py "$USER" "$SSH_CLIENT" "$HOSTNAME"