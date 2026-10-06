FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd --create-home appuser
COPY src ./src
COPY models ./models
RUN chown -R appuser:appuser /app
USER appuser
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD [ "python","-c","import urllib.request;urllib.request.urlopen('http://localhost:8000/health')" ]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t production-ml-api .
# docker run production-ml-api
# docker run -p 8000:8000 production-ml-api
# docker run --env-file .env production-ml-api