FROM python:3.12

WORKDIR /App

pip3 install -r requirements.txt

COPY / .

CMD ["py", "App.py"]