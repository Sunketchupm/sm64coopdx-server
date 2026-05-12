import docker

client = docker.from_env()
container = client.containers.get("coop-server-1")

for raw_line in container.logs(stream=True, follow=True):
    line = raw_line.decode("utf-8", errors="replace")

    if "Coopnet shutdown!" in line and "packet_chat.c" not in line:
        print("CoopNet disconnected; restarting container")
        container.restart()
        break