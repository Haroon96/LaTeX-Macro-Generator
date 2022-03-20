# latex-macro-generator

Simple helper script that I wrote to help me automate updating numbers/variables in LATEX documents.
It generates macros for variables using `\newcommand{}` in a `macros.tex` file that I include in my LATEX documents.
Just call `update_macro()` in your code wherever you need to update a value and refer to the macro name in your LATEX document instead of the value.


## Example
### Python code/notebook:
```
from macrogen import update_macro
from random import random

new_result_value = random()
update_macro('resultvalue', new_result_value)
```
### LATEX document:
```
\input{macros}
In our results, we found that the value is \resultvalue{}.
```
