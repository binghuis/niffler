from typing import List

from openai import OpenAI

from niffler.config import settings
from niffler.llm.message import system_message, user_message


class XAI:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.xai.api_key,
            base_url=settings.xai.base_url,
        )

    def chat(self, messages: List[str]):
        completion = self.client.beta.chat.completions.parse(
            model=settings.xai.model,
            messages=messages,
            temperature=1,
        )

        print(completion.choices[0].message)


if __name__ == "__main__":
    xai = XAI()
    xai.chat(
        [
            system_message("我将给你发加密货币的名字，你给我发 ca 地址"),
            user_message("toly"),
        ]
    )
