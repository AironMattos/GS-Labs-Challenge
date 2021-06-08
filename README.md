# GS-Labs-Challenge




## Como rodar e como utilizar?  :zap:
```bash
git clone https://github.com/AironMattos/GS-Labs-Challenge.git

cd GS-Labs-Challenge

env\Scripts\activate

docker-compose build --no-cache

docker-compose up -d

docker-compose exec web python manage.py makemigrations

docker-compose exec web python manage.py migrate
```

---
