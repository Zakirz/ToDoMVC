from Core.BrowserHelpers import BrowserHelpers
from . import homepage_or
from selenium.webdriver.common.keys import Keys
import time


class HomePage(BrowserHelpers):
    def __init__(self):
        self.obj = homepage_or

    def add_todo(self, todo):
        self.enter_text(self.obj.add_new_todo, todo)
        self.enter_key(self.obj.add_new_todo, Keys.ENTER)
        self.wait_time(2)

    def is_todo_present(self, todo):
        todo_locator = self.obj.select_task.replace("TASK_PLACEHOLDER", todo)
        return self.is_element_present(todo_locator)

    def check_todo(self, todo):
        todo_locator = self.obj.check_task.replace("TASK_PLACEHOLDER", todo)
        self.click_on(todo_locator)

    def is_todo_checked(self, todo):
        todo_locator = self.obj.checked_task.replace("TASK_PLACEHOLDER", todo)
        return self.is_element_present(todo_locator)

    def get_todo_count(self):
        return self.get_text(self.obj.task_count)

    def delete_todo(self, todo):
        todo_locator = self.obj.select_task.replace("TASK_PLACEHOLDER", todo)
        todo_remove_locator = self.obj.delete_task.replace(
            "TASK_PLACEHOLDER", todo)
        self.mouse_hover(todo_locator)
        time.sleep(1)
        self.click_on(todo_remove_locator)

    def click_active_filter(self):
        self.click_on(self.obj.filter_active)

    def click_completed_filter(self):
        self.click_on(self.obj.filter_completed)
