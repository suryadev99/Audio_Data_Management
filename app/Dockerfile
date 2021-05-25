FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN pip3 install -U Werkzeug==0.16.0
# RUN pip3 install email_validator
# RUN pip3 install pyyaml

COPY src/ /app/

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["main.py"]
