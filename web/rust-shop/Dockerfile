# 使用 Rust 官方镜像构建应用程序
FROM rust:latest as builder

# 设置工作目录
WORKDIR /usr/src/app

# 复制 Cargo.toml 和 Cargo.lock 文件
COPY Cargo.toml Cargo.lock ./

# 复制源代码
COPY src ./src
COPY static ./static

# 构建依赖以缓存依赖层
RUN cargo build --release

# 运行阶段，不需要再构建镜像
FROM rust:latest

# 安装运行依赖
RUN apt-get update && apt-get install -y \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /usr/src/app

# 复制构建阶段的可执行文件到运行阶段
COPY --from=builder /usr/src/app/target/release/rust-shop /usr/local/bin/rust-shop
ENV ROCKET_ADDRESS=0.0.0.0
ENV ROCKET_PORT=8000
# 暴露端口
EXPOSE 8000

COPY . /usr/src/app

# 运行应用程序
CMD ["rust-shop"]
