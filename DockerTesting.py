import docker



# failed,due to ssh
client = docker.DockerClient(base_url="tcp://192.168.0.196:22")



# client.images.list()  # docker images  显示image的信息列表

# client.containers.list()  # docker ps

client.containers.list(all=True)  # docker ps -a

#container = client.containers.get(container_id)  # 获取daodocker容器

#container.start()  # docker start container_id   开启容器