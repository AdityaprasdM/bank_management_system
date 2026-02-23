class Authservice:
    def login(self, account, pin):
        if account.verify_pin(pin):
            return True
        raise Exception("Invalid PIN")
    
