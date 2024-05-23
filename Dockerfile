FROM python:3

WORKDIR /expenses_analysis

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./scripts/main.py"]
