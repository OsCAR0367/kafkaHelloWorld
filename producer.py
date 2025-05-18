from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

message = {"message": "¡Hola Mundo desde Kafka!"}
print(f"Enviando mensaje: {message}")

producer.send('hello-world-topic', message)

producer.flush()
print("Mensaje enviado correctamente")
