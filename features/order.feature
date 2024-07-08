Feature: Luma webshop order
  As a logged in user
  I would like to order on the Luma webshop

  Scenario: Successful order with Discount
    Given I am on the Luma homepage
    And I login to my user account
    When I select the first product from Hot Sellers
    Then I add to cart a size XS and color blue product
    Then I apply a Discount Code in the Shopping cart
    Then I click Proceed to Checkout button in the Shopping cart
    Then I confirm the Shipping and Payments details for my order