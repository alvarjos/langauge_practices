# API
## Postman API's
API - Application Programming Interface

Examples of API's I've used today
- Spotify
- Youtube
- Instagram

REST API's -
Representational State Transfer

* REST API Checklist
1. Client Server Architecture
2. Statelessness
3. Cacheability
4. Layered System
5. Code on Demand
6. Uniform Interface

* API Gateway HTTP API - A collection of routes and methods that are integrated with backend HTTP endpoints or Lambda functions. You can deploy this collection in one or more stages. Each route can expose one or more API methods that have unique HTTP verbs supported by API Gateway

* API endpoint - A hostname for an API in API Gateway that is deployed to a specific Region. The hostname is of the form {api-id}.execute-api.{region}.amazonaws.com. The following types of API endpoints are supported:<br>
- Edge-optimized API endpoint
- Private API endpoint
- Regional API endpoint

* API key - An alphanumeric string that API Gateway uses to identify an app developer who uses your REST or WebSocket API. API Gateway can generate API keys on your behalf, or you can import them from a CSV file. You can use API keys together with Lambda authorizers or usage plans to control access to your APIs.

* Mapping Template - A script in Velocity Template Language (VTL) that transforms a request body from the frontend data format to the backend data format, or that transforms a response body from the backend data format to the frontend data format. Mapping templates can be specified in the integration request or in the integration response. They can reference data made available at runtime as context and stage variables. The mapping can be as simple as an identity transform that passes the headers or body through the integration as-is from the client to the backend for a request. The same is true for a response, in which the payload is passed from the backend to the client.

* Quick create - You can use quick create to simplify creating an HTTP API. Quick create creates an API with a Lambda or HTTP integration, a default catch-all route, and a default stage that is configured to automatically deploy changes. 

* Route - A WebSocket route in API Gateway is used to direct incoming messages to a specific integration, such as an AWS Lambda function, based on the content of the message. When you define your WebSocket API, you specify a route key and an integration backend. The route key is an attribute in the message body. When the route key is matched in an incoming message, the integration backend is invoked. A default route can also be set for non-matching route keys or to specify a proxy model that passes the message through as-is to backend components that perform the routing and process the request.


Practice creating REST API using API Gateway REST API Console - Steps: 
1. Create a Lambda function
2. Create a REST API
3. Create a Lambda proxy integration
4. Deploy your API
5. Invoke your API
6. (Optional) Clean up<br>

### Creation Walkthrough:
https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-rest-new-console.html#getting-started-rest-new-console-create-function

In Amazon API Gateway, you build a REST API as a collection of programmable entities known as API Gateway resources. For example, you use a RestApi resource to represent an API that can contain a collection of Resource entities.

Each Resource entity can have one or more Method resources. A Method is an incoming request submitted by the client and is expressed in the request parameters and body. It defines the application programming interface for the client to access the exposed Resource. To integrate the Method with a backend endpoint, also known as the integration endpoint, you create an Integration resource. This forwards the incoming request to a specified integration endpoint URI. If necessary, you can transform request parameters or request body to meet the backend requirements.

For responses, you can create a MethodResponse resource to represent a request response received by the client and you create an IntegrationResponse resource to represent the request response that is returned by the backend. You can configure the integration response to transform the backend response data before returning the data to the client or to pass the backend response as-is to the client.

## API Gateway Rest API's

### API Gateway Endpoint Types
An API endpoint type refers to the hostname of the API. The API endpoint type can be edge-optimized, regional, or private, depending on where the majority of your API traffic originates

* Methods for REST APIs in API Gateway
In API Gateway, an API method embodies a method request and a method response. You set up an API method to define what a client should or must do to submit a request to access the service at the backend and to define the responses that the client receives in return. For input, you can choose method request parameters, or an applicable payload, for the client to provide the required or optional data at run time. For output, you determine the method response status code, headers, and applicable body as targets to map the backend response data into, before they are returned to the client. To help the client developer understand the behaviors and the input and output formats of your API, you can document your API and provide proper error messages for invalid requests.



## AWS Data Types
Resource - Contents
* id - The resource's identifier.<br>
Type: String<br>
Required: No

* parentId - The parent resource's identifier.<br>
Type: String<br>
Required: No

* path - The full path for this resource.<br>
Type: String<br>
Required: No

* pathPart - The last path segment for this resource.<br>
Type: String<br>
Required: No

* resourceMethods - Gets an API resource's method of a given HTTP verb.<br>
Type: String to Method object map<br>
Required: No<br>

Method - Represents a client-facing interface by which the client calls the API to access back-end resources. A Method resource is integrated with an Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a Method resource, whereas an integration request is embodied in an Integration resource. On the other hand, a method response is represented by a MethodResponse resource, whereas an integration response is represented by an IntegrationResponse resource.
