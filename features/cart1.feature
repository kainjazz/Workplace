
Feature: add to cart

  Scenario: Add some product to cart
    Given go to 220-volt.ru
    When navigate to some category
    Then perform some product
    Then close cart banner
    Then go to cart
    Then delete product from cart