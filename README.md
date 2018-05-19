# 2IMV15 
Simulation in computer graphics

## Manually installed packages (Anaconda)
* pyopengl 3.1.1a1
* freeglut 3.0.0
* numpy 1.13.3
* opencv 3.3.1 (used only by Capture.py)

## Possible installation method (Windows, Anaconda and PyCharm)
1. Make sure Anaconda is installed
2. In PyCharm create a new project using a new Anaconda environment
3. Install packages listed above in the new Anaconda environment 
4. The code should now be able to run

## Comments C++ conversion
* In C++ Vector is more integrated. In Python make sure to use np.array explicitly.
* You can define multiple classes in one file. So, put extensions on short classes
  in the same file. Makes importing and reading classes easier.
* Sometimes I use type-hints (example: pVertex: List[Particle], note import from
  typing required here). This is very useful since it enables IDE to check validity
  of things like pVertex[1].m_Position. It is of course also useful to use the type
  checking to prevent bugs.
* C++ double precision is 53 bits usually. Python float has 53 bits precision as well,
  so doubles can be replaced by the Python build in float.