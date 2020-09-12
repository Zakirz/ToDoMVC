from Core.BrowserHelpers import BrowserHelpers
from PageFactory.HomePage.HomePage import HomePage


class Test_Homepage(BrowserHelpers):
    homepage = HomePage()

    def test_todomvc(self):
        self.navigate_to_url(self.BASE_URL)
        first_task = "Drink water every hour"

        # Add to-do is working
        self.homepage.add_todo(first_task)
        assert self.homepage.is_todo_present(first_task)

        # Marking an item as complete works.
        inactive_task_count = self.homepage.get_todo_count()
        assert inactive_task_count == "1"
        self.homepage.check_todo(first_task)
        assert self.homepage.is_todo_checked(first_task)
        assert self.homepage.get_todo_count() == "0"

        # Delete a to-do
        self.homepage.delete_todo(first_task)
        assert not self.homepage.is_todo_present(first_task)

        # Filtering a to-do is working
        active_task = "Active Todo"
        completed_task = "Completed Todo"
        self.homepage.add_todo(active_task)
        self.homepage.add_todo(completed_task)
        assert self.homepage.get_todo_count() == "2"
        self.homepage.check_todo(completed_task)

        self.homepage.click_active_filter()
        assert self.homepage.is_todo_present(active_task)
        assert not self.homepage.is_todo_checked(active_task)

        self.homepage.click_completed_filter()
        assert self.homepage.is_todo_present(completed_task)
        assert self.homepage.is_todo_checked(completed_task)
