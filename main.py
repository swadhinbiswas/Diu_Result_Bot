from logging import DEBUG, getLogger, StreamHandler, Formatter, FileHandler,WARNING,ERROR,CRITICAL,INFO,basicConfig
from colorama import Fore, Back, Style
from Bot.resultBot import Bot

basicConfig(format=Back.GREEN+'%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
              
              level=INFO)
  
  

logger = getLogger(__name__)



app=Bot.app


if __name__=="__main__":
  logger.info("Bot is running")
  app.run()
  
