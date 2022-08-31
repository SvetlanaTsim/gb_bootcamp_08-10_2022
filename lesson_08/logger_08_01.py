from datetime import datetime
import os
import fnmatch


class Logger:
    def __init__(self, path='.'):
        self.path = path
        self.file_path = f"{self.path}/log_{datetime.now().strftime('%d-%m-%y').replace('-', '.')}.txt"
        try:
            os.stat(self.path)
        except FileNotFoundError:
            os.mkdir(self.path)
        self.log_file = open(self.file_path, "w", encoding="UTF-8")
        self.log_file.close()
        self.last_note = None

    @staticmethod
    def __get_current_date():
        return datetime.now()

    def write_log(self, event):
        with open(self.file_path, "a", encoding='UTF-8') as f:
            self.last_note = f"[{self.__get_current_date().strftime('%H:%M:%S')}]" + ' ' + event
            f.write(self.last_note + '\n')

    def clear_log(self):
        open(self.file_path, "w").close()

    def get_logs(self):
        with open(self.file_path, 'r', encoding='UTF-8') as f:
            data = f.read()
            logs = data.split('\n')
            logs.remove('')
            logs_tuple = [(time, log) for time, log in [note.split() for note in logs]]
        return logs_tuple

    def get_last_event(self):
        return self.last_note

    def get_all_logs(self):
        dir_content = os.listdir(self.path)
        log_files = [file for file in dir_content if fnmatch.fnmatch(file, "log_??.??.??.txt")]
        return log_files


#a = Logger('./logs')
a = Logger()
print("Object created", a)
a.write_log('тралала')
a.write_log('трололо')
a.write_log('трилили')
print(a.get_logs())
#a.clear_log()
print(a.get_last_event())
print(a.get_all_logs())

c = Logger()
print("Object created", c)
