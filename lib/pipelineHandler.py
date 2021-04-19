# from yaml import load, dump

class pipelineHandler:
    def __init__(self, proxyH, serviceH):
        self.PIPES = {}
        self.DEVICES = {}
        self.PIPE_DEVICE = {}
        self.proxyH = proxyH
        self.serviceH = serviceH

    def add_pipe(self, pipe):
        if "name" in pipe and "pipeline" in pipe :
            self.PIPES[pipe["name"]] = pipe

            for pipeline in pipe["pipeline"]:
                if "dependency" in pipeline:
                    for dependency, name in pipeline["dependency"]:
                        if "type" in dependency:
                            if dependency["type"] == "device":
                                self.connect_device_with_pipe(pipe["name"], name)
                                self.deploy()
    
    def remove_pipe(self, pipe):
        if "name" in pipe :
            if pipe['name'] in self.PIPES:
                del self.PIPES[pipe['name']]
                self.deploy()

    def list_pipes(self):
        return self.PIPES

    def get_pipe(self, name):
        if name in self.PIPES:
            return self.PIPES[name]
        else :
            return -1

    def add_device(self, dtype, id, hostname):
        self.DEVICES[id] = {"type": dtype, "hostname": hostname}
        self.deploy()

    def remove_device(self, id):
        del self.DEVICES[id]
        self.deploy()

    def connect_device_with_pipe(self, pipe_name, device_name):
        if device_name in self.PIPE_DEVICE:
            self.PIPE_DEVICE[device_name].append(device_name)
        else:
            self.PIPE_DEVICE[device_name] = [device_name]
        
    def deploy(self):
        pass


pipe = {
    "name": 'eman',
    "pipeline" : [
        "UI":{
            "type": "depl", 
            "id": "depl-name",
            "dependency": [
                "DB":{
                    "type": "service",
                    "policy": "single" # single || multiple || number
                }
            ],
        },
        "DB":{
            "type": "service",
            "id": "db-service",
            "dependency" : [],
        },
        "Manager":{
            "type": "depl",
            "id": "manager",
            "dependency": [
                "DB":{
                    "type": "service",
                    "policy": "single" # single || multiple || number
                },
                "drone":{
                    "type": "device",
                    "policy": "multiple" # single || multiple || number
                }
            ],
        }
    ]
}