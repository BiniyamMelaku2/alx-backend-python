# 0x02. Python - Async Comprehension

## Resources
Read or watch:

* [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
* [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
* [Type-hints for generators](https://stackoverflow.com/questions/42531143/type-hinting-generator-in-python-3-6)

## General
* All your functions and coroutines must be `type-annotated`.
* All your modules and function should have a `documentation`
* Your code should use the `pycodestyle` style

## Tasks

## [0. Async Generator](./0-async_generator.py)
Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.
```
$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```
