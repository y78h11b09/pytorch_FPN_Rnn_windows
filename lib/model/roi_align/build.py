import os
import torch
from torch.utils.ffi import create_extension

sources = ['src/roi_align.c']
headers = ['src/roi_align.h']
defines = []
with_cuda = False

# if torch.cuda.is_available():
#     print('Including CUDA code.')
#     sources += ['src/roi_align_cuda.cpp']
#     headers += ['src/roi_align_cuda.h']
#     defines += [('WITH_CUDA', None)]
#     libraries = ['ATen','cudart_static'],  # 在必要时添加CUDA相关的库，如cudart
#     with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)
#extra_objects = ['src/roi_align_kernel.cu.o']
extra_objects=[]
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

ffi = create_extension(
    '_ext.roi_align_cpu',
    headers=headers,
    sources=sources,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=with_cuda,
    extra_objects=extra_objects
)

if __name__ == '__main__':
    ffi.build()
