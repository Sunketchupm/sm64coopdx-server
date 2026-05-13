import docker
import subprocess
import re
from datetime import datetime

client: docker.DockerClient = docker.from_env()
patterns = re.compile(
    r"(?P<human_time>\w{3} \w+ \d+ \d+:\d+:\d+ \d+)(?:.+?:) (?P<chat>.+)"
)
# 2026-05-13T17:25:55.155723132Z Wed May 13 17:25:55 2026 [00] [INFO] packet_chat.c: [9683671587288506465] teru: abcd

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
        init_time = datetime.now()
        for line in line_generator(container.logs(stream=True, follow=True, since=init_time)):
            if "packet_chat.c" in line or ("coopnet.c" in line and "Coopnet shutdown!" in line):
                match = patterns.search(line)
                if match != None:
                    human_timestamp = match.group("human_time")
                    chat_message = match.group("chat")
                    file.write(f"{human_timestamp} {chat_message}\n")
                else:
                    file.write(line + "\n")
                file.flush()

            if "Coopnet shutdown!" in line and "packet_chat.c" not in line:
                container.restart()