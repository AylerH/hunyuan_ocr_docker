import base64
import time

from openai import OpenAI

openai_ocr_client = OpenAI(
    base_url="http://10.xx.xx.xx:10003/v1",
    api_key="xxx",
)


def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def image_ocr(image_path):
    content = [
        {
            "type": "text",
            "text": f"提取文档图片中正文的所有信息用 markdown 格式表示，其中页眉、页脚部分忽略，表格用 html 格式表达，文档中公式用 latex 格式表示，按照阅读顺序组织进行解析。"
        }
    ]
    print(f'ocr image_path: {image_path}')
    b64_img = convert_image_to_base64(image_path)
    image_message = {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/png;base64,{b64_img}",
        },
    }
    content.append(image_message)
    response = openai_ocr_client.chat.completions.create(
        model="HunyuanOCR",
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        stream=False,
        max_tokens=8192,
        temperature=0,
    )
    return response.choices[0].message.content


if __name__ == '__main__':
    start_time = time.time()
    x = image_ocr("/Users/valdanito/Downloads/imagetest1.jpeg")
    print(x)
    duration = time.time() - start_time
    print(f"{duration:.3f}")
