Feature: Facebook Login
    Facebook Login testing

Scenario: Facebook Login
    Given the Zalora App has completed Country and Language selection
    When I login with Facebook
    Then I should see language selection page
