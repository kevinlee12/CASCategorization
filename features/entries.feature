Feature: New entry creation

  Scenario: User creates a new entry
  Given user is logged in
  When user creates a new entry
  Then entry is created
