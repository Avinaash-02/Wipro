class Mobile:
    def __init__(self,model,storage):
        self.model = model
        self.storage = storage
    def display(self):
        return f"Model: {self.model}\n"f'Storage: {self.storage}'
