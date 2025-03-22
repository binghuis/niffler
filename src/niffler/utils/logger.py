import os
import sys

from loguru import logger


class LogManager:
    def __init__(self, log_dir="logs"):
        self.logger = logger
        self._init_config(log_dir)

    def _init_config(self, log_dir):
        self.logger.remove()

        os.makedirs(log_dir, exist_ok=True)

        self.logger.add(
            sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level.icon}</level> | <cyan>{module}:{line}</cyan> - <level>{message}</level>",
            colorize=True,
        )

        self.logger.add(
            os.path.join(log_dir, "app_{time:YYYY-MM-DD}.log"),
            rotation="100 MB",
            retention="30 days",
            compression="zip",
            enqueue=True,
            encoding="utf-8",
        )


log = LogManager().logger
