import logging

logging.basicConfig(
    level=logging.ERROR,
    format='[{asctime}] #{levelname:8} {filename}:'
           '{lineno} - {name} - {message}'
)
logging.error("fghj")



