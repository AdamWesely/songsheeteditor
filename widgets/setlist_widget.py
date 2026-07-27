from PySide6.QtWidgets import QListWidget


class SetlistWidget(QListWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.changed_callback = None

    def dropEvent(self, event):

        super().dropEvent(event)

        if self.changed_callback:
            self.changed_callback()