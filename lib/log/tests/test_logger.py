from log.logger import get_logger


def test_get_logger_returns_logger():
    logger = get_logger("test")
    assert logger.name == "test"
