Feature: Test add product

  Scenario: Test add product
    Given open main page with delivery
    When add product
    Then cart counter should be 1

