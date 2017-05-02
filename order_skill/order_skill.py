import echokit
from echokit import Response, PlainTextOutputSpeech, SimpleCard

# In the Lambda config, 'handler' would be
# set to ``order_skill.handler``
handler = echokit.handler

# Your skill ID, as provided in the Alexa dev portal
echokit.application_id = "your_app_id"


# All apps are required to handle three basic requests,
# which have their own decorators:
# * LaunchRequest:          @echokit.on_session_launch
# * SessionEndedRequest:    @echokit.on_session_ended
# * IntentRequest:          @echokit.on_intent('your_intent_name')

# Handles: LaunchRequest
@echokit.on_session_launch
def session_started(request):
    return echokit.tell("Welcome to Order Maker!")


# Handles: SessionEndedRequestf
# Can't respond, so this just logs the reason via print()
@echokit.on_session_ended
def session_ended(request):
    print(request.request.reason)


# Handles: IntentRequest
@echokit.on_intent('HoursIntent')
def hours_intent(request):
    return echokit.tell("We're open today from 5am to 8pm")


# Handles: IntentRequest
# This example is for an intent that handles a slot and keeps a
# session attribute. This would return output speech like: 'You ordered pizza'
@echokit.on_intent('OrderIntent')
@echokit.slot('menu_item')
def order_intent(request, menu_item):
    response_text = f'You ordered: {menu_item}.'
    return echokit.ask(response_text)\
        .simple_card(title="Order", content=response_text)\
        .session_attributes({'last_order': menu_item})


# Handles: IntentRequest (unimplemented intent)
# For example, if 'WeaveBasketIntent' is defined in your
# interaction model, but you haven't defined a handler
# for it with @echokit.on_intent('WeaveBasketIntent'),
# this will catch it. If you don't define your own here,
# by default echokit will return a "Sorry, I didn't
# understand your request" speech response.
@echokit.fallback
def unimplemented(request):
    return echokit.tell(f"Sorry, {request.request.intent.name} isn't "
                        f"implemented!")
