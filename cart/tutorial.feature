
Feature: Личный кабинет
  @slow
  Scenario: Вход в личный кабинет
    Given открыта страница "http://220-volt.ru"
    When нажать ссылку "Вход"
    Then появится форма входа
    When ввести емейл "ci-test-user@220-volt.ru"
     And ввести пароль "password"
     And нажать кнопку "Войти"
    Then откроется страница со ссылкой "Перейти в личный кабинет"

   Scenario: nav in lk
     When in lk
     Then press contacts
     Then press favorite
     Then press gift
     Then press hammer

