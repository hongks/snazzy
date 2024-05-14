FROM python:3.11

WORKDIR /snazzy

COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "--debug", "run", "--host=0.0.0.0"]
