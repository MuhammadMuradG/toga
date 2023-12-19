from pathlib import Path

import pytest

import toga_cocoa
from toga_cocoa.libs import NSImage

from .probe import BaseProbe


class IconProbe(BaseProbe):
    alternate_resource = "resources/icons/blue"

    def __init__(self, app, icon):
        super().__init__()
        self.app = app
        self.icon = icon
        assert isinstance(self.icon._impl.native, NSImage)

    def assert_icon_content(self, path):
        if path == "resources/icons/green":
            assert (
                self.icon._impl.path
                == self.app.paths.app / "resources/icons/green.icns"
            )
        elif path == "resources/icons/blue":
            assert (
                self.icon._impl.path == self.app.paths.app / "resources/icons/blue.png"
            )
        else:
            pytest.fail("Unknown icon resource")

    def assert_default_icon_content(self):
        assert (
            self.icon._impl.path
            == Path(toga_cocoa.__file__).parent / "resources/toga.icns"
        )

    def assert_platform_icon_content(self, platform):
        assert self.icon._impl.path == self.app.paths.app / f"resources/logo-{platform}.icns"
