Feature: Adding products to the shopping cart

  Scenario: Select the last product and add the product to the cart
    Given User on the product listing page
    When user clicks on next button until reaches the last page
    And clicks on the last product
    And user clicks on Add to Cart button
    Then user should display product added message


