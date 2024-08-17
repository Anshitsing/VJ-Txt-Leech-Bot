import telegram
from telegram import Update
from telegram.ext import Handler

admin_ids = [123456, 456789, 1231515]

class AdminHandler(Handler):
    def __init__(self):
        super().__init__(self.cb)

    def cb(self, update: telegram.Update, context):
        update.message.reply_text('Unauthorized access')

    def check_update(self, update: telegram.update.Update):
        if update.message is None or update.message.from_user.id not in admin_ids:
            return True

        return False
