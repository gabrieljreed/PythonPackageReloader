import sys
from unittest import mock
from unittest.mock import MagicMock, patch

from unload_packages import unload


def test_unload():
    mocked_module_1 = MagicMock()
    mocked_module_2 = MagicMock()
    mocked_module_3 = MagicMock()
    with patch.dict(
        "sys.modules",
        {"mocked_module_1": mocked_module_1, "mocked_module_2": mocked_module_2, "another_module": mocked_module_3},
    ):
        assert "mocked_module_1" in sys.modules
        assert "mocked_module_2" in sys.modules
        assert "another_module" in sys.modules

        unload(packages=["mocked_module"])

        assert "mocked_module_1" not in sys.modules
        assert "mocked_module_2" not in sys.modules
        assert "another_module" in sys.modules


def test_unload_verbose(capsys):
    mocked_module_1 = MagicMock()
    mocked_module_2 = MagicMock()
    mocked_module_3 = MagicMock()
    with patch.dict(
        "sys.modules",
        {"mocked_module_1": mocked_module_1, "mocked_module_2": mocked_module_2, "another_module": mocked_module_3},
    ):
        assert "mocked_module_1" in sys.modules
        assert "mocked_module_2" in sys.modules
        assert "another_module" in sys.modules

        unload(packages=["mocked_module"], verbose=True)

        assert "mocked_module_1" not in sys.modules
        assert "mocked_module_2" not in sys.modules
        assert "another_module" in sys.modules

        captured = capsys.readouterr()

        assert "Unloaded: mocked_module_1" in captured.out
        assert "Error unloading mocked_module_1: " not in captured.out
        assert "Unloaded: mocked_module_2" in captured.out
        assert "Error unloading mocked_module_2: " not in captured.out
        assert "Unloaded: another_module" not in captured.out


@mock.patch("unload_packages.DEFAULT_RELOAD_PACKAGES", ["mocked_module"])
def test_unload_default_packages():
    mocked_module_1 = MagicMock()
    mocked_module_2 = MagicMock()
    mocked_module_3 = MagicMock()
    with patch.dict(
        "sys.modules",
        {"mocked_module_1": mocked_module_1, "mocked_module_2": mocked_module_2, "another_module": mocked_module_3},
    ):
        assert "mocked_module_1" in sys.modules
        assert "mocked_module_2" in sys.modules
        assert "another_module" in sys.modules

        unload()

        assert "mocked_module_1" not in sys.modules
        assert "mocked_module_2" not in sys.modules
        assert "another_module" in sys.modules


def test_unload_exception_handling():
    # Mock sys.modules to include a module that cannot be deleted
    with patch.dict("sys.modules", {"mocked_module": None}):
        unload(packages=["mocked_module"], verbose=True)
