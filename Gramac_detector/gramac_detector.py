from fame.core.module import PreprocessingModule, ModuleInitializationError
from subprocess import Popen, PIPE
import os

try:
    import r2pipe
    HAVE_R2PIPE = True
except ImportError:
    HAVE_R2PIPE = False

class Gramac_detector(PreprocessingModule):
    name = "Gramac_detector"

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

        self.results = {}
        path=os.path.dirname(os.path.abspath(__file__))
        self.log("info", "start scanning")
        cmd = ("python3", path+"/Gramac_detector/model/detector.py", "--target", target)
        ai_detector_process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output = ai_detector_process.communicate()[0].decode('utf-8')
        

        self.log("info","scanning end")
        if output == "":
            output = "error"

        stderr=ai_detector_process.communicate()[1].decode('utf-8')

        self.results['scan_data']=output
        self.log("info", self.results['scan_data'])
        self.log("info", stderr)
        
        return True
