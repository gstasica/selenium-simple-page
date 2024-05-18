from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

# keeps chrome open
edge_options = webdriver.EdgeOptions()
# edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

# Closes Edge Browser
# driver.quit()
driver.close()

