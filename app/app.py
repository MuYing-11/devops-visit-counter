import os
import socket

from flask import Flask
from redis import Redis

app = Flask(__name__)

# The Redis host name is the container name on the app-network
redis = Redis(host=os.getenv("REDIS_HOST", "db-service"),
              port=int(os.getenv("REDIS_PORT", 6379)))


def build_message(hits, container_id):
    return (f"Bonjour ! Cette page a été vue {hits} fois. "
            f"Je suis le conteneur {container_id}")


@app.route("/")
def index():
    hits = redis.incr("hits")
    # Inside a container, the hostname is the short container ID
    return build_message(hits, socket.gethostname())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", 5000)))
