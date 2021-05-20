Feature: Google Searching
  As a web surfer, I want to search Google, so that I can learn new things.
  
# noinspection CucumberUndefinedStep
  @automated @google @panda
  Scenario Outline: Simple Google searches
    Given a web browser is on the Google page
    When the search phrase <phrase> is entered
    And the button 'Поиск в Google' is clicked
    Then results for <phrase> are shown
    And the related results include <related>

    Examples: Animals
      | phrase   | related  |
      | panda    | panda    |
      | elephant | elephant |
