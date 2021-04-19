# keep track of active services 

class serviceHandler:
    def __init__(self):
        self.SERVICES = {}
    
    def add_service(self, id, conf):
        if id in self.SERVICES:
            self.SERVICES[id].append(conf)
        else:
            self.SERVICES[id] = [conf]
    
    def get_service(self, id):
        if id in self.SERVICES:
            return self.SERVICES[id]
        else:
            return -1

    def list_service(self):
        return self.SERVICES