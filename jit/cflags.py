import dis
_flags = {v: k for k, v in dis.COMPILER_FLAG_NAMES.items()}
OPTIMIZED = _flags['OPTIMIZED']
NEWLOCALS = _flags['NEWLOCALS']
VARARGS = _flags['VARARGS']
VARKEYWORDS = _flags['VARKEYWORDS']
NESTED = _flags['NESTED']
GENERATOR = _flags['GENERATOR']
NOFREE = _flags['NOFREE']
COROUTINE = _flags['COROUTINE']
ITERABLE_COROUTINE = _flags['ITERABLE_COROUTINE']
ASYNC_GENERATOR = _flags['ASYNC_GENERATOR']

