# pylint: disable=C,R,W
from flask import send_file
from flask_appbuilder import expose
from flask_appbuilder.security.decorators import has_access

from superset import app, appbuilder, thumbnail_cache
from superset.utils.selenium import DashboardScreenshot, SliceScreenshot
from .base import BaseSupersetView

config = app.config
NO_IMAGE_SRC = '/static/assets/images/no-image.png'


class Thumb(BaseSupersetView):
    """Base views for thumbnails"""
    @expose('/chart/<slice_id>/<sha>/')
    @has_access
    def chart(self, slice_id, sha=None):
        """Returns an thumbnail for a given chart, uses cache if possible"""
        # TODO SECURITY
        screenshot = SliceScreenshot(id=slice_id)
        # TODO handle no image
        img = screenshot.get_from_cache(thumbnail_cache)
        return send_file(img, mimetype='image/png')

    @expose('/dashboard/<dashboard_id>/<sha>/')
    @has_access
    def dashboard(self, dashboard_id, sha=None):
        """Returns an thumbnail for a given dash, uses cache if possible"""
        # TODO SECURITY
        screenshot = DashboardScreenshot(id=dashboard_id)
        img = screenshot.get_from_cache(thumbnail_cache)
        # TODO handle no image
        return send_file(img, mimetype='image/png')


appbuilder.add_view_no_menu(Thumb)
