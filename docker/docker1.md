## Docker Tutorial Net Ninja
### https://www.youtube.com/watch?v=31ieHmcTUOk&list=PL4cUxeGkcC9hxjeEtdHFNYMtCpjNBm3h7
# Docker Crash Course Lesson 1
Docker uses Containers to run applications on isolated environments on a computer
Example
- Node app
- Reac app
- Mongo db

Containers are like a package that contains everything our application needs such as:
- Correct runtime enviornment
- Source Code 
- Dependencies
- Specific versions of Node, Python, etc...

## Example Containers
Container 1 - Node 17.2, Dependencies, source code 
Container 2 - Node 15.4, Dependencies, source code
Container 3 - Python 3, Dependencies, source code 

Containers vs VMs
Virtual Machines
- Has it's own full operating system & typically slower
Containers
- Share the host's operating system & typically quicker

# Docker Crash Course Lesson 2
### Images
Images are like blueprints for containers
- Runtime environment
- Application code
- Any dependencies
- Extra configuration (e.g. env variables)
- Commands

Images also have a file system of their own which is independent from the rest of your computer
Images are READ ONLY, once you have created an image, you can't change it 
If you need to change something, you need to create a brand new image to incoporate that change. 

- Containers are runnable instances of those images
![Image -> Container Relationship](docker\Images_to_Containers.jpg)

