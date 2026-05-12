import docker

client: docker.DockerClient = docker.from_env()

def line_generator(stream):
    line = ""
    for raw_line in stream:
        char = raw_line.decode("utf-8", errors="replace")
        line += char
        if char == "\n":
            yield line
            line = ""

with open("logs.txt", "a") as file:
    while True:
        container = client.containers.get("sm64coopdx-server")
        for line in line_generator(container.logs(stream=True, follow=True)):
            if "packet_chat.c" in line or ("coopnet.c" in line and "Coopnet shutdown!" in line):
                file.write(line)
                file.flush()

            if "Coopnet shutdown!" in line and "packet_chat.c" not in line:
                container.restart()