# start by pulling the python image and using alpine as a service
FROM python:3.8-alpine
RUN apk add --no-cache git openssh 
RUN git clone https://github.com/KarlesP/flask-chatbot.git
WORKDIR /flask-chatbot
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]