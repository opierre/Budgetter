import sys
import traceback
from typing import Callable

from PySide6.QtCore import QRunnable, Signal, QObject


class WorkerSignals(QObject):
    """
    Custom signals for runnable
    """

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)


class Worker(QRunnable):
    """
    Worker class to handle threaded calls
    """

    def __init__(self, func: Callable, *args, **kwargs):
        super().__init__()

        # Store arguments
        self.func = func
        self.args = args
        self.kwargs = kwargs

        # Store signals
        self.signals = WorkerSignals()

    def run(self) -> None:
        """
        Override run function with custom

        :return: None
        """

        try:
            # Call function
            result = self.func(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exc_type, value = sys.exc_info()[:2]
            self.signals.error.emit((exc_type, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
