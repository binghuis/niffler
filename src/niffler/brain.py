from openai import OpenAI
from pydantic import BaseModel, Field

from niffler.config import settings


class Invoice(BaseModel):
    ca: str = Field(description="加密货币的 ca")


class Brain:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.xai.api_key,
            base_url=settings.xai.base_url,
        )

    def think(self):
        completion = self.client.beta.chat.completions.parse(
            model=settings.xai.model,
            messages=[
                {
                    "role": "system",
                    "content": "我将给你发加密货币的名字，你给我发 ca 地址",
                },
                {"role": "user", "content": "toly"},
            ],
            response_format=Invoice,
        )

        print(completion.choices[0].message)


if __name__ == "__main__":
    brain = Brain()
    brain.think()
