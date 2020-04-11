conda install -r requirements.txt
echo 'schema.registry.url=http://localhost:8081' >> /etc/kafka/connect-distributed.properties
systemctl start confluent-zookeeper > startup/startup.log 2>&1
systemctl start confluent-kafka > startup/startup.log 2>&1
