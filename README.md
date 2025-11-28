## Deploying HunyuanOCR with Docker

1. Download model weights from https://huggingface.co/tencent/HunyuanOCR
2. Modify the data volume and startup command in `docker-compose.yml` and `.env` according to the actual situation.
3. `docker compose up -d`
