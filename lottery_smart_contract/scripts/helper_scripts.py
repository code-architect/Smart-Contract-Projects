import logging
import os

class SimpleLogger:
  """
  A simple logging library to write messages to a file.
  """

  def __init__(self, filename="logfile.log", level=logging.INFO):
    """
    Initializes the logger with a filename and logging level.

    Args:
      filename (str, optional): The filename for the log file. Defaults to "logfile.log".
      level (int, optional): The logging level. Defaults to logging.INFO.
    """
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(level)

    # Create log file if it doesn't exist
    if not os.path.exists(filename):
      with open(filename, 'w') as f:
        pass

    # Configure logging to write to the file
    file_handler = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_handler.setFormatter(formatter)
    self.logger.addHandler(file_handler)

  def debug(self, message):
    """Logs a debug message."""
    self.logger.debug(message)

  def info(self, message):
    """Logs an informational message."""
    self.logger.info(message)

  def warning(self, message):
    """Logs a warning message."""
    self.logger.warning(message)

  def error(self, message):
    """Logs an error message."""
    self.logger.error(message)

  def critical(self, message):
    """Logs a critical message."""
    self.logger.critical(message)

# Example usage
logger = SimpleLogger()  # Create a logger object (default settings)

logger.debug("This is a debug message.")
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

# Example usage with custom filename and level
custom_logger = SimpleLogger(filename="custom_log.log", level=logging.DEBUG)
custom_logger.info("This is a message logged with custom settings.")
