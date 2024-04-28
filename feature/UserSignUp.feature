Feature: User SignUp

#Positive Scenario
  Scenario: Signup with valid details
    When User clicks on the Sign Up button
    And enters a valid username "automate54" and valid password "automate"
    And click on sign-up button
    Then It should display confirmation message


#Negative Scenario
  Scenario: Signup with already registered username
    When User clicks on the Sign Up button
    And enters a already registered username "automate1" and password "automate1"
    And click on sign-up button
    Then It should display user already exist message






