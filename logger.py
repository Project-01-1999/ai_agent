import logging
from pathlib import Path


class AstraLogger:

    def __init__(self):

        log_folder = Path(__file__).parent.parent / "Logs"
        log_folder.mkdir(exist_ok=True)

        log_file = log_folder / "astra.log"

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.logger = logging.getLogger("Astra")

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)