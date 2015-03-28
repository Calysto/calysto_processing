from IPython.kernel.zmq.kernelapp import IPKernelApp 
from .kernel import ProcessingKernel
IPKernelApp.launch_instance(kernel_class=ProcessingKernel) 
