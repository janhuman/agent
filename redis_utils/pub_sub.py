import redis
import threading

import yaml

# 加载YAML配置文件
with open("config/lbai-agent.yml", "r") as file:
    config_data = yaml.safe_load(file)

# 获取redis配置
redis_config = config_data["redis_config"]


def publish_message(channel, message):
    r = redis.Redis(
        host=redis_config["host"],
        port=redis_config["port"],
        password=redis_config["password"],
        db=redis_config["db"]
    )
    r.publish(channel, message)

def subscribe_channel(channel, callback):
    r = redis.Redis(
        host=redis_config["host"],
        port=redis_config["port"],
        password=redis_config["password"],
        db=redis_config["db"]
    )
    p = r.pubsub()
    p.subscribe(channel)

    # 在单独的线程中进行消息订阅
    thread = threading.Thread(target=listen_for_messages, args=(p,callback, ))
    thread.start()

def listen_for_messages(pubsub, callback):
    for message in pubsub.listen():
        if message.get('type') == 'message':
            channel = message['channel'].decode('utf-8')
            data = message['data'].decode('utf-8')
            print(f"Received message on channel {channel}: {data}")
            callback(channel, data)

