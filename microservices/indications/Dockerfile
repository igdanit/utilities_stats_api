FROM python:3.11
WORKDIR /code
COPY . .
RUN pip install requirements.txt
CMD python motorService/initial_script.py \
    && python main.py