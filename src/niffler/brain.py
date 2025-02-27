from openai import OpenAI

from niffler.config import get_settings

settings = get_settings()


class Brain:
    def __init__(self):
        client = OpenAI(
            api_key=settings.xai.api_key,
            base_url=settings.xai.base_url,
        )

        completion = client.chat.completions.create(
            model="grok-2-latest",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "你好"},
            ],
        )

        print(completion.choices[0].message)


if __name__ == "__main__":
    Brain()
