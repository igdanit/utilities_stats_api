from loguru import logger

logger.add("logs.json", format="{time} {level} {message}",
level="ERROR", rotation="1MB", compression="zip",
serialize=True)
