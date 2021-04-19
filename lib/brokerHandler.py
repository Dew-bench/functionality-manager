
class brokerHandler:
    def __init__(self):
        self.BROKERS = {}
    
    def add_broker(self, broker):
        if "url" in broker :
            if "port" in broker :
                self.BROKERS[broker["url"]] = broker
    
    def remove_broker(self, broker):
        if pipe['url'] in self.BROKERS:
            del self.BROKERS[broker['url']]

    def list_brokers(self):
        return self.BROKERS

    def get_broker(self):
        if len(self.BROKERS.keys()) > 0:
            return self.BROKERS[list(self.BROKERS)[0]]
        else:
            return -1