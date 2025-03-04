from typing import List


def user_message(content: str | List):
    return {
        "role": "user",
        "content": content,
    }


def system_message(content: str):
    return {
        "role": "system",
        "content": content,
    }
