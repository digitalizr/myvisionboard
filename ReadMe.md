python manage.py runserver   

python manage.py migrate  
python manage.py makemigrations  

docker build -t mohanpannir08/visionboard:latest .
docker run -d -p 8000:8000 --name visionboard mohanpannir08/visionboard:latest

#if all good then push
docker push mohanpannir08/visionboard:latest 