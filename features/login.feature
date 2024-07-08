Feature: Luma webshop login
  As a user
  I want to login to the Luma webshop
  So that I can access to my user account

  Background:
    Given I am on the Luma homepage
    And I navigate to the Customer Login page

  Scenario: Successful login
    When I fill in the login form with valid data
    And I click on login button
    Then I should get logged in

  Scenario: Unsuccesful Login without credentials
    When I dont enter anything into email and password fields
    And I click on Login button
    Then I should see required fields warning message and the login fails

  Scenario: Unsuccessful login with invalid credentials
    When I enter invalid credentials into email and password fields
    And I click on login button
    Then I should see invalid credentials warning message and the login fails