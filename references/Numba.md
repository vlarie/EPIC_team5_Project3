# Numba
[http://numba.pydata.org/](http://numba.pydata.org/)

derived from [NumPy](http://www.numpy.org/) and [Mamba](https://pypi.org/project/mamba/)

* type-specializing JIT compiler for Python
* uses LLVM codegen (high quality, portable backend)

## Easy Install
[http://numba.pydata.org/numba-doc/latest/user/installing.html](http://numba.pydata.org/numba-doc/latest/user/installing.html)

* Through Anaconda:

`conda install numba`

or

`conda update numba`

* Through pip:

`pip install numba`



##### NOTE:  If using CUDA, will need to install CUDA toolkit
`conda install cudatoolkit`



### Terms to Know:
**JIT:**  just-in-time, dynamic compilation method that combines ahead-of-time (AOT) and interpretation that identifies areas in the code that would benefit from compilation, runs after the program has started and compiles the code (usually bytecode or some kind of VM instructions) on the fly (or just-in-time, as it's called) into a form that's usually faster, typically the host CPU's native instruction set. A JIT has access to dynamic runtime information, whereas a standard compiler doesn't, and can make better optimizations like inlining functions that are used frequently.

**LLVM:**  Low Level Virtual Machine, intermediate assembly language that acts as a mid-point between source code and machine code, part of clang project with the purpose of being a consistent, single stop conversion from high-level languages to instruction set architecture (ISA, e.g. x86, NVIDIA GPU SASS, ARM, etc), "collection of modular and reusable compiler and toolchain technologies" used to develop compiler front ends (source code/programming language to LLVM) and back ends (LLVM to ISAs) 

**GIL:**  global interpreter lock, mechanism used in computer-language interpreters to synchronize the execution of threads so that only one native thread can execute at a time, prevents multi-threading

**CUDA:**  NVIDIA's general purpose GPU programming language



## Why use Numba?
- puts a subset of Python on equal footing with C, C++, and Fortran
- turns Python code into machine language (compiled code) for faster processing
- like clang for C++ code
- CUDA Python == CUDA C
- utilizes LLVM Library
- works great with NumPy arrays and loops (and more)
- you can `raise` exceptions, but not `try` and `except` within Numba code


## Why use JIT?
- faster prototyping
- optimizing across module boundaries (AOT not good at this)
- selects best machine instructions at runtime


### @numba.jit
- multiplying arrays/matrix vector multiplication
- NoPython mode (nopython=True) - forces code to be completely converted to machine code or raise an exception if not possible
  - best setting to increase optimization
  - can just use @njit (built-in alias)

### @ngjit_parallel  <- this is an alias, see below
- ngjit_parallel = numba.jit(nopython=True, nogil=True, parallel=True)
- nogil useful when you want multiple threads running in parallel
- use prange() instead of range() to run in parallel

### @cuda.jit
- set up cuda grid
  - e.g.  iz, ir = cuda.grid(2)
- example:  https://github.com/fbpic/fbpic

### @hpat.jit
- works with Numpy arrays and Pandas
- High Performance Analytics Toolkit:  [https://github.com/IntelLabs/HPAT.jl](https://github.com/IntelLabs/HPAT.jl)


### PyGDF 
- GPU Open Analytics Initiative
- GPU dataframe
- Pandas for GPU using Apache Arrow data format
- best for doing functions on groups using groupby()


### @vectorize or @guvectorize
- high-level array operations
- guvectorize allows you to specify target (CPU, parallel (aka multi-threaded CPU), or cuda (aka NVIDIA GPU))


### @stencil
- contributed by Intel



#### References:
**Accelerating Scientific Workloads with Numba - Siu Kwan Lam:**  [https://www.youtube.com/watch?v=6oXedk2tGfk](https://www.youtube.com/watch?v=6oXedk2tGfk)

**Using Numba to program the GPU from Python:**  [https://www.youtube.com/watch?v=06VErVj9MaQ&t=814s](https://www.youtube.com/watch?v=06VErVj9MaQ&t=814s)