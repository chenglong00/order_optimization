import argparse
import logging

logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='enter path to config file', required=False)
    args = parser.parse_args()

    if args.config is None:
        # parser.print_help()
        logger.info("Config file path is not provided, default to default config ")
        return None
    else:
        config_path = args.config

    return config_path
