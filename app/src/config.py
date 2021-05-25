from loguru import logger
import sys

logger.add(sys.stdout, level="DEBUG")
logger.add(
    "./logs/log_file.log",
    rotation="1 day",
    level="DEBUG",
    retention="30 days",
    backtrace=True,
    diagnose=True,  
)