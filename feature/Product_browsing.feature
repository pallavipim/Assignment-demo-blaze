Feature: Product browsing:

  Scenario: Verify that products are displayed correctly on the homepage
    Given the User is on the homepage
    When the User hovers over a product and captures its title and description
    Then the User verifies that the product description should contain the product title


  Scenario: Verify that product categories can be navigated successfully.
    Given the user is on the homepage
    Then User should display Categories on homepage
    And the list of Product Categories
    When the user click on a category from the list
    Then the user should be taken to the page displaying products in that category
    And user should display relevant products listed

