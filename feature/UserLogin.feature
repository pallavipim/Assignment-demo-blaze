@order_2
Feature: User Login

  Scenario: Log in with valid username and valid password
    When User clicks on the Log in button
    And enters a valid username "Automate14" and valid password "Automate14" in LogIn window
    And click on log in button
    Then user should display Welcome username message


  Scenario: Log in with invalid username and invalid password
    When User clicks on the Log in button
    And enters a invalid username "Automate100" and invalid password "Automate100" in LogIn window
    And click on log in button
    Then User should display "user does not exist" message




