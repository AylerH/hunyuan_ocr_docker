# 概览
github(0.61k,,TENCENT HUNYUAN COMMUNITY LICENSE-所有服务月活用户数超过1亿，则您必须向腾讯申请授权，python):https://github.com/Tencent-Hunyuan/HunyuanOCR
hf（2G,TENCENT HUNYUAN COMMUNITY LICENSE-所有服务月活用户数超过1亿，则您必须向腾讯申请授权，python）：https://huggingface.co/tencent/HunyuanOCR

本项目github(解决部署找不到cuda问题https://github.com/Valdanitooooo/hunyuan_ocr_docker/issues/1):https://github.com/AylerH/hunyuan_ocr_docker

特点：8G显存（RTX4060）windows上跑通（需要6G即可）

# docker compose部署 HunyuanOCR

1. Download model weights from https://huggingface.co/tencent/HunyuanOCR
2. Modify the data volume and startup command in `docker-compose.yml` and `.env` according to the actual situation.
```
注意：.env中的--model对应容器中的目录；docker-compose.yml中 volumes:左半边的路径为非容器路径；
```
3. `docker compose up -d`
### .env（环境变量配置文件）
vllm相关的变量设置，以此文件中的为主；
```
VLLM_ARGS=--trust-remote-code  --served-model-name=HunyuanOCR --model=/storage-800GB/models/models--tencent--HunyuanOCR/snapshots/987eba7a6c5efb4e37c6effc352bc03a1ca59dc5/ --limit-mm-per-prompt '{"image": 50, "video": 1}'  --gpu-memory-utilization=0.8 --max-model-len=32768 --uvicorn-log-level debug  --tensor-parallel-size 1 --enable-log-requests --no-enable-prefix-caching --mm-processor-cache-gb 0

```

## 默认参数
```
 non-default args: {'host': '0.0.0.0', 'port': 5000, 'uvicorn_log_level': 'debug', 'model': '/storage-800GB/models/models--tencent--HunyuanOCR/snapshots/987eba7a6c5efb4e37c6effc352bc03a1ca59dc5/', 'trust_remote_code': True, 'max_model_len': 32768, 'served_model_name': ['HunyuanOCR'], 'gpu_memory_utilization': 0.8, 'enable_prefix_caching': False, 'limit_mm_per_prompt': {'image': 50, 'video': 1}, 'mm_processor_cache_gb': 0.0, 'enable_log_requests': True}
 ```

