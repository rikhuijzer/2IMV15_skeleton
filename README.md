# 2IMV15 
Simulation in computer graphics. This code should be reasonably close to the C++ skeleton provided by the lecturer. If in doubt please check the C++ skeleton.

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
