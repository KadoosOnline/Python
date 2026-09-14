# print() is fine while learning, but a real program uses 'logging':
# every message has a level, a time stamp, and can be sent to a file.
import logging

logging.basicConfig(
    level=logging.DEBUG,                     # show everything from DEBUG upwards
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
    # filename='app.log',                    # uncomment to write into a file
)

logger = logging.getLogger(__name__)


def divide(a: float, b: float) -> float | None:
    logger.debug('divide(%s, %s) was called', a, b)
    try:
        result = a / b
    except ZeroDivisionError:
        # exception() also prints the traceback - perfect inside an except block
        logger.exception('division by zero')
        return None
    logger.info('the result is %s', result)
    return result


def main() -> None:
    logger.info('program started')
    divide(10, 2)
    divide(10, 0)
    logger.warning('this is a warning')
    logger.error('this is an error')
    logger.info('program finished')


if __name__ == '__main__':
    main()
