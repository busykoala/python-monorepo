import requests
from log.logger import get_logger

logger = get_logger("bar")


def run() -> None:
    response = response = requests.get("https://httpbin.org/get", timeout=5)
    logger.info("Response status code: %s", response.status_code)

    logger.info("Hello from bar!")


if __name__ == "__main__":
    run()
