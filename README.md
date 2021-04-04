### Build 
```
docker build -t whitera2bit/mafia -f dockerfiles/Dockerfile .
```

### Run
```
docker run --name mafia -it whitera2bit/mafia /bin/bash
```

### RM
```
docker stop mafia && docker rm mafia
```

### Dockerhub
https://hub.docker.com/repository/docker/whitera2bit/mafia

### Run service
```
cd /app/mafia/service
python mafia_service.py
```


### Run client
```
cd /app/mafia/service
python mafia_client.py
```

### Service Config
`MIN_USERS_NUM` - minimum number of users to start a game
`MAFIA_NUM` - nubmer of mafia players

### Client commands
`GET_USERS` - get list of users
`BROADCAST` - send message to other users, during night mafia and detective can communicate using it as well
`VOTE_FINISH_DAY` - vote for end of the day
`DECISION` - used to send mafia or detective decisions
`ACCUSE` - used for voting who to kill during day


### Note
You can ran multiple sessions at once using gunicorn
