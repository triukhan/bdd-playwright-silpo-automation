Feature: Test card counter

  Scenario: Test card counter
    Given open main page with delivery
    When add product
    Then should be counter on selected_product
    When execute decrease on selected_product
    Then counter absent on selected_product

