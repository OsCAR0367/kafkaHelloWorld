from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'hello-world-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='hello-world-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumidor iniciado. Esperando mensajes...")

for message in consumer:
    print(f"Recibido: {message.value}")
