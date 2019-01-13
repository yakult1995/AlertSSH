#!/usr/bin/env python3

import sys
import os
import datetime
import json
import dotenv
import requests

# 環境変数読み込み
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

# Slack設定
SLACK_URL = os.environ.get("SLACK_URL")
SLACK_ROOM = os.environ.get("SLACK_ROOM")

# SlackにPOSTする内容をセット
payload_dic = {
    'attachments': [
    	{
    		'color': 'warning',
    		'pretext': 'SSHログイン通知',
    		'fields': [
    			{
    				'title': 'ログインユーザ',
    				'value': sys.argv[1],
    				'short': 'true'
    			},
    			{
    				'title': '接続元IP',
    				'value': sys.argv[2].split(' ')[0],
    				'short': 'true'
    			},
    			{
    				'title': '接続先HOST',
    				'value': sys.argv[3],
    				'short': 'true'
    			},
    		]
    	}
    ],
    'channel': SLACK_ROOM,
    'username': 'SecurityBot',
    'icon_emoji': ':ghost:'
}

# SlackにPOST
r = requests.post(SLACK_URL, data=json.dumps(payload_dic))
