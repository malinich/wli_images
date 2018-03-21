MONGODB_URI = "mongodb://localhost:27017"
CONSUL_HOST = ""
CONSUL_PORT
PORT =
MONGODB_URI =\

docker run --name=wli_consul --net=wli consul agent -server -ui -bootstrap -bind=127.0.0.1
docker run -d --net=wli -p 27017:27017 --name wli_mongo mongo:latest
docker run -d \
    --name=registrator \
    --net=wli\
    --volume=/var/run/docker.sock:/tmp/docker.sock \
    gliderlabs/registrator:latest \
      consul://localhost:8500