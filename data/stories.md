## happy path
* greet
  - action_intro
* mood_great
  - utter_happy
* goodbye
  - utter_goodbye

## happy path - bot challenge
* greet
  - action_intro
* bot_challenge
  - utter_iamabot
  - utter_happy_or_sad
* mood_great
  - utter_happy
* goodbye
  - utter_goodbye

## sad path 1
* greet
  - action_intro
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* goodbye
  - utter_goodbye

## sad path 1 - bot challenge
* greet
  - action_intro
* bot_challenge
  - utter_iamabot
  - utter_happy_or_sad
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* goodbye
  - utter_goodbye

## sad path 2
* greet
  - action_intro
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

  ## sad path 2 - bot challenge
* greet
  - action_intro
* bot_challenge
  - utter_iamabot
  - utter_happy_or_sad
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

<!-- Stories for after a conversation restart -->

## happy path
  - action_intro
* mood_great
  - utter_happy
* goodbye
  - utter_goodbye

## happy path - bot challenge
  - action_intro
* bot_challenge
  - utter_iamabot
  - utter_happy_or_sad
* mood_great
  - utter_happy
* goodbye
  - utter_goodbye

## sad path 1
  - action_intro
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* goodbye
  - utter_goodbye

## sad path 1 - bot challenge
  - action_intro
* bot_challenge
  - utter_iamabot
  - utter_happy_or_sad
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* goodbye
  - utter_goodbye

## sad path 2
  - action_intro
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## sad path 2 - bot challenge
  - action_intro
* bot_challenge
  - utter_iamabot
  - utter_happy_or_sad
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye