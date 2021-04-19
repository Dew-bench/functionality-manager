
class deplHandler:
    def __init__(self):
        self.DEPLOYMENTS = {}

    def add_depl(self, depl):
        if "name" in depl :
            self.DEPLOYMENTS[depl["name"]] = depl
    
    def remove_depl(self, depl):
        if depl['name'] in self.DEPLOYMENTS:
            del self.DEPLOYMENTS[depl['name']]

    def list_depl(self):
        return self.DEPLOYMENTS

    def get_depl(self, name):
        if name in self.DEPLOYMENTS:
            return self.DEPLOYMENTS[name]
        else :
            return -1 