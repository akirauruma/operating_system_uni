import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
import os


class FolderRenamer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Folder Renamer")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.selected_folder_label = QLabel("Selected Folder:")
        self.layout.addWidget(self.selected_folder_label)

        self.selected_folder_text = QLabel()
        self.layout.addWidget(self.selected_folder_text)

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_folder)
        self.layout.addWidget(self.browse_button)

        self.rename_button = QPushButton("Rename Folders")
        self.rename_button.clicked.connect(self.rename_folders)
        self.layout.addWidget(self.rename_button)

        self.selected_folder_path = ""

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.selected_folder_path = folder_path
            self.selected_folder_text.setText(folder_path)

    def rename_folders(self):
        if self.selected_folder_path:
            subdirectories = [os.path.join(self.selected_folder_path, name)
                              for name in os.listdir(self.selected_folder_path)
                              if os.path.isdir(os.path.join(self.selected_folder_path, name))]

            for dir_path in subdirectories:
                dir_name = os.path.basename(dir_path)
                name_parts = dir_name.split(' ')
                if len(name_parts) == 2:
                    new_name = name_parts[1] + " " + name_parts[0]
                    new_path = os.path.join(os.path.dirname(dir_path), new_name)
                    os.rename(dir_path, new_path)

            self.selected_folder_text.setText("Folders renamed successfully!")
        else:
            self.selected_folder_text.setText("Please select a folder.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderRenamer()
    window.show()
    sys.exit(app.exec())
