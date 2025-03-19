import base64
import json
import os

from openai import OpenAI

from niffler.config import settings
from niffler.integrations.llm.message import system_message, user_message
from niffler.integrations.llm.prompts.kimi import x_screenshot_extraction_prompt


class Kimi:
    BASE_PATH = "screenshots"

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

    @staticmethod
    def image_to_base64_data_url(base_path, image_url):
        try:
            image_path = os.path.abspath(f"{base_path}/{image_url}")
            with open(image_path, "rb") as f:
                image_data = f.read()
                base64_data = base64.b64encode(image_data).decode("utf-8")
            image_extension = os.path.splitext(image_path)[1][1:]
            data_url = f"data:image/{image_extension};base64,{base64_data}"
            return data_url
        except FileNotFoundError:
            raise ValueError(f"图片文件不存在: {image_path}")
        except Exception as e:
            raise ValueError(f"处理图片时发生错误: {e}")

    def extract_screenshot(self, image_url):
        image_url = self.image_to_base64_data_url(self.BASE_PATH, image_url)
        messages = [
            system_message(x_screenshot_extraction_prompt),
            user_message(
                [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                    # {
                    #     "type": "text",
                    #     "text": "",
                    # },
                ]
            ),
        ]
        self.chat(messages)


if __name__ == "__main__":
    kimi = Kimi()
    kimi.extract_screenshot("10Ronaldinho.png")
