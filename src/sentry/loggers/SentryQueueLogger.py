import logging


class SentryQueryLogger(logging.Handler):
    def __init__(self, level=logging.DEBUG):
        super().__init__(level)

    def handle(self, log):
        from sentry_sdk import add_breadcrumb

        add_breadcrumb(
            category="query",
            message=log.msg,
            level="info",
            data={
                "time": f"{log.query_time}ms",
                "query_time": log.query_time,
                "query": log.query,
                "bindings": log.bindings,
                "level": log.levelname,
                "name": log.name,
            },
        )
