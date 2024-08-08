# AWS SIMPLE NOTIFICATION SERVICE

### What is SNS?
- Message publishing and processing service (PubSub). It allows Fanout(1 to many relationship between publisher and consumer) to millions of consumers(Email, HTTP Endpoint, SQS, Texting)
- Fully managed and durable with automatic scaling

- Consist of Topics and Subscriptions
Topic is the 1 circle sending to many (1 to many relationship)<br>
Subscription 

- 2 Ways to use SNS
Application to Person or Application to Application

1. Application to Person
Ex. Promotional Topic(message) sent to every person that signed up to a clothing stores account. Each customer and their phone numbers would have a subscription created for them.

2. Application to Application
Ex. Placing an online order, and the Customer Order Service gathers that information for the order then sends it to another application Customer Order Topic, that uses the specific info from the online order like time of day it was purchased, etc, and sends that to corrisponding applications like AWS Lambda, NodeJS App, SQS Queue, etc... It saves time and resources by outsourcing the task of saving this detailed information from the Customer Order Service to the Customer Order Topic application
