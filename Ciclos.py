


Este código imprimirá los números del 0 al 4.

### Uso de `break` y `continue`
- **`break`**: se utiliza para salir del ciclo.
- **`continue`**: se utiliza para saltar a la siguiente iteración del ciclo.

Ejemplo con `break`:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Ejemplo con `continue`:

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
