from typing import List

from openai import OpenAI

from niffler.config import settings
from niffler.llm.message import system_message, user_message


# https://api-docs.deepseek.com/zh-cn/
class Grok:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.grok.api_key,
            base_url=settings.grok.base_url,
        )

    def chat(self, messages: List[str]):
        completion = self.client.beta.chat.completions.parse(
            model=settings.grok.model,
            messages=messages,
            temperature=1,
        )

        print(completion.choices[0].message)


if __name__ == "__main__":
    grok = Grok()
    grok.chat(
        [
            system_message("我将给你发加密货币的名字，你给我发 ca 地址"),
            user_message("toly"),
        ]
    )
