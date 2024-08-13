### Simple Queue Service 

- Offers Async message based communication as aopposed to API calls
- Scalable, Highly Available, Fully Managed, and Cost Effective
- Useful in a variety of contexts: 
1. Data Processing workloads
2. Real Time Event Processing
3. Ad-hoc job queueing 


### Core Concepts
* Queue - FIFO (first in, first out)

- Publisheers/Producers(enque) is how messages are put into the Queue
- Processors/Consumers(deque) is how messages are taken out/removed/processed out of the Queue

### Example
OrdersService<br>              
    |<br>
    | OrdersAnalytics <br>
    |    Queue        <br>
    V<br>
AnalyticsService

### Message Processing Workflow
1. A message is published to the queue
2. Message is claimed by the receiver(consumer) and visibility timeout countdown starts
- Visibility Timeout allows SQS to set a thresthold of time, if they run out of time, it will be released back to the Queue
3. a. Message is processed and deleted by consumer <br>
   b. Visibility timeout expires and message is returned to queue

### Why SQS over API Calls
* Backpressure Control - Consumers can choose the rate of processing
* Fire and Forget - Publishers have no insight into client processing
* Eventual Guaraneed Processing - Great for async or non-realtime apps
* Application Decoupling - Decouple service dependencies

### Standard vs FIFO Queues
### Standard 
* Best Effort Ordering (Messages aren't always in order)
* At least Once Delivery
* Unlimited Throughput (unlimited processing, polling and publishing rate)
<br>

### FIFO
* First in First out
* Exactly once processing
* 3OO TPS Max(3000 with Batching)
* Slightly (~25%) more expensive
* Supports multiple channels of messages

### Common Patterns with SQS
- Fanout: 1 to many relationship
- Serverless Processing with Backpressure Control
- Job Buffering 

### Important Detials of SQS Queues
* Many threads/processes can POLL a Queue at once
* Only a single thread/process can process a message at once
* Long Polling is supported and encouraged
* Support for cross acount publishing/processing
* 256 KB max payload size per message
* Dead Letter Queue(DLQ) can help store failed messages for later processing
