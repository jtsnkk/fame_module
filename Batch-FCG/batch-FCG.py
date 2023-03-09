from fame.core.module import PreprocessingModule, ModuleInitializationError
from subprocess import Popen, PIPE
import os

try:
    import r2pipe
    HAVE_R2PIPE = True
except ImportError:
    HAVE_R2PIPE = False

class Batch_FCG(PreprocessingModule):
    name = "Batch_FCG"

    description = "Get Scan Rrport from connlab."
    
    def initialize(self):
        if not HAVE_R2PIPE:
            raise ModuleInitializationError(self, "Missing dependency: r2pipe")

        return True

    def each_with_type(self, target, target_type):

        self.results = {}
        path=os.path.dirname(os.path.abspath(__file__))
        self.log("info", "start scanning")
        
        cmd = ("python3", path+"/Batch-FCG/model/detector.py", "--target", target)
        ai_detector_process = Popen(cmd, stdout=PIPE,stderr=PIPE)
        output = ai_detector_process.communicate()[0].decode('utf-8')
        
        if output == "":
            output = "error"

        self.log("info","scanning end")

        
        self.results['scan_data'] = output
        stderr=ai_detector_process.communicate()[1] 
        self.log("info", self.results['scan_data'])
        self.log("info", stderr.decode('utf-8'))

        return True
