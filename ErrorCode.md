Traceback (most recent call last):
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/site-packages/pyttsx3/__init__.py", line 20, in init
    eng = _activeEngines[driverName]
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/weakref.py", line 137, in __getitem__
    o = self.data[key]()
KeyError: None

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/erieriver/AlphaChu/002/main.py", line 68, in <module>
    Assistant()
  File "/home/erieriver/AlphaChu/002/main.py", line 16, in __init__
    self.speaker = tts.init()
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/site-packages/pyttsx3/__init__.py", line 22, in init
    eng = Engine(driverName, debug)
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/site-packages/pyttsx3/engine.py", line 30, in __init__
    self.proxy = driver.DriverProxy(weakref.proxy(self), driverName, debug)
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/site-packages/pyttsx3/driver.py", line 50, in __init__
    self._module = importlib.import_module(name)
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/site-packages/pyttsx3/drivers/espeak.py", line 9, in <module>
    from . import _espeak, toUtf8, fromUtf8
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/site-packages/pyttsx3/drivers/_espeak.py", line 18, in <module>
    dll = cdll.LoadLibrary('libespeak.so.1')
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/ctypes/__init__.py", line 452, in LoadLibrary
    return self._dlltype(name)
  File "/home/erieriver/anaconda3/envs/AlphaChuAI/lib/python3.10/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libespeak.so.1: cannot open shared object file: No such file or directory
