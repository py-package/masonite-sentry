from masonite.environment import env
import sentry_sdk


class SentryExceptionListener:
    def handle(self, event, exception):
        from wsgi import application

        request = application.make("request")
        sentry_sdk.set_context(
            "Request",
            {
                "path": request.get_path_with_query(),
                "params": request.params,
            },
        )

        sentry_sdk.set_tag("environment", env("APP_ENV", "not set"))
        sentry_sdk.set_context("WSGI Environment", request.environ)

        if request.user():
            sentry_sdk.set_user({"id": request.user().id, "email": request.user().email})
        sentry_sdk.capture_exception(exception)
