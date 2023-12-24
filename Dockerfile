FROM python:3.12   
 
WORKDIR /home/app  
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip  
 
COPY . .  

RUN pip install -r requirements.txt  

EXPOSE 8000  

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver"]