from Core.BrowserHelpers import BrowserHelpers
from . import homepage_or
from selenium.webdriver.common.keys import Keys


class HomePage(BrowserHelpers):
    def __init__(self):
        self.obj = homepage_or

    def add_todo(self, todo):
        self.enter_text(self.obj.add_new_todo, todo)
        self.enter_text(self.obj.add_new_todo, Keys.ENTER)
        self.wait_time(2)

    def is_todo_added(self, todo):
        todo_locator = self.obj.select_task.replace("TASK_PLACEHOLDER", todo)
        return self.is_element_present(todo_locator)
