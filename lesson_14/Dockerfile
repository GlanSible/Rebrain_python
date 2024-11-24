FROM python:3.10.12-slim
WORKDIR /app/
COPY . .

RUN python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip \
    && python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

# EXPOSE 8000

# CMD ["python","manage.py","runserver","0.0.0.0:8000"]