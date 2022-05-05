## Deploy project

### Postgres
```
psql postgres
>> create database dname; 
>> create user slovo_user with password 'password';
>> grant all privileges on database dname to slovo_user;
```

### Python
```
apt install python3
apt install virtualenv
virtualenv -p python3 env
source env/bin/activate

```

### Redis

```
brew install redis-server
brew services start redis
```

### Django

```

pip install -r req.txt (pip3 install -r req.txt)
python manage.py migrate

python manage.py runserver 
```

### Celery
```
. celery.sh
```
