FROM python:3.12.1-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY src/ .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Word_Cloud_App.py"]
