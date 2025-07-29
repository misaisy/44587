from flask import Flask
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=6379,
    decode_responses=True
)

@app.route('/')
def hello():
    visit_count = redis_client.incr('visit_count')
    return f"Hello, Docker! Visit count: {visit_count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)