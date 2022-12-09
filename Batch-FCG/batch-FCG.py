from fame.core.module import PreprocessingModule, ModuleInitializationError
from subprocess import Popen, PIPE
#import subprocess
import os
import r2pipe

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
        #output=subprocess.run(["python3", path+"/Batch-FCG/model/detector.py", "--model", target], capture_output=True, text=True)
        cmd = ("python3", path+"/batch-FCG/model/detector.py", "--model", target)
        ai_detector_process = Popen(cmd, stdout=PIPE,stderr=PIPE)
        output = ai_detector_process.communicate()[0].decode('utf-8')
        

        self.log("info","scanning end")
        #if "[0]" in output:
        #    output="0"
        #elif "[1]" in output:
        #    output="1"
        #elif "BenignWare" in output:
        #    output = "BenignWare"
        #if "Malware" in output:
        #    output = "Malware"
        #else:
        #    output = "error"

        self.results['scan_data']=str(output)
        self.log("info", self.results['scan_data'])
        #return len(self.results["scan_data"]) > 0
        return True
