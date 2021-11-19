import time

from clearcut import get_logger, log_block

logger = get_logger(__name__)

if __name__ == "__main__":
    logger.info("This is an info level log")

    logger.debug("This is a debug level log")

    with log_block("This is an default (debug) log block", logger):
        time.sleep(1)

    with log_block("This is an info log block", logger, debug=False):
        time.sleep(1)
