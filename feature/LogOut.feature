Feature: User LogOut

  Scenario: Logout Process
    Given User clicks on the Log in button
    And enters a valid username "Automate1" and valid password "Automate1" in LogIn window
    And click on log in button
    When User click on Logout button
    Then user should display Log in button