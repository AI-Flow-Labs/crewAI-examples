FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install uv
RUN uv sync
CMD ["uv", "run", "run_http"]