# Kafka Hello World Example
## SOLUCION PRACTICA DOS HELLO WORLD CON KAFKA OSCAR MAMANI AYALA
## Descripción
Este proyecto es una implementación básica de un productor y consumidor para Apache Kafka, que demuestra el funcionamiento fundamental de una plataforma de mensajería distribuida. El ejemplo muestra cómo enviar un simple mensaje "¡Hola Mundo!" a través de Kafka y cómo recibirlo con un consumidor.

## Prerequisitos
- Python 3.7 o superior
- Docker y Docker Compose
- Conexión a Internet para descargar las imágenes Docker

## Estructura del Repositorio
```
kafkaHelloWorld/
├── docker-compose.yml   # Configuración de Kafka y Zookeeper
├── requirements.txt     # Dependencias Python
├── producer.py          # Código del productor
├── consumer.py          # Código del consumidor
└── README.md            # Este archivo
```

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/kafka-hello-world.git
cd kafka-hello-world
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Iniciar los servicios de Kafka y Zookeeper:
```bash
docker-compose up -d
```

## Cómo ejecutar el ejemplo

1. Espera aproximadamente 30-60 segundos hasta que Kafka esté completamente iniciado.

2. Inicia el consumidor en una terminal:
```bash
python consumer.py
```
El consumidor se quedará esperando mensajes.

3. En otra terminal, ejecuta el productor:
```bash
python producer.py
```

4. Observa cómo el consumidor recibe e imprime el mensaje enviado.

5. Para detener los servicios cuando termines:
```bash
docker-compose down
```

## Explicación del código

### Producer (producer.py)
El productor configura una conexión a Kafka y envía un mensaje JSON simple al tema 'hello-world-topic'. Utiliza un serializador para convertir el diccionario Python a JSON y luego a bytes.

### Consumer (consumer.py)
El consumidor se suscribe al tema 'hello-world-topic', espera mensajes y los imprime cuando llegan. Está configurado para comenzar a leer desde el mensaje más antiguo disponible.

### Docker Compose (docker-compose.yml)
Configura un entorno Kafka de un solo nodo con:
- ZooKeeper: Componente necesario para la coordinación de Kafka
- Kafka Broker: El servidor que maneja los mensajes

## Conceptos básicos de Kafka
- **Topic**: Canal donde se publican los mensajes (similar a una tabla de base de datos)
- **Producer**: Aplicación que envía mensajes a un topic
- **Consumer**: Aplicación que lee mensajes de un topic
- **Broker**: Servidor que gestiona los topics y mensajes

## Solución de problemas comunes

### El comando Docker Compose falla
Asegúrate de que Docker Desktop esté en ejecución. Si el error persiste, intenta:
```bash
docker-compose down -v
docker-compose up -d
```

### El productor o consumidor no pueden conectarse
Verifica que los servicios estén en ejecución con:
```bash
docker ps
```
Si Kafka no está listo, espera un poco más y vuelve a intentarlo.

### Los mensajes no aparecen en el consumidor
Asegúrate de que tanto el productor como el consumidor estén utilizando el mismo nombre de topic.

## Recursos adicionales
- [Documentación oficial de Apache Kafka](https://kafka.apache.org/documentation/)
- [Confluent Kafka Python Client](https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html)
- [Tutoriales de Kafka](https://kafka.apache.org/quickstart)

## Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.