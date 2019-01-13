## 使用方法
* VPS内にcloneして下記コマンドで事前準備  
`pipenv install`  
`chmod 777 sshlogin.sh`  
`cp sshlogin.sh /etc/ssh/sshrc`  

* .envの作成
```
SLACK_URL = 'https://hooks.slack.com/services/xx'
SLACK_ROOM = 'zz'
```

* 後はVPSにログインして通知が来れば◯