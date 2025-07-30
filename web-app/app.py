#Project 1: web-app app.pyThis is the simple Flask application that connects to Redis.from flask import Flask
from redis import Redis
import os

from flask import Flask
app = Flask(__name__)
# Connect to Redis. The hostname 'redis-cache' comes from the service name in docker-compose.yaml
# Default Redis port is 6379.
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis-cache'), port=6379)

@app.route('/')
def hello():
    # Increment the 'hits' counter in Redis
    # decode_responses=True makes Redis return strings instead of bytes
    visits = redis.incr('visits')
    return f'Hello from Project 1! I have been visited {visits} times.\n'

if __name__ == "__main__":
    # In a Docker environment, Flask should listen on 0.0.0.0
    # The port is exposed in the Dockerfile and mapped in docker-compose.
    #app.run(host="0.0.0.0", port=5000)
    pass
