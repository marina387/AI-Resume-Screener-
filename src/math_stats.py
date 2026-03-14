

def mean(values: list[float]) -> float:
    """Среднее арифметическое. Требует непустой список."""
    if len(values) == 0: 
        raise ValueError("Нельзя вычислить среднее для пустого списка")
    return sum(values) / len(values)


print("mean =", mean(sample))



def median(values: list[float]) -> float:
    """Медиана. Требует непустой список."""
    if not values:
        raise ValueError("median: empty list")
    sorted_values = sorted(values)
    n = len(sorted_values)
    middle = n // 2
    if n % 2 == 1:
        # Для нечетного n: элемент посередине
        return float(sorted_values[middle])
    else:
       # Для четного n: среднее двух центральных
        return (sorted_values[middle - 1] + sorted_values[middle]) / 2
    

print("median =", median(sample))



def variance_sample(values: list[float]) -> float:
    """Выборочная дисперсия (деление на n-1)."""
    n = len(values)
    if n < 2:
        raise ValueError("Нужно минимум 2 элемента")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / (n - 1)

print("variance_sample =", variance_sample(sample))
def std_sample(values: list[float]) -> float:
    """Выборочное стандартное отклонение."""     
    var = variance_sample(values)
    return var ** 0.5

print("std_sample =", std_sample(sample))



def trimmed_mean(values: list[float], k: int = 1) -> float:
    """Усечённое среднее: убрать k минимальных и k максимальных."""
    n = len(values)
    if not values:
        raise ValueError("Список не может быть пустым")
    if 2 * k >= n:
        raise ValueError("k слишком большое")
    sorted_values = sorted(values)
    core = sorted_values[k:n-k] 
    return mean(core)

print("trimmed_mean(before) =", round(trimmed_mean(sample, k=1), 3))
print("trimmed_mean(after)  =", round(trimmed_mean(sample_out, k=1), 3))



def describe(values: list[float]) -> dict:
    """Короткое описание выборки (как мини-отчёт)."""
    return {
        "n": len(values),
        "min": min(values) if values else None,
        "max": max(values) if values else None,
        "mean": mean(values) if values else None,
        "median": median(values) if values else None,
        "std": std_sample(values) if len(values) >= 2 else None,
    }

print("describe(sample) =", describe(sample))
print("describe(sample_out) =", describe(sample_out))



