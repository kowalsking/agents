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
