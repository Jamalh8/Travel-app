# GET IMAGE FOR PYTHON
FROM python:3.6
# CREATE A WORKING DIRECTORY FOR APP
WORKDIR /app
# COPY THE APPLICATION 
COPY application /app/application
COPY app.py create.py requirements.txt /app/
# RUN THE REQUIREMENTS INSTALL FIRST
RUN pip install -r requirements.txt
# NOW START THE APP
ENTRYPOINT ["python3", "app.py"]