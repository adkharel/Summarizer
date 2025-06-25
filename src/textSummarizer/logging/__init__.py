import os
import sys
import logging

log_dir = 'logs'
logging_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_file = os.path.join(log_dir, 'continuouslogs.log')

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("SummarizerLogger")