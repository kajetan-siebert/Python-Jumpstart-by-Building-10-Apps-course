class EmptyTextError(Exception):
    def __init__(self,message="Text cannot be empty"):
        self.message = message.strip()
        super().__init__(self.message)