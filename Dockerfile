FROM python:3.11
ADD ergasia.py .
RUN pip install requests paho.mqtt
CMD [ "python", "./main.py" ]
