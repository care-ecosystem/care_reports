from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

PLUGIN_NAME = "care_reports"


class CareReportsConfig(AppConfig):
    name = PLUGIN_NAME
    verbose_name = _("Care Reports") 

    def ready(self):
        pass
        # import care_reports.signals  # noqa: F401
        # import care_reports.tasks    # noqa: F401

        # from care.security.permissions.base import PermissionController
        # from care_reports.security.permissions import ReportsPermissions

        # PermissionController.register_permission_handler(ReportsPermissions)

        # import care_reports.security.access  # noqa: F401