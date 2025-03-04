import base64
import json
import os

from openai import OpenAI

from niffler.config import settings
from niffler.llm.message import system_message, user_message
from niffler.llm.prompts.kimi import x_screenshot_extraction_prompt


class Kimi:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.kimi.api_key,
            base_url=settings.kimi.base_url,
        )

    def chat(self, messages):
        completion = self.client.chat.completions.create(
            model=settings.kimi.model,
            messages=messages,
            temperature=1,
            response_format={"type": "json_object"},
        )
        content = json.loads(completion.choices[0].message.content)
        print(content)


if __name__ == "__main__":
    kimi = Kimi()
    image_path = os.path.abspath("screenshots/10Ronaldinho.png")
    with open(image_path, "rb") as f:
        image_data = f.read()

        image_url = f"data:image/{os.path.splitext(image_path)[1]};base64,{base64.b64encode(image_data).decode('utf-8')}"
        kimi.chat(
            [
                system_message(x_screenshot_extraction_prompt),
                user_message(
                    [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                            },
                        },
                        {
                            "type": "text",
                            "text": "这个 x 账号粉丝数是多少，使用数字表示。",
                        },
                    ]
                ),
            ]
        )
