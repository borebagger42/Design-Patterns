class Notifier():
    def send(seelf, message):
        print(message)

class BaseDecorator():
    
    def __init__(self):
        self.wrapee = Notifier()
        
    
    def send(self, message):
        message = self.decorator(message)
        self.wrapee.send(message)
        
    def decorator(self, message):
        return("new message: " + message)
        
class SMSDecorator(BaseDecorator):
    def decorator(self, message):
        return("New text: " + message)
        

        
        
class FacebookDecorator(BaseDecorator):
    def decorator(self, message):
        return("New Facebook notification: " + message)

        
class SlackDecorator(BaseDecorator):
    def decorator(self, message):
        return("New Slack message: " + message)
  
  
  
facebook = FacebookDecorator()
FacebookDecorator.send(facebook,"Hello world")