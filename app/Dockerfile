#===== The builder ======
FROM python:3.11-slim-bookworm as builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY app/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

WORKDIR /app

#===== Install dependence ====
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


#===== Runtime =========
FROM python:3.11-slim-bookworm
#==== Users privileges ====
FROM gcr.io/distroless/python3-debian12:nonroot
WORKDIR /app

#copy librery from builder 
COPY --from=builder /install /usr/local
COPY app/ .

#variable for python 
ENV PYTHONPATH="/usr/local/lib/python3.11/site-packages" \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:${PATH}"


# distrolles user is nonroot
user nonroot



EXPOSE 8080

# Guinicorn server for scaling
ENTRYPOINT ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
