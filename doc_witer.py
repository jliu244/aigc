import asyncio

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from openai import OpenAI


client = OpenAI(base_url='https://api.xty.app/v1', api_key="sk-WHRCoUdd39GWq4RW084f16CeBaAc4f21BdD178F6Ba55Fd80")


prompt = """\
你是一个文档生成器，你能够根据输入的json数据结构生成文档，请把用户的输入转换成MarkDown格式文档。
文档应包括对数据整体的描述，以及每个字段的描述（使用表格），包括字段名、数据类型、是否必填、说明等信息。
"""


def generate_doc(text):
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


if __name__ == '__main__':
    # 打开文件读取json数据
    with open('data.json', 'r') as f:
        text = f.read()
        generate_doc(text)


#这段Python脚本使用了OpenAI的API，以生成来自GPT-4模型的回应。脚本设置为流式响应，意味着它会在生成回应的同时，逐块打印出来。
# 下面是对脚本的简要解释：
# 1. 导入openai库，这是OpenAI API的Python客户端。
# 2. 创建了一个OpenAI类的实例，并将API密钥和基础URL作为参数传递。
# 3. 使用client.chat.completions.create()方法创建了一个聊天完成。
# 这个方法接受一个model参数，指定使用的模型（在这种情况下，是"gpt-4"），以及一个messages参数，这是要发送给模型的消息列表。
# 列表中的每条消息都是一个字典，有两个键：role（可以是"system"、"user"或"assistant"）和content（消息的内容）。
# 4. stream参数设置为True，意味着响应将被流式处理。
# 5. 然后，脚本进入一个循环，在生成每个块的响应时打印出来。如果一个块没有任何选择或其内容是None，则跳过它。
# 6. 最后，使用一个空的print()语句在输出的末尾打印一个换行符。

