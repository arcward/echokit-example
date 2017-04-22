==============
echopy-example
==============
A sample Alexa skill using echopy_ (https://github.com/arcward/echopy)

==========
Setting up
==========
Lambda
------
Set up your Lambda function as described in the `official docs`_, with the
following exceptions:
 - At the **Select blueprint** screen, choose **Python 3.6** as the runtime, then
   choose **Blank Function**
 - In the **Configure function** section, set:
 
   + Runtime: **Python 3.6**
   + Handler: ``order_skill.handler``

Alexa
-----
See the `official docs`_ for a more comprehensive guide.

After setting your skill name/invocation name, copy the application ID. Then,
open ``echopy-example/order_skill/order_skill.py`` and set
``echopy.application_id`` as your own app ID.

Interaction model
^^^^^^^^^^^^^^^^^
See ``echopy-example/interaction_model/``

**Intent schema**::

    {
  "intents": [
    {
      "intent": "OrderIntent",
      "slots": [
        {
          "name": "MenuItem",
          "type": "MENU_ITEM"
        }
      ]
    },
    {
      "intent": "HoursIntent"
    },
    {
      "intent": "CancelIntent"
    }
  ]

**Utterances**::

    HoursIntent what are your hours
    OrderIntent I'll have {MenuItem}
    CancelIntent cancel my order

Custom slots types
~~~~~~~~~~~~~~~~~~
Add a custom slot type ``MENU_ITEM``, with whatever values you'd like.


Creating the Lambda deployment ZIP
----------------------------------
After installing echopy_, in the command line, from
the ``echopy-example/`` directory, run ``echodist --dir order_skill``. For
example, if you cloned this repo in your home directory:

.. code-block:: bash

    ~/echopy-example $ echodist --dir order_skill/

You can then upload the resulting ``order_skill.zip`` file via the Lambda
console and test your skill from there or the `Alexa dev portal`_!

.. _echopy: https://github.com/arcward/echopy
.. _`official docs`: https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function#creating-a-lambda-function-for-an-alexa-skill

.. _`Alexa dev portal`: https://developer.amazon.com/edw/home.html#/
