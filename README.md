# Real-Time Stock Market Analysis System

## Problem Definition
_News feeds, stock prices, social media sentiment, and economic indicators shape the stock market.
Integrating and analyzing these diverse data streams in real-time is a significant challenge,
but it can provide valuable insights into market trends and potential investment opportunities._

## Project Objectives
1. Demonstrate a system for real-time stock market prediction and analysis.
2. Provide insights into the stock market and allow users to monitor stock prices effectively
2. Using Apache Spark for data analysis and Apache Kafka for data collection.


## Project Overview

This project implements a real-time stock market analysis system using Apache Kafka, Apache Spark, and Python.
It simulates stock market transactions, processes them in real-time, and provides visual analytics using Seaborn.
Originally, we planned to display the data using the open source Grafana platform and upload the data from our consumer to InfluxDB that would be connected to Grafana.
Due to time constraints, we opted for a local visualization using Seaborn, but the system is designed to be easily integrated with Grafana and InfluxDB.
We also attached to this project the older version where we tried to implement the connection to Grafana and InfluxDB.



## Components
1. **One-Time-Script**:
    We used to generate the data and save it in a csv file to be used in the second part of the project.
    Originally, we wanted to use live-real data, but we couldn't find a free API that provides this data.
    Therefore, we decided to write a script that generates the data and save it in a csv file using the `yfinance` library.
2. **Kafka Producer (`kafkaProducer.ipynb`)**: 
   - Generates mock stock market transaction data
   - Publishes data on a Kafka topic called 'transactions'
3. **Spark Consumer (`pysparkConsumer.ipynb`)**: 
   - Subscribe to the Kafka topic
   - Processes incoming data using Spark Structured Streaming
   - Enriches data with static stock information
   - Performs real-time analysis
   - Visualizes results using Seaborn

## Key Features

- Real-time data processing and analysis
- Data enrichment with static stock information
- Six different types of analysis:
  1. Daily industry growth (heatmap)
  2. Transaction type distribution (buy/sell)
  3. Daily trading volume per stock
  4. Identification of highest average trading volume stock
  5. Growing companies by country (heatmap)
  6. Growing technologies market (heatmap)
- Local visualization of results using Seaborn


## Technologies Used
### Apache Kafka
- Used for real-time data streaming
- Implements a producer-consumer model for stock market transactions
- Enables decoupling of data production and consumption

### Apache Spark
- Core distributed data processing engine
- Utilized for real-time data processing and analysis
- Spark version: [Specify the version you're using]

### PySpark
- Python API for Apache Spark
- Enables writing Spark applications using Python

### Jupyter Notebook
- Interactive development environment
- Used for both the Kafka producer and Spark consumer implementations

### Seaborn and Matplotlib
- Python data visualization libraries
- Used for creating real-time visualizations of analysis results

## Spark Capabilities and Features Utilized

| Feature | Description | Application in Project |
|---------|-------------|------------------------|
| Structured Streaming | Core feature for processing real-time data | Implements micro-batch processing model for Kafka streams |
| DataFrame API | Used for structured data manipulation | Enables SQL-like queries on streaming data |
| User-Defined Functions (UDFs) | Custom functions applied to DataFrame columns | Used for data enrichment and complex calculations |
| Window Operations | Applied for time-based aggregations | Analyzes trends over specific time periods |
| Stateful Processing | Maintains state across micro-batches | Essential for cumulative calculations and trend analysis |
| Join Operations | Enriches streaming data with static data | Implements broadcast joins for efficiency |
| Aggregation Functions | Used for various analytical calculations | Includes sum, average, count, etc. |
| Custom Aggregation (UDAF) | Implemented for complex aggregations | Used when built-in functions are insufficient |
| Event Time Processing | Utilizes event time for accurate analysis | Handles late-arriving and out-of-order events |
| Watermarking | Implemented to handle late data | Maintains system stability with unbounded data |
| Output Modes | Utilizes append, update, complete modes | Applied as needed for various analyses |
| Trigger Intervals | Configures micro-batch intervals | Balances throughput and latency |
| Checkpointing | Implements fault-tolerance mechanism | Allows recovery in case of failures |
| Performance Optimizations | Utilizes caching and persistence | Implements broadcast variables for efficient data sharing |
| Data Enrichment | Joins streaming data with static data | Utilizes broadcast hash joins for performance |
| Complex Event Processing | Implements pattern matching | Detects sequences in transaction streams |
| Schema Inference and Enforcement | Automatically infers schema from JSON | Ensures data consistency |
| Error Handling | Implements handling for corrupt records | Performs data quality checks on incoming streams |
| Interactive Queries | Allows ad-hoc queries on streaming state | Enables real-time data exploration |
| Continuous Applications | Implements long-running analytics | Provides updateable analytics capabilities |

This project showcases a comprehensive use of Spark's streaming capabilities, demonstrating its power in real-time data processing and analysis. The combination of Structured Streaming with various Spark SQL and DataFrame operations allows for complex, real-time analytics on high-volume stock market data.
## Prerequisites

- Apache Kafka
- Apache Spark
- Python 3.x
- Jupyter Notebook
- Required Python libraries: 
  - `confluent_kafka`
  - `pyspark`
  - `pandas`
  - `seaborn`
  - `matplotlib`

## Setup and Installation

**The project is set up to run on the vlabs server.**
The following steps are assuming that you are using the vlabs server, if you are using your local machine please jump to the next section.

1. Enter the vlab server.
2. Clone the project to a local directory.
3. Open a new terminal and run the following commands:
    ```bash
    cd  /usr/local/kafka/kafka_2.13-3.2.1
    bin/zookeeper-server-start.sh    config/zookeeper.properties &
    ```
4. Open a new terminal and run the following commands:
    ```bash
    cd  /usr/local/kafka/kafka_2.13-3.2.1
    bin/kafka-server-start.sh        config/server.properties &
    ```
5. Move to the project directory, choose the producer directory.
6. The directory should contain two csv files `mock_transaction_data.csv` and `order_flow_data.csv`, verify both files exist, the `order_flow_data.csv` is a smaller file, we advise starting running the app with it.
7. In the directory run the following command:
    ```bash
    pyspark       --packages      org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2
    ```
8. Open the `kafkaProducer.ipynb`, verify that the match csv file is being read, and run the notebook.
9. Move to the project directory, choose the consumer directory.
10. In the directory run the following command:
    ```bash
    pyspark       --packages      org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2
    ```
11. Open the `pysparkConsumer.ipynb`, verify that the match csv file is being read, and run the notebook.


#### If you are using your local machine, please follow the following steps:**
1. Install Apache Kafka and Apache Spark on your local machine.
2. Install Zookeeper and Kafka servers.
3. Install the required Python libraries.
4. configure and start the Zookeeper and Kafka servers.
5. keep from step 5 in the previous section.


## Conclusion

This real-time stock market analysis system demonstrates the power of combining Apache Kafka and Apache Spark for processing and analyzing high-volume, fast-moving financial data. By leveraging these technologies, we've created a robust platform capable of providing valuable insights into market trends and stock performance.

While our system offers impressive capabilities for data processing and visualization, it's important to remember that the stock market is influenced by countless factors, many of which are unpredictable. This tool should be viewed as one of many in an investor's toolkit, not as a crystal ball for market prediction.

We hope this project serves as a valuable learning resource for those interested in real-time data processing, financial technology, and the practical applications of big data tools. As markets evolve and new technologies emerge, so too will the opportunities for innovative analysis and insight.

Remember: in the world of stock trading, past performance is no guarantee of future results – but a well-designed data pipeline certainly doesn't hurt!