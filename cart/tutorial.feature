
Feature: login profile
  @slow
  Scenario: запустить простой тест
    Given open 'http://220-volt.ru'
    When press "login"
    Then open login form
    Then input login
    Then input pass
#    Then press Enter
    Then go to LK
    Then Are u in LK

   Scenario: nav in lk
     When in lk
     Then press contacts
     Then press favorite
     Then press gift
     Then press hammer

