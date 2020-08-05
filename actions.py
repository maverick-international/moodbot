from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUttered, Restarted, FollowupAction

class ActionRestart(Action):
    """Resets the tracker to its initial state.
    Utters the restart response if available."""

    def name(self):
        return "action_restart"

    async def run(self, dispatcher, tracker, domain):
        return [Restarted(), FollowupAction("action_intro")]


class ActionIntroduction(Action):

    def name(self):
        return "action_intro"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        dispatcher.utter_message(template="utter_happy_or_sad_or_bot")
        return [FollowupAction("action_listen")]