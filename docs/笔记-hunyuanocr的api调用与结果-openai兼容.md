# api调用
## 总览
post:
```
http://127.0.0.1:10003/v1/chat/completions
```
## 识别图片-提取为md
```
提取文档图片中正文的所有信息用 markdown 格式表示，文档中公式用 latex 格式表示，按照阅读顺序组织进行解析
```
结果：
```
{
    "id": "chatcmpl-8b28a3cd896c4ffbb1cbbcc08c575a60",
    "object": "chat.completion",
    "created": 1765175511,
    "model": "HunyuanOCR",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "# 附录A（资料性附录）石油化工压力容器法兰用垫片\n\n石油化工压力容器法兰用垫片与介质等参数的匹配可参照表A选择。\n\n## 表A 压力容器法兰垫片选用表\n\n| 介质 | 法兰公称压力（MPa） | 工作温度（℃） | 法兰型式 | 密封面 | 垫片 |  | 备注 |\n|---|---|---|---|---|---|---|---|\n|  |  |  |  |  | 型式 | 材料 |  |\n| 油品、油气、溶剂*、石油化工原料及产品$ ^{\\ast} $ | ≤1.6 | ≤200 | 甲、乙型平焊 | 平（凹凸）面 | 耐油垫、四氟垫 | 耐油橡胶石棉板、聚四氯乙烯板 | 当介质为易燃、易爆、有毒或强渗透性时，应采用凹凸面法兰 |\n|  |  | 201~250 | 长颈对焊 | 平（凹凸）面 | 缠绕垫、金属包垫、柔性石墨复合垫 | 0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、铁皮（铝皮）+特制石棉、石墨+金属骨架（0Cr13、0Cr18Ni9等） |  |\n|  | 2.5 | ≤200 | 乙型平焊 | 平（凹凸）面 | 耐油垫、缠绕垫、金属包垫、柔性石墨复合垫 | 耐油橡胶石棉板<br>0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、铁皮（铝皮）+特制石棉、石墨+金属骨架（0Cr13、0Cr18Ni9等） |  |\n|  |  | 201~250 | 长颈对焊 | 平（凹凸）面 | 缠绕垫、金属包垫、柔性石墨复合垫 | 0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、铁皮（铝皮）+特制石棉、石墨+金属骨架（0Cr13、0Cr18Ni9等） |  |\n|  | 4.0 | ≤40 | 长颈对焊 | 凹凸面 | 缠绕垫、柔性石墨复合垫 | 0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、石墨+金属骨架（0Cr13、0Cr18Ni9等） |  |\n|  |  | 41~450 | 长颈对焊 | 凹凸面 | 缠绕垫、金属包垫、柔性石墨复合垫 | 0Cr13(0Cr18Ni9)钢带+石墨带、铁皮（铝皮）+特制石棉、石墨+金属骨架（0Cr13、0Cr18Ni9等） |  |\n|  | 6.4 | ≤450 | 长颈对焊 | 凹凸面 | 缠绕垫、金属包垫 | 0Cr13(0Cr18Ni9)钢带+石墨带、铁皮（0Cr13）+特制石棉 |  |\n|  |  |  |  |  | 梯形槽 | 金属环垫 | 0Cr13、0Cr18Ni9、10 |",
                "refusal": null,
                "annotations": null,
                "audio": null,
                "function_call": null,
                "tool_calls": [],
                "reasoning": null,
                "reasoning_content": null
            },
            "logprobs": null,
            "finish_reason": "stop",
            "stop_reason": null,
            "token_ids": null
        }
    ],
    "service_tier": null,
    "system_fingerprint": null,
    "usage": {
        "prompt_tokens": 769,
        "total_tokens": 1460,
        "completion_tokens": 691,
        "prompt_tokens_details": null
    },
    "prompt_logprobs": null,
    "prompt_token_ids": null,
    "kv_transfer_params": null
}
```

## 识别图片-提取为md-忽略页眉页脚（官方推荐）
body:
 ```
{
  "model": "HunyuanOCR",
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "提取文档图片中正文的所有信息用 markdown 格式表示，其中页眉、页脚部分忽略，表格用 html 格式表达，文档中公式用 latex 格式表示，按照阅读顺序组织进行解析。" },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://work8.top/static/uploads/2025/12/2243fcd6b46d414da45a4ff91d2c34d5.png"
          }
        }
      ]
    }
  ],
  "temperature": 0.0
}
}
```
结果（耗时: 7.78 s ）(有少行、错别字、错列)：
```
{
    "id": "chatcmpl-592818502a374f269b58bb971f3d0acd",
    "object": "chat.completion",
    "created": 1765174479,
    "model": "HunyuanOCR",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "# 附录A（资料性附录）石油化工压力容器法兰用垫片\n\n石油化工压力容器法兰用垫片与介质等参数的匹配可参照表A选择。\n\n<table><caption>表A 压力容器法兰垫片选用表</caption><tr><td rowspan=\"2\">介质</td><td rowspan=\"2\">法兰公称压力<br>（MPa）</td><td rowspan=\"2\">工作温度<br>（℃）</td><td rowspan=\"2\">法兰型式</td><td rowspan=\"2\">密封面</td><td colspan=\"2\">垫片</td><td rowspan=\"2\">备注</td></tr><tr><td>型式</td><td>材料</td></tr><tr><td>油品、油气、溶剂*、石油化工原料及产品*</td><td>≤1.6</td><td>≤200</td><td>甲、乙型平焊</td><td>平（凹凸）面</td><td>耐油垫、四氟垫</td><td>耐油橡胶石棉板、聚四氯乙烯板</td><td rowspan=\"5\">当介质为易燃、易爆、有毒或强渗透性时，应采用凹凸面法兰</td></tr><tr><td rowspan=\"3\">2.5</td><td rowspan=\"3\">≤200</td><td rowspan=\"3\">201~250</td><td rowspan=\"3\">长颈对焊</td><td rowspan=\"3\">平（凹凸）面</td><td rowspan=\"3\">缠绕垫、金属包垫、柔性石墨复合垫</td><td>0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、铁皮（铝皮）+特制石棉、石墨+金属骨架(0Cr13,0Cr18Ni9等)</td></tr><tr><td>耐油橡胶石棉板</td><td>0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、铁皮（铝皮）+特制石棉、石墨+金属骨架(0Cr13,0Cr18Ni9等)</td></tr><tr><td>缠绕垫、金属包垫、柔性石墨复合垫</td><td>0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、铁皮（铝皮）+特制石棉、石墨+金属骨架(0Cr13,0Cr18Ni9等)</td></tr><tr><td rowspan=\"3\">4.0</td><td>≤40</td><td>长颈对焊</td><td>凹凸面</td><td>缠绕垫、柔性石墨复合垫</td><td>缠绕垫、柔性石墨复合垫</td><td>0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、石墨+金属骨架(0Cr13,0Cr18Ni9等)</td></tr><tr><td>41~450</td><td>长颈对焊</td><td>凹凸面</td><td>缠绕垫、金属包垫、柔性石墨复合垫</td><td>缠绕垫、金属包垫、柔性石墨复合垫</td><td>0Cr13(0Cr18Ni9)钢带+石墨带、铁皮（铝皮）+特制石棉、石墨+金属骨架(0Cr13,0Cr18Ni9等)</td></tr><tr><td>6.4</td><td>≤450</td><td>长颈对焊</td><td>凹凸面</td><td>缠绕垫、金属包垫</td><td>0Cr13(0Cr18Ni9)钢带+石墨带、铁皮（0Cr13）+特制石棉</td></tr><tr><td></td><td></td><td></td><td></td><td>梯形槽</td><td>金属环垫</td><td>0Cr13,0Cr18Ni9,10</td></tr></table>",
                "refusal": null,
                "annotations": null,
                "audio": null,
                "function_call": null,
                "tool_calls": [],
                "reasoning": null,
                "reasoning_content": null
            },
            "logprobs": null,
            "finish_reason": "stop",
            "stop_reason": null,
            "token_ids": null
        }
    ],
    "service_tier": null,
    "system_fingerprint": null,
    "usage": {
        "prompt_tokens": 786,
        "total_tokens": 1630,
        "completion_tokens": 844,
        "prompt_tokens_details": null
    },
    "prompt_logprobs": null,
    "prompt_token_ids": null,
    "kv_transfer_params": null
}
```
### 识别结果的大模型后处理
deepseek-v3:
```
# 附录A（资料性附录）石油化工压力容器法兰用垫片

石油化工压力容器法兰用垫片与介质等参数的匹配可参照表A选择。

**表A 压力容器法兰垫片选用表**

| 介质 | 法兰公称压力（MPa） | 工作温度（℃） | 法兰型式 | 密封面 | 垫片 | 材料 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 油品、油气、溶剂*、石油化工原料及产品* | ≤1.6 | ≤200 | 甲、乙型平焊 | 平（凹凸）面 | 耐油垫、四氟垫 | 耐油橡胶石棉板、聚四氯乙烯板 | 当介质为易燃、易爆、有毒或强渗透性时，应采用凹凸面法兰 |
| | 2.5 | ≤200 | 长颈对焊 | 平（凹凸）面 | 缠绕垫、金属包垫、柔性石墨复合垫 | 0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、铁皮（铝皮）+特制石棉、石墨+金属骨架(0Cr13,0Cr18Ni9等) | |
| | | 201~250 | 长颈对焊 | 平（凹凸）面 | 缠绕垫、金属包垫、柔性石墨复合垫 | 0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、铁皮（铝皮）+特制石棉、石墨+金属骨架(0Cr13,0Cr18Ni9等) | |
| | 4.0 | ≤40 | 长颈对焊 | 凹凸面 | 缠绕垫、柔性石墨复合垫 | 0Cr13(0Cr18Ni9)钢带+特制石棉（石墨）、石墨+金属骨架(0Cr13,0Cr18Ni9等) | |
| | | 41~450 | 长颈对焊 | 凹凸面 | 缠绕垫、金属包垫、柔性石墨复合垫 | 0Cr13(0Cr18Ni9)钢带+石墨带、铁皮（铝皮）+特制石棉、石墨+金属骨架(0Cr13,0Cr18Ni9等) | |
| | 6.4 | ≤450 | 长颈对焊 | 凹凸面 | 缠绕垫、金属包垫 | 0Cr13(0Cr18Ni9)钢带+石墨带、铁皮（0Cr13）+特制石棉 | |
| | | | | 梯形槽 | 金属环垫 | 0Cr13,0Cr18Ni9,10 | |
```

