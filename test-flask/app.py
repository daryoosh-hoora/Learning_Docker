import redis
from flask import Flask
app=Flask(__name__)
cache=redis.Redis(host='db_service', port=6379)
def get_hit_count():
	return cache.incr('hits')
@app.route('/')
def main():
	count=get_hit_count()
	return 'Counter is: {}'.format(count)
