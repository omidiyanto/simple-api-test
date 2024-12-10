FROM python:3.10-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 9120
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "9120"]