# SF Crime Statistics with Spark Streaming Project
The second project of the udacity data streaming nanodegree. The goal of this project is to create a streaming application with Spark structured streaming that connects to a Kafka cluster, reads and processes the data.

## Requirements

* Java 1.8.x
* Scala 2.11.x
* Spark 2.4.x
* Kafka
* Python 3.6 or above

## Application Usage (plus screenshots and debugging instructions)

I was running the application in the workspace.

1. Run `bash start.sh` in order to start Zookeeper and Kafka server

2. Ingest data via KafkaProducer and run the Kafka server  
`python kafka_server.py`

3. Open new terminal start CLI kafka consumer to see if topic creates events  
`kafka-console-consumer --bootstrap-server localhost:9092 --topic com.udacity.crime_calls.v1 --from-beginning`
![kafka_console_consumer](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/1_kafka_console_consumer.PNG)

4. Run KafkaConsumer script  
`python consumer_server.py`
![consumer.py_console_output](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/2_consumer_py_console_output.PNG)

5. Run Spark Structured Streaming Application  
`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`

console output for events from Kafka topic (binary output)

![spark_stream_output_df](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/3_spark_stream_output_df.png)

console output for events from Kafka topic (binary output converted to string)    

![spark_stream_output_kafka_df](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/4_spark_stream_output_kafka_df.png)

console output for service_table (events dataframe with schema)  

![spark_stream_output_service_table](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/5_spark_stream_output_service_table.png)

console output for distinct_table  

![spark_stream_output_distinct_table](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/6_spark_stream_output_distinct_table.PNG)

console output for agg_df  

![spark_stream_output_agg_df](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/7_1_spark_stream_output_agg_df.PNG)

screenshot of progress reporter for agg_df  

![spark_progress_reporter_agg_df](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/7_2_spark_progress_reporter_agg_df.PNG)

screenshot of Spark UI  

![spark_ui](https://github.com/RobertBemmann/sf_crime_data_project_spark_kafka/blob/master/screenshots/8_spark_ui.PNG)

## Questions

1.How did changing values on the SparkSession property parameters affect the throughput and latency of the data?  
Through modifying the configuration values mainly the `inputRowsPerSecond` and the `processedRowsPerSecond` changed.

2.What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?  
I was checking on increasing the value for `processedRowsPerSecond`.  
spark.sql.shuffle.partitions : 10  
spark.streaming.kafka.maxRatePerPartition : 10  
spark.default.parallelism : 100

