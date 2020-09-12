from Core.BrowserHelpers import BrowserHelpers
from PageFactory.HomePage.HomePage import HomePage


class Test_Homepage(BrowserHelpers):
    homepage = HomePage()

    def test_todomvc(self):
        self.navigate_to_url(self.BASE_URL)
        
        self.homepage.add_todo("Zakir")
        assert self.homepage.is_todo_added("Zakir")
