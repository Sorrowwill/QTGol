from qtgol import __version__
from pytestqt.qtbot import QtBot
from qtgol.app import MyWidget
from PySide6 import QtCore


def test_version():
    assert __version__ == "0.1.0"


def test_hello(qtbot: QtBot):
    widget = MyWidget()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button, QtCore.Qt.LeftButton)

    assert widget.text.text() in ["Hallo Welt", "Привет мир"]
