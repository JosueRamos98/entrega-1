"""API del proyecto de contenedores - Experiencia 2 - DevOps ISY2201.

Servicio independiente del frontend: tiene su propio runtime (Python 3.12)
y su propio ciclo de vida. Se comunica con el contenedor de Redis usando el
nombre de servicio "cache" que resuelve el DNS interno de Docker.
"""

import os
import socket

import redis
from flask import Flask, jsonify

app = Flask(__name__)

cache = redis.Redis(
    host=os.environ.get("REDIS_HOST", "cache"),
    port=int(os.environ.get("REDIS_PORT", "6379")),
    socket_connect_timeout=2,
    decode_responses=True,
)


@app.get("/status")
def status():
    """Incrementa el contador en Redis y devuelve el estado del servicio."""
    try:
        visitas = cache.incr("visitas")
        cache_disponible = True
    except redis.RedisError:
        visitas = None
        cache_disponible = False

    return jsonify(
        servicio="api",
        runtime="python 3.12 + gunicorn",
        contenedor=socket.gethostname(),
        cache_disponible=cache_disponible,
        visitas=visitas,
    )


@app.get("/health")
def health():
    """Sonda de vida usada por el orquestador."""
    return jsonify(estado="ok", contenedor=socket.gethostname())
