FROM python:3.10
WORKDIR /your-bot-name
COPY requirements.txt /your-bot-name/
RUN pip install -r requirements.txt
COPY . /your-bot-name
CMD python main.py