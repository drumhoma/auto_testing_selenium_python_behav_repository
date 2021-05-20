# Укажем что это за фича
Feature: Checking search
  # Укажем имя сценария (в одной фиче может быть несколько)
  # noinspection CucumberUndefinedStep
  Scenario: Check some text in search results
    # И используем шаги
    Given website 'https://ya.ru'
    When search text 'Тест'
    And push button with text 'Найти'
    Then page include text 'НеТест'
