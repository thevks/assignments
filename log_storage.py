#!/usr/bin/env python3
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

#es = Elasticsearch(["localhost:9200"])
es = Elasticsearch(["http://localhost:9200"])

consumer = KafkaConsumer('logs', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    log = message.value
    #print(log)
    es.index(index="logs", document=log)
