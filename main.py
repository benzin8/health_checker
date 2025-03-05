import sys
from ui.main_ui import Ui_MainWindow,QMainWindow,QApplication
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QThread,Signal

from services.net_check import net_check
from services.disk_check import disk_check
from services.file_check import file_check
from services.cpu_check import cpu_check
from services.serv_check import serv_check
from services.db_check import check_db_connection, check_db_operations

class Thread(QThread):
    update_signal = Signal(str, int)
    def __init__(self, task, page_index):
        super().__init__()
        self.task = task
        self.page_index = page_index

    def run(self):
        result = self.task()
        self.update_signal.emit(result, self.page_index)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_worker = None
        self.setup_conn()

    def setup_conn(self):
        self.net_btn.clicked.connect(lambda: self.start_test(net_check,0))
        self.disk_btn.clicked.connect(lambda: self.start_test(disk_check, 0))
        self.file_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.cpu_btn.clicked.connect(lambda: self.start_test(cpu_check, 0))
        self.serv_btn.clicked.connect(lambda: self.start_test(serv_check, 0))
        self.db_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.choose_file.clicked.connect(self.file_selection)
        self.check_db_btn.clicked.connect(self.db_selection_conn)
        self.check_db_oper_btn.clicked.connect(self.db_selection_oper)

    def file_selection(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose file",
            "",
            "Все файлы (*)"
        )
        if not file_path:
            return
        self.start_test(
            task=lambda:file_check(file_path, "664"),
            page_index=1
        )

    def db_selection_conn(self):
        db_user = self.user_line.text()
        db_pass = self.pass_line.text()

        self.start_test(
            task=lambda:check_db_connection(host="localhost", user=db_user, password=db_pass),
            page_index=2
        )

    def db_selection_oper(self):
        db_name = self.name_line.text()
        db_user = self.user_line.text()
        db_pass = self.pass_line.text()
        self.start_test(
            task=lambda: check_db_operations(host="localhost", user=db_user, password=db_pass, database_name=db_name),
            page_index=2
        )

    def start_test(self, task, page_index):
        self.stackedWidget.setCurrentIndex(page_index)

        if self.current_worker and self.current_worker.isRunning():
            self.current_worker.terminate()

        self.current_worker = Thread(task, page_index)
        self.current_worker.update_signal.connect(self.show_result)
        self.current_worker.start()

    def show_result(self, result, page_index):
        text_edit ={
            0: self.textEdit,
            1: self.textEdit_3,
            2: self.textEdit_2
        }.get(page_index, self.textEdit)

        text_edit.append(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())