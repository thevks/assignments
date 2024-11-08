# alerting_system.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('logs', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    log = message.value
    if log["log_level"] in ["WARN", "ERROR", "FATAL"]:
        print(f"ALERT: {log['log_level']} from {log['service_name']} - {log['message']}")
