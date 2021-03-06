import logging
import logging.config

def main():
    logging.basicConfig(
        filename='app.log',
        level=logging.WARNING,
        format='%(levelname)s:%(asctime)s:%(message)s')
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode = %r', filename, mode)
    logging.debug('Got here')

def main():
    # Configure the logging system
    logging.config.fileConfig('logconfig.ini')

if __name__ == '__main__':
    main()