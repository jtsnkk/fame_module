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

class Opcode_detector(PreprocessingModule):
    name = "Opcode_detector"

    description = "Get Scan Rrport from connlab."
    
    def initialize(self):
        if not HAVE_R2PIPE:
            raise ModuleInitializationError(self, "Missing dependency: r2pipe")

        return True

    def each_with_type(self, target, target_type):

        self.results = {}
        path=os.path.dirname(os.path.abspath(__file__))
        self.log("info", "start scanning")
        #output=subprocess.run(["python3", path+"/ReinterpretedFCG/model/detector.py", "--model", target], capture_output=True, text=True)
        cmd = ("python3", path+"/Opcode_detector/model/detector.py", "--model", target)
        ai_detector_process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output = ai_detector_process.communicate()[0].decode('utf-8')
        

        self.log("info","scanning end")
        if "Malware" in output:
            output = "Malware"
        elif "BenignWare" in output:
            output = "BenignWare"
        else:
            output = "error"
    
        stderr=ai_detector_process.communicate()[1].decode('utf-8')

        self.results['scan_data']=str(output)
        self.log("info", self.results['scan_data'])
        self.log("info", stderr)
        return True
