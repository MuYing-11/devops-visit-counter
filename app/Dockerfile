# 1) Image de base : python:3.12-alpine (~21 Mo) au lieu de python:3.12 (~1 Go)
FROM python:3.12-alpine

# 2) Pas de fichiers .pyc et logs affiches directement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 3) Utilisateur sans privileges : l'application ne tourne pas en root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 4) Les dependances d'abord : cette couche reste en cache
#    tant que requirements.txt ne change pas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) Le code source en dernier (c'est lui qui change souvent)
COPY app.py .

# 6) On passe a l'utilisateur non-root
USER appuser

EXPOSE 5000

# 7) Commande lancee au demarrage du conteneur
CMD ["python", "app.py"]
