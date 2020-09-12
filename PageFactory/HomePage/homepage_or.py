# TODOMVC locators
todo_app = "Todo MVC App#Xpath=//section[contains(@class,'todoapp')]"
add_new_todo = "New Todo Tasks#Xpath=//form/input[contains(@class,'new-todo')]"
number_of_tasks = "Todo Tasks#Xpath=//ul[@class='todo-list']/li"
task_count = "Remaining Task Count#Xpath=//span[@class='todo-count']/strong"
todo_tasks = "Todo Task#Xpath=//ul[@class='todo-list']/li//label"

# INDIVIUAL TASK OPTIONS
check_task = "check Todo Task#Xpath=//ul[@class='todo-list']/li//label[text()='TASK_PLACEHOLDER']/parent::div/input"
select_task = "Select Todo Task#Xpath=//ul[@class='todo-list']/li//label[text()='TASK_PLACEHOLDER']"
delete_task = "Delete Todo Task#Xpath=//ul[@class='todo-list']/li//label[text()='TASK_PLACEHOLDER']/parent::div/button"

# TASK FILTERS
filter_active = "Active Filter#Xpath=//ul[@class='filters']/li/a[text()='Active']"
filter_all = "All Filter#Xpath=//ul[@class='filters']/li/a[text()='All']"
filter_completed = "Completed Filter#Xpath=//ul[@class='filters']/li/a[text()='Completed']"

clear_completed_btn = "clear completed button#Xpath=//button[text() = 'Clear completed']"
