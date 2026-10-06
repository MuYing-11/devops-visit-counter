# TP1 DevOps - Visit-Counter

Flask + Redis application, containerised with Docker.

- `app/` : application, unit tests and Dockerfile
- `docker-compose.yml` + `.env` : web (scalable) + db-service (Redis, volume redis-data)
- `Jenkinsfile` : tests -> build image -> push to Docker Hub (muying11/counter-app)
- `jenkins/` : Jenkins image configured as code (polls this repo every minute)

Run: `docker compose up -d --scale web=3` then open http://localhost:8000
