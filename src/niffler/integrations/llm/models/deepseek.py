from typing import List

from openai import OpenAI

from niffler.config import settings
from niffler.integrations.llm.message import system_message, user_message


class DeepSeek:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.deepseek.api_key,
            base_url=settings.deepseek.base_url,
        )

    def chat(self, messages: List[str]):
        response = self.client.chat.completions.create(
            model=settings.deepseek.model,
            messages=messages,
            stream=False,
        )
        print(response.choices[0].message.content)


if __name__ == "__main__":
    deepseek = DeepSeek()
    deepseek.chat(
        [
            system_message("我将给你发加密货币的名字，你给我发 ca 地址"),
            user_message("solana 上的toly"),
        ],
    )
