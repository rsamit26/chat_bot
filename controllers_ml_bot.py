from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging



# logging.basicConfig(level=logging.INFO)

bot = ChatBot('Terminal',
              storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
              logic_adapters=[
                  'chatterbot.logic.BestMatch',
                  'chatterbot.logic.MathematicalEvaluation',

              ],
              filters=[
                  'chatterbot.filters.RepetitiveResponseFilter'
              ],
              input_adapter='chatterbot.input.VariableInputTypeAdapter',
              output_adapter='chatterbot.output.OutputAdapter',
              database='chatterbot-database'
              )

# bot.set_trainer(ChatterBotCorpusTrainer)
#
# bot.train(
#     "chatterbot.corpus.english"
# )
#
#
#
# print('Type something to begin...')
#
# while True:
#     try:
#         bot_input = bot.get_response(None)
#
#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break