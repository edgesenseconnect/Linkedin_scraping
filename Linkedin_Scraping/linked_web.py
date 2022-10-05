from linkedin_scraper import Person, actions
from selenium import webdriver
from getpass import getpass
chrome_driver = input("Enter chrome driver *.exe absolute path:")
linked_in_email = input("LinkedIn mail ID:")
linked_in_password = getpass(" Enter Password:")
linked_in_profile = input("Enter Profile URL:")
driver = webdriver.Chrome(chrome_driver)
actions.login(driver, linked_in_email, linked_in_password) # if email and password isnt given, it'll prompt in terminal
person = Person(linkedin_url=linked_in_profile, name=None, about=[], experiences=[], educations=[], interests=[], accomplishments=[], company=None, job_title=None, driver=driver, scrape=True)
print(person)
