class UpdateEntity:
    def __init__(self, update_id, message):
        self.update_id = update_id
        self.message = message

    def __eq__(self, other):
        if not isinstance(other, UpdateEntity):
            return NotImplemented
        return self.update_id == other.update_id and \
               self.message == other.message


class MessageEntity:
    def __init__(self, message_id, date, chat, text):
        self.message_id = message_id
        self.date = date
        self.chat = chat
        self.text = text

    def __eq__(self, other):
        if not isinstance(other, MessageEntity):
            return NotImplemented
        return self.message_id == other.message_id and \
               self.date == other.date and \
               self.chat == other.chat and \
               self.text == other.text


class ChatEntity:
    def __init__(self, id, type, first_name, last_name, username):
        self.id = id
        self.type = type
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def __eq__(self, other):
        if not isinstance(other, ChatEntity):
            return NotImplemented
        return self.id == other.id and \
               self.type == other.type and \
               self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.username == other.username
