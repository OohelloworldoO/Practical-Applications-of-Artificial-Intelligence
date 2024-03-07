import torch

# return evenly spaced values within a given interval
range_arr_torch = torch.arange(10)
print("An array given range is \n", range_arr_torch, "with dimensions ", range_arr_torch.shape, "\n")

# return evenly spaced numbers over a specified interval
linspace_arr_torch = torch.linspace(2.0, 3.0, steps=5)
print("An evenly spaced array given range is \n", linspace_arr_torch, " with dimensions ", linspace_arr_torch.shape, "\n")

# Tensor with uniform distribution between 0 and 1
uniform_tensor = torch.rand(10)
print("Random tensor with elements sampled from a Unifrom(0,1) distribution: \n", uniform_tensor, "\n with dimensions ", uniform_tensor.shape, "\n")

#