import boto3
import os
import logging
import pprint

def set_logger(log_level:str = "INFO")->object:
    log_level = os.environ.get("LOG_LEVEL", log_level).strip().upper()
    logging.basicConfig(
        format="[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    return logger

logger = set_logger()

def set_pretty_printer():
    return pprint.PrettyPrinter(indent=2)


def _is_env_var_set(env_var: str) -> bool:
    return env_var in os.environ and os.environ[env_var] not in (
        "",
        "0",
        "false",
        "False",
    )


def get_from_secretstore_or_env(key: str, region_name:str) -> str:
    if _is_env_var_set(key):
        logger.warning(
            f"getting value for {key} from environment var; recommended to use AWS Secrets Manager instead"
        )
        return os.environ[key]

    session = boto3.session.Session()
    secrets_manager = session.client(
        service_name="secretsmanager", region_name=region_name
    )
    try:
        secret_value = secrets_manager.get_secret_value(SecretId=key)
    except Exception as e:
        logger.error(f"could not get secret {key} from secrets manager: {e}")
        raise e

    secret: str = secret_value["SecretString"]

    return secret

