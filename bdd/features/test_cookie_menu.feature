Feature: Test cookie menu

  Scenario: Test cookie menu
    Given open main page
    When should be cookie banner
    When click accept_cookie
    Then cookie_banner should be absent
