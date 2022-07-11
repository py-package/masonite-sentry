"""A sentryProvider Service Provider."""

from masonite.packages import PackageProvider

from ..Sentry import Sentry


class SentryProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (self.root("sentry").name("sentry").config("config/sentry.py", publish=True))

    def register(self):
        super().register()
        self.application.bind("sentry", Sentry(application=self.application))

    def boot(self):
        """Boots services required by the container."""
        pass
