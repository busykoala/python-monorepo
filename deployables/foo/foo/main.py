from log.logger import get_logger

logger = get_logger("foo")


def run_foo() -> None:
    logger.info("Hello from foo!")


if __name__ == "__main__":
    run_foo()
