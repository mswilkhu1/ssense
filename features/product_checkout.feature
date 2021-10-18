Feature: User is able to order product online and see confirmation
  As a user I would like to order a product online and get the confirmation

  Scenario Outline: Ordering product on SwagLabs and getting confirmation
    Given user is logged in on SwagLabs
    When  user add to cart this <product> with <price>
    And   user navigates to cart
    And   clicks on checkout button <product> <price>
    And   enter checkout information
    And   click continue
    And   click finish <product> <price>
    Then  confirmation should be displayed <price>
    Examples:
      | product                        | price |
      | Sauce Labs Fleece Jacket       | 49.99 |
