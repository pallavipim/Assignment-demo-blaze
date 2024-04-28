Selenium_Python_Behave_Bdd_Allure

This is a Web Automation Testing framework using:
Language: Python
Version : 3.11
Testing framework: BDD Cucumber
Automation tool: Selenium webdriver
Reporting: Allure


Installation Prerequisite:
Python
Pycharm
Allure
Selenium


Framework Structure

allure/results--> contains allure report files
feature --> contains cucumber feature files
environment.py --> contains Hooks methods
steps --> contains Step Definition files
PageObjects--> Contains Locator and methods
allure/reports--> HTML report is generated using behave html formatter
run_test.py-->contains the script that runs the tests, creates reports and handles the test environment



Automated Testing Setup Guide:
1. Download the Project folder

2. Add dependency libraries
    selenium
    behave
    behave-html-formatter

3. Command to execute test and generate report:
    python run_test.py      

   



