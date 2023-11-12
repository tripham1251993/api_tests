@auth_test
Feature: Test Authentication
  Test Authentication

  @C000001
  Scenario Outline: Login successfully with valid credential
    When User call auth api with credential "<credential>"
    Then Response code should be "<response_code>"
    And Response time should less than "<response_time>"s
    And Response should match schema "<schema>"
    Examples:
      | credential | response_code | response_time | schema          |
      | WEB3AUTH   | 200           | 1.5           | auth_login_resp |
