import asyncio
import json
import random

from confluent_kafka import Consumer

BROKER_URL = "PLAINTEXT://localhost:9092"

async def consume(topic_name):
    """Consumes data from the Kafka Topic"""
    #https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=confluent_kafka%20consumer#confluent_kafka.Consumer
    c = Consumer({ "bootstrap.servers": BROKER_URL, 
                   "group.id": "0",
                   "enable.auto.commit": "false",
                   "auto.offset.reset":"earliest"
                   })
    c.subscribe([topic_name])

    while True:
        messages = c.consume()

        for message in messages:
            print(f"consume message {message.key()}: {message.value().decode('utf-8')}")
        
        await asyncio.sleep(0.01)

def main():
    try:
        asyncio.run(consume("com.udacity.crime_calls.v1"))
        
    except KeyboardInterrupt as e:
        print("Shutting down...")
    
if __name__ == "__main__":
    main()