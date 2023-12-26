FROM python:3.12   

WORKDIR /home/app  

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip  

COPY . .

RUN pip install -r requirements.txt   
RUN python3 manage.py makemigrations   
RUN python3 manage.py migrate
RUN chmod 777 db.sqlite3

RUN chmod +x entrypoint.sh
CMD [ "./entrypoint.sh" ]