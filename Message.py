class Message():
    """:argument: key : message key publish to topic
                  value: A value of type string or json or list ..."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "key: " + self.key + " " + "value: " + self.value
