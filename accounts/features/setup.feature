Feature: Accounts App :: Setup account
    As a new user
    I want to setup my account on created

    Scenario: Account first setup
        Given I was a registered in user
        When I first login into my account
        Then I should see the setup account form
        And I should see the text "You are..."
        And I should see the text "Teacher"
        And I should see the text "Looking for students"
        And I should see the text "Parent"
        And I should see the text "Looking for teachers"

    Scenario: Teacher setup
        Given I was a registered in user
        When I first login into my account
        And I click on link "Teacher"
        Then my account should be set to "TEACHER" type

    Scenario: Parent setup
        Given I was a registered in user
        When I first login into my account
        And I click on link "Parent"
        Then my account should be set to "PARENT" type
