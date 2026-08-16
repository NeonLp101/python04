# python04

42 Heilbronn — Python module 04: file I/O.

A "Cyber Archives" theme. Each exercise takes a target filename as a command
line argument and works through progressively safer ways of handling streams
and their failure modes.

| | Topic |
|---|---|
| `ex0` | `open` / `read` / `close`, with `finally` guaranteeing the close |
| `ex1` | Reading a file, tagging every line, and writing the result back out |
| `ex2` | Stream management — errors routed to `stderr`, output to `stdout` |
| `ex3` | `with` blocks, and a `(success, message)` tuple convention instead of raising |

## Running

```
python3 ex0/ft_ancient_text.py Test.txt
```

The `.txt` files at the repository root are fixtures. `ex3` deliberately
attempts to read `/etc/shadow` to exercise the permission-denied path.
