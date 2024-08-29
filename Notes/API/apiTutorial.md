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


cURL is a command that we can run from our terminal

curl --request GET \ -url 'https://api.spotify.com/v1/search?q=travis+scott&type=artist' \ -header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'

curl --request GET \ --url https://api.spotify.com/v1/artists/0Y5tJX1MQlPlqiwlOH1tJY/albums \ --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'