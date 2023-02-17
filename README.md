# E-Doctor (Flask)
## Installation
1. Install docker and git using the [docker docs](https://docs.docker.com/engine/install/) as well as [git docs](https://git-scm.com/downloads) respectfully
2. Clone this git repo and using the command line of your OS (Windows: CMD, Linux: Terminal etc) and navigate to the cloned folder
3. Execute `docker build --tag e-doc-flask .` and `docker run -p 5000:5000 -d e-doc-flask`
4. Open a browser and make sure that the service started succesfully or open POSTMAN and test the API

### Helpful docker commands
* Stop containers `docker stop $(docker ps -a -q)`
* Remove dockers `docker rm $(docker ps -a -q)`
* Clear cache `docker system prune -a`
