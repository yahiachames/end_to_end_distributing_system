# Distributed Computing System for E-commerce Project

## **Overview**
This project implements a robust, distributed computing system for an e-commerce platform. The system is designed to handle high transactional throughput, scalable logging, and advanced analytics. The architecture leverages modern technologies to ensure fault tolerance, scalability, and efficiency.

---

## **System Architecture**

### **Architecture Diagram**
![System Architecture Diagram](https://drive.google.com/uc?id=1jaJybaEuJBMD_o2GjMXydGWYT7-rs3N0)

---

### **1. Backend and Frontend**
- **Framework**: **Django**  
  Django serves as both the backend and frontend framework, providing:
  - RESTful APIs for the frontend and external integrations.
  - Secure and efficient user authentication and session management.
  - Dynamic HTML rendering using Django templates for enhanced SEO and faster server-side rendering.

---

### **2. Transactional Data Storage**
- **Database**: **MongoDB**  
  MongoDB is used to store transactional data, including:
  - Order details, user cart items, and payment histories.
  - Document-oriented schema allows for flexible and scalable data management.
  - Support for indexing and sharding ensures high performance under heavy loads.

---

### **3. Distributed Logging System**
- **Task Distribution**: **Celery with Redis**  
  - **Celery** is employed to handle logging tasks, distributing them efficiently across workers.  
  - **Redis** acts as the message broker, facilitating communication between Celery workers and the Django application.
  - Logs are categorized into Redis channels for streamlined processing and scalability.

---

### **4. Real-Time Log Processing**
- **Log Aggregation**: **Logstash**  
  Logstash is configured to:
  - Consume logs from multiple Redis channels in real-time.
  - Transform and enrich logs for downstream analysis.
  - Forward processed logs to **Elasticsearch** for indexing.

---

### **5. Interactive Dashboards**
- **Search and Visualization**: **Elasticsearch and Kibana**  
  - **Elasticsearch** provides a powerful search and analytics engine, indexing logs for querying and monitoring.
  - **Kibana** offers an interactive dashboard to visualize logs and system metrics, enabling administrators and developers to:
    - Monitor application performance.
    - Investigate errors and performance bottlenecks.
    - Generate insights through real-time and historical data analysis.

---

### **6. Analytical Queries**
- **Ad-hoc Query System**: **Cassandra**  
  Cassandra is used to support ad-hoc analytical queries for:
  - Business analysts to explore user behavior and sales trends.
  - Marketing teams to derive actionable insights for campaigns.  

  **Key Features**:
  - Distributed architecture for horizontal scaling.
  - High throughput and low-latency queries for large datasets.

---

## **Data Flow**

1. **Django** handles user requests and processes transactions.
2. Transactional data is stored in **MongoDB**.
3. Application logs are distributed to **Redis** channels by **Celery** workers.
4. **Logstash** consumes logs from Redis, processes them, and sends them to **Elasticsearch**.
5. Logs in Elasticsearch are visualized through **Kibana** dashboards.
6. Business analysts query **Cassandra** for detailed, ad-hoc insights into sales and marketing data.

---

## **Technologies**

| Component                  | Technology              | Purpose                                      |
|----------------------------|-------------------------|----------------------------------------------|
| Backend & Frontend         | Django                 | Web application framework                   |
| Transactional Data Storage | MongoDB                | Flexible, document-oriented database        |
| Task Distribution          | Celery, Redis          | Distributed logging and message brokering   |
| Log Processing             | Logstash               | Real-time log aggregation and processing    |
| Dashboards                 | Elasticsearch, Kibana  | Log search and visualization                |
| Analytical Queries         | Cassandra              | Ad-hoc querying for large datasets          |

---

## **Key Features**

- **Scalability**: Horizontally scalable architecture with support for high traffic and data volumes.
- **Fault Tolerance**: Resilient design with Redis, Elasticsearch, and Cassandra providing redundancy and failover mechanisms.
- **Real-Time Insights**: Kibana dashboards enable real-time monitoring and analysis.
- **Flexibility**: Document-oriented MongoDB schema and ad-hoc queries in Cassandra cater to dynamic business needs.

---

## **Deployment**

The system can be deployed in a cloud environment using container orchestration tools like **Docker** and **Kubernetes** to manage services effectively. Each component runs as an independent microservice to ensure isolation and ease of scaling.

---

## **Usage**

### **1. Start the Application**
Ensure all services (**Django**, **Redis**, **MongoDB**, **Logstash**, **Elasticsearch**, **Kibana**, **Cassandra**) are running.

### **2. Monitor Logs**
Access **Kibana** dashboards to view logs, analyze metrics, and debug issues.

### **3. Query Data**
- Use **MongoDB** queries for transactional data.
- Execute **Cassandra** queries for business analysis.

---

## **Future Enhancements**

- Introduce **Kafka** for better event streaming between components.
- Implement **Prometheus** and **Grafana** for enhanced system monitoring.
- Automate scaling of services based on real-time load using **Kubernetes**.

---

## **Contributors**

- **Project Lead**: Chameseddine Yahia
- **Backend Development**: Chameseddine Yahia 
- **Database & Analytics**: Chameseddine Yahia 
- **DevOps**: Chameseddine Yahia

For inquiries or contributions, contact yahiachames@gmail.com
