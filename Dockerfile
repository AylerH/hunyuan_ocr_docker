FROM vllm/vllm-openai:nightly

RUN curl -sL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-compat-12-9_575.57.08-0ubuntu1_amd64.deb -o /tmp/cuda-compat.deb
RUN dpkg -i /tmp/cuda-compat.deb
RUN rm /tmp/cuda-compat.deb
RUN whereis python3
RUN uv pip install --python /usr/bin/python3 transformers==4.57.1 --no-cache-dir
ENV HTTPS_PROXY=
ENV HTTP_PROXY=
