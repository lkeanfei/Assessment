Feature: Order Transaction
    Order Transaction testing

Scenario: Order Transaction
    Given that Country and Language Selection has completed
    When I select and add product to cart
    Then I should be able to checkout successfully
