import os
from config_module.config_singleton import ConfigSingleton
from utils_module.logger import LoggerSingleton

def init_config_and_logger(local_config_host: str, local_config_port: int, local_app_id: str) \
        -> tuple[ConfigSingleton, LoggerSingleton]:
    config_host = os.environ.get('CONFIG_HOST', local_config_host)
    config_port = int(os.environ.get('CONFIG_PORT', local_config_port))
    app_id = os.environ.get('APP_ID', local_app_id)

    config = ConfigSingleton()
    config.load_config(host=config_host, port=config_port, app_id=app_id)

    app_config = config.get_value('app')

    log_level = os.environ.get('LOG_LEVEL', 'DEBUG')
    logger = LoggerSingleton.get_logger(f'{app_config["name"]}.main', level=log_level)

    return config, logger
