Feature: Teacher App :: Create class
    As a teacher
    I want to create my class

    Scenario: Create class
        Given I was a logged in "TEACHER" user
        When I go to "teacher:class" page
        Then I should see the text "You did not setup any classes."
        And I should see the form "add_class"
        And I should see the form "add_class" fields:
            | name                  | type      |
            | Class                 | select    |
            | Hour salary minimum   | number    |
            | Hour salary maximum   | number    |
            | Days per week         | select    |
            | Hours per day         | select    |
            | Salary per 4 weeks    | text      |
            | Add                   | button    |
        And I should see the button "Add" in state "disabled"
        When I fill in the form "add_class" fields:
            | name                  | value     |
            | Class                 | 10        |
            | Hour salary minimum   | 50        |
            | Hour salary maximum   | 60        |
            | Days per week         | 3         |
            | Hours per day         | 1.5       |
        Then I should see the form "add_class" fields values:
            | name                  | value         |
            | Salary per 4 weeks    | 900 - 1080    |
        And I should see the button "Add" in state "ready"
        When I click on button "Add"
        Then I should see the button "Add" in state "working"
        When the button "Add" done "working"
        Then I should see the "classes" table has rows:
            | Class     | Hour salary   | Days per week | Hours per day     | Salary per 4 weeks    |
            | 10        | 50 - 60       | 3             | 1.5               | 900 - 1080            |
        And I should see the form "add_class" fields values:
            | name                  | value         |
            | Class                 |               |
            | Hour salary minimum   |               |
            | Hour salary maximum   |               |
            | Days per week         |               |
            | Hours per day         |               |
            | Salary per 4 weeks    |               |

    Scenario: Create class error
        Given I was a logged in "TEACHER" user
        When I go to "teacher:class" page
        And I fill in the form "add_class" fields:
            | name                  | value     |
            | Class                 |           |
            | Hour salary minimum   | 50        |
            | Hour salary maximum   | 60        |
            | Days per week         | 3         |
            | Hours per day         | 1.5       |
        Then I should see the error "You have to select the class."
        And I should see the button "Add" in state "disabled"
        When I fill in the form "add_class" fields:
            | name                  | value     |
            | Class                 | 10        |
            | Hour salary minimum   |           |
            | Hour salary maximum   | 60        |
            | Days per week         | 3         |
            | Hours per day         | 1.5       |
        Then I should see the error "You have to enter the Hour salary minimum salary per hour."
        And I should see the button "Add" in state "disabled"
        When I fill in the form "add_class" fields:
            | name                  | value     |
            | Class                 | 10        |
            | Hour salary minimum   | 50        |
            | Hour salary maximum   |           |
            | Days per week         | 3         |
            | Hours per day         | 1.5       |
        Then I should see the error "You have to enter the Hour salary maximum salary per hour."
        And I should see the button "Add" in state "disabled"
        When I fill in the form "add_class" fields:
            | name                  | value     |
            | Class                 | 10        |
            | Hour salary minimum   | 50        |
            | Hour salary maximum   | 40        |
            | Days per week         | 3         |
            | Hours per day         | 1.5       |
        Then I should see the error "Maximum salary per hour must higher than minimum salary per hour."
        And I should see the button "Add" in state "disabled"
        When I fill in the form "add_class" fields:
            | name                  | value     |
            | Class                 | 10        |
            | Hour salary minimum   | 50        |
            | Hour salary maximum   | 60        |
            | Days per week         |           |
            | Hours per day         | 1.5       |
        Then I should see the error "You have to select how many days per week for this class."
        And I should see the button "Add" in state "disabled"
        When I fill in the form "add_class" fields:
            | name                  | value     |
            | Class                 | 10        |
            | Hour salary minimum   | 50        |
            | Hour salary maximum   | 60        |
            | Days per week         | 3         |
            | Hours per day         |           |
        Then I should see the error "You have to enter how many hours per day for this class."
        And I should see the button "Add" in state "disabled"
