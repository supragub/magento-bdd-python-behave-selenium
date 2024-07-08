Feature: Luma webshop registration
  As a user
  I want to registrate to the Luma webshop
  So that I can access to my user account

  Background:
    Given I am on the Luma homepage without logged in
    And I navigate to the registration page

  Scenario: Create a new customer account succesfully
    When I fill in the registration form with valid data
    And I submit the registration form
    Then I should be registered successfully and redirected to My Account page

	Scenario: There is already an account with this email address
    When I fill in the registration form with already registered email address
    And I submit the registration form
    Then I should see a warning message and the registration fails

  Scenario: Create a new customer account with invalid email format
    When I fill in the registration form with invalid email format
    And I submit the registration form
    Then I should see invalid email format warning message and the registration fails

  Scenario Outline: Create a new customer account with invalid passwords
    When I fill in the registration form with invalid "<password>" or "<confirm_password>"
    And I submit the registration form
    Then I should see invalid password warning message and the registration fails
    Examples:
    | password | confirm_password |
    | 12345678 | 12345678         |
    | password | password         |
    | q1w2e3r4 | q1w2e3r4         |
    | Q1w2e3   | q1w2e3r4         |
    | Q1w2e3r4 | q1w2e3r4         |

