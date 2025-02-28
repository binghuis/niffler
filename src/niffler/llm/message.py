def user_message(content: str):
    return {
        "role": "user",
        "content": content,
    }


def system_message(content: str):
    return {
        "role": "system",
        "content": content,
    }
