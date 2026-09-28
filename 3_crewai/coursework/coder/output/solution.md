I wrote a Python program in the sandbox to compute the first 1,000,000 terms of the Leibniz series, multiplied the sum by 4, and ran it successfully.

Program content:
```python
def leibniz_pi_terms(n_terms: int) -> float:
    total = 0.0
    sign = 1.0
    for i in range(n_terms):
        denominator = 2 * i + 1
        total += sign / denominator
        sign *= -1.0
    return 4.0 * total


if __name__ == "__main__":
    n_terms = 1_000_000
    result = leibniz_pi_terms(n_terms)
    print(f"Approximation of pi using {n_terms} terms: {result:.15f}")
```

Output from running it:
```text
Approximation of pi using 1000000 terms: 3.141591653589774
```