#!/usr/bin/env python3
from kafka import KafkaConsumer
import json
from datetime import datetime, timedelta

consumer = KafkaConsumer('your_kafka_topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))
heartbeat_status = {}

def check_node_status():
    now = datetime.utcnow()
    for node, last_seen in list(heartbeat_status.items()):
        if now - last_seen > timedelta(seconds=10):
            print(f"ALERT: Node {node} may have failed.")
            del heartbeat_status[node]

for message in consumer:
    data = message.value
    if data["message_type"] == "HEARTBEAT":
        node_id = data["node_id"]
        heartbeat_status[node_id] = datetime.fromisoformat(data["timestamp"])
    check_node_status()
