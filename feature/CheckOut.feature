Feature:Checkout process:
  Scenario: Positive scenario: Successfully check the items added to the cart.
    Given User click on the desired product
    And add product to cart by clicking on button Add to cart
    When user click on Cart menu
    Then selected product should be displayed in the product list


  Scenario Outline: Negative scenario: Attempt to checkout without adding any products to the cart.
    Given User is on Home Page
    When User navigates to cart page
    Then Cart page should be empty
    When User clicks on place order button
    And  provide checkout details: "<name>","<country>","<city>","<CC>","<month>","<year>" and click on purchase button
    Then user should see message as unable to checkout with empty cart

    Examples: Checkout Details
      | name | country | city | CC | month | year |
      | John  | India  |Pune  |9898969574757124| March|2025|