FROM python:3
EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir 

COPY . /app

ENTRYPOINT ["python"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]



