import torch
print("Is CUDA available?", torch.cuda.is_available())
print("GPU name:", torch.cuda.get_device_name(0))

"""
check CPU details with nvidia-smi
nvidia-smi 
"""