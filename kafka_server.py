import producer_server

BROKER_URL = "localhost:9092"

def run_kafka_server():
    # TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="com.udacity.crime_calls.v1",
        bootstrap_servers=BROKER_URL,
        client_id="crime.stats.producer"
    )

    return producer

def feed():
    producer = run_kafka_server()
    producer.generate_data()

if __name__ == "__main__":
    feed()