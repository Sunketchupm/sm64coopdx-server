FROM debian:bookworm-slim AS build

RUN apt-get update && \
    apt-get install -y \
        binutils-mips-linux-gnu \
        bsdmainutils \
        build-essential \
        libcapstone-dev \
        pkgconf \
        python3 \
        libz-dev \
        libcurl4-openssl-dev \
        git \
        libsdl2-dev

WORKDIR /sm64
ENV PATH="/sm64/tools:${PATH}"

COPY sm64coopdx .
RUN make -j16 DISCORD_SDK=0 RENDER_API=DUMMY WINDOW_API=DUMMY

FROM debian:bookworm-slim AS release

RUN apt-get update && \
    apt-get install -y \
        libsdl2-2.0-0 \
        libcurl4

WORKDIR /sm64
COPY --from=build /sm64/build/us_pc/sm64coopdx /sm64/sm64coopdx

# docker build -t sm64coopdx .
# docker run --rm --mount type=bind,source="$(pwd)",destination=/sm64 sm64coopdx make -j HEADLESS=1
# see https://github.com/n64decomp/sm64/blob/master/README.md for advanced usage
