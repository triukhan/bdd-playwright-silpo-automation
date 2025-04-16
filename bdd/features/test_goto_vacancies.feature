Feature: Test cookie menu

  Scenario: Test cookie menu
    Given open main page
    When click burger_button
    When click vacancies_link
    Then opened vacancies page
    Then should be vacancies_banner
    Then should be header elements
    When click logo
    Then opened main page
    Then should be main_banner