## 识别图片-OCR this image
 ```
 {
  "model": "HunyuanOCR",
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "OCR this image" },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://你的图片地址.jpg"
          }
        }
      ]
    }
  ],
  "temperature": 0.0
}
```
结果（耗时: 7.82 s 大小: 807 B）：
```
{
    "id": "chatcmpl-23d1c19ce7394562812a72680730df9f",
    "object": "chat.completion",
    "created": 1765174307,
    "model": "HunyuanOCR",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "根据提供的图片，石油化工压力容器法兰用垫片的选择参照表A。该表列出了不同介质、压力等级、工作温度、法兰型式、密封面、型号和材料等信息。",
                "refusal": null,
                "annotations": null,
                "audio": null,
                "function_call": null,
                "tool_calls": [],
                "reasoning": null,
                "reasoning_content": null
            },
            "logprobs": null,
            "finish_reason": "stop",
            "stop_reason": null,
            "token_ids": null
        }
    ],
    "service_tier": null,
    "system_fingerprint": null,
    "usage": {
        "prompt_tokens": 744,
        "total_tokens": 782,
        "completion_tokens": 38,
        "prompt_tokens_details": null
    },
    "prompt_logprobs": null,
    "prompt_token_ids": null,
    "kv_transfer_params": null
}
```
