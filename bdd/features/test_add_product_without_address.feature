Feature: Test add product without address

  Scenario: Test add product without address
    Given open main page
    When add product
    Then should be select_address_dialog
