from celery import shared_task
import redis
import json

@shared_task
def notify_redis_of_product_creation(product_data):
    """
    Sends product creation information to a Redis list.
    """
    r = redis.Redis(host='redis', port=6379, db=0)
    product_json = json.dumps(product_data)
    # Push to a Redis list instead of publishing
    r.rpush('celery_tasks', product_json)
    r.rpush('elastic_tasks', product_json)
    r.rpush('cassandra_tasks', product_json)
    return f"Product {product_data['title']} added to Redis list"
