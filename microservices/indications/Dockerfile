FROM python:3.11
WORKDIR /etc/indicationService/
COPY . .
RUN pip install -r requirements.txt
RUN python motorService/initial_script.py
CMD ["python", "main.py"]