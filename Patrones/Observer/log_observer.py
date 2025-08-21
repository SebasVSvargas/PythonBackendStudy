from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, subject) -> None:
        pass

class Subject(ABC):

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


class LogSubject(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = ""

    @property
    def state(self) -> str:
        return self._state
    
    @state.setter
    def state(self, value: str) -> None:
        self._state = value
        self.notify()

# La siguiente puede ser una implementación alternativa
    # def set_state(self, state: str) -> None:
    #     self._state = state
    #     self.notify()

    # def get_state(self) -> str:
    #     return self._state

class FileObserver(Observer):
    def __init__(self, file_path):
        self.file_path = file_path

    def update(self, subject: LogSubject) -> None:
        with open(self.file_path, "a") as log_file:
            log_file.write(f"File updated: {subject.state}\n")

class ConsoleObserver(Observer):
    def update(self, subject: LogSubject) -> None:
        print(f"Console updated: {subject.state}")

#implementacion

file_observer = FileObserver("log.txt")
console_observer = ConsoleObserver()

log_subject = LogSubject()
log_subject.attach(file_observer)
log_subject.attach(console_observer)

log_subject.state = "First log entry"
log_subject.state = "Second log entry"

log_subject.detach(console_observer)
log_subject.state = "Third log entry"