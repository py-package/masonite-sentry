import sentry_sdk
from masonite.configuration import config
import logging

from .loggers.SentryQueueLogger import SentryQueryLogger
from .listeners.SentryExceptionListener import SentryExceptionListener
from masonite.environment import env


class Sentry:
    def __init__(self, application) -> None:
        self.app = application
        self.sentry_config = config("sentry")

        # if not env("APP_DEBUG"):
        #     self.setup()
        self.setup()

    def setup(self):
        sentry_sdk.init(
            dsn=self.sentry_config.get("sentry_dsn"),
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=self.sentry_config.get("sentry_sample_rate"),
            before_breadcrumb=self.before_breadcrumb,
        )
        logger = logging.getLogger("masoniteorm.connection.queries")
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        logger.addHandler(SentryQueryLogger(logging.DEBUG))

        self.app.make("event").listen("masonite.exception.*", [SentryExceptionListener])

    def before_breadcrumb(self, crumb, hint=None):
        if crumb["category"] == "masoniteorm.models.hydrate":
            return None
        return crumb
