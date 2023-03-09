from fame.core.module import ProcessingModule, ModuleInitializationError
from subprocess import Popen, PIPE
import os

try:
    import r2pipe
    HAVE_R2PIPE = True
except ImportError:
    HAVE_R2PIPE = False

class aiDetector(ProcessingModule):
    name = "ai-detector"

    description = "Get Scan Rrport from connlab."
    config = [
        {
            "name": "size",
            "type": "integer",
            "description": "MAX bytes size for analysis"
        }
    ]
    
    def initialize(self):
        if not HAVE_R2PIPE:
            raise ModuleInitializationError(self, "Missing dependency: r2pipe")

        return True

    def each_with_type(self, target, target_type):
        
        file_size=os.path.getsize(target)
        if file_size > self.size:
            self.log("debug", "file size cannot exceed max bytes")
            return False

        self.results = {}
        path=os.path.dirname(os.path.abspath(__file__))
        
        self.log("info", "start scanning")
        
        cmd = ("python3",path+"/detection/graphity_detection/graphity_script.py", "-i", target)
        ai_detector_process = Popen(cmd, stdout=PIPE,stderr=PIPE)
        
        output = ai_detector_process.communicate()[0].decode('utf-8')
        self.log("info","scanning end")
        if output == "":
            output = "error"

        self.results['scan_data'] = output
        stderr=ai_detector_process.communicate()[1] 
        self.log("info", self.results['scan_data'])
        self.log("info", stderr.decode('utf-8'))
        return True
