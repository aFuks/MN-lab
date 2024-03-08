import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def funSeriesExpansion(n, x):
    # Definicja zmiennych symbolicznych
    a = sp.symbols('a')

    # Wartości a i x
    a_val = np.pi / 4
    x_val = x

    # Wyrażenie funkcji
    expr = sp.cos(x + a)

    # N-te rozwinięcie w szereg potęgowy funkcji w punkcie x
    series_expr = expr.series(a, n=n).removeO()

    # Podstawienie wartości a
    series_expr_sub = series_expr.subs(a, a_val)

    # Wartość funkcji pierwotnej dla danego x i a
    original_value = sp.cos(x + a_val)
    original_value_sub = original_value.subs(x, x_val)

    return series_expr_sub, original_value_sub


# obliczanie błędu bezwzglęgnego
def absolute_error(approx_value, true_value):
    return abs(approx_value - true_value)


# obliczanie błędu wzglęgnego
def relative_error(approx_value, true_value):
    return absolute_error(approx_value, true_value) / abs(true_value) * 100


# Przygotowanie danych dla tabeli
n_values = range(11)
x_values = np.linspace(0, 2 * np.pi, 100)

# obliczanie wartości rozwinięcia dla różnych n
for n in n_values:
    for x in x_values:
        series_value, true_value = funSeriesExpansion(n, x)
        abs_err = absolute_error(series_value, true_value)
        rel_err = relative_error(series_value, true_value)

def plot_cos_function():
    # Tworzenie danych x od -2pi do 2pi
    x = np.linspace(0, 2 * np.pi, 1000)

    # Obliczanie wartości funkcji cos(x+pi/4)
    y = np.cos(x + np.pi / 4)

    # Tworzenie wykresu
    plt.plot(x, y, label=r'$\cos(x+\frac{\pi}{4})$')

    # Pobranie wartości x z tabeli
    x_values = np.linspace(0, 2 * np.pi, 100)

    # Dodanie rozwinięcia dla n=1, n=3 i n=7
    for n_val, color_val in zip([1, 3, 7], ['orange', 'blue', 'green']):
        series_values = []
        for x_val in x_values:
            series_value, _ = funSeriesExpansion(n_val, x_val)
            series_values.append(series_value)
        plt.plot(x_values, series_values, label=f'n={n_val}', color=color_val)

    # Dodanie tytułu i etykiet osi
    plt.title('Wykres funkcji $\cos(x+\pi/4)$ oraz rozwinięcia dla n=1, 3 i 7')
    plt.xlabel('x')
    plt.ylabel('$\cos(x+\pi/4)$')

    # Dodanie legendy
    plt.legend()

    # Pokazanie wykresu
    plt.grid(True)
    plt.show()


# wywołanie funkcji z podpunktu 1
n = 4
x = 0.7
result, _ = funSeriesExpansion(n, x)
print(f"Wartość {n}-tego rozwinięcia w punkcie x = 0.7 wynosi: {result}")

# Nagłówki tabeli
print("{:<10} {:<20} {:<20} {:<20}".format("n", "Rozwinięcie", "Błąd bezwzględny", "Błąd względny (%)"))

# Iteracja po wartościach n od 0 do 10
for n in range(11):
    # Obliczanie wyniku i wartości oryginalnej funkcji
    result, original_value = funSeriesExpansion(n, x)

    # Obliczanie błędów
    abs_err = absolute_error(float(result), float(original_value))
    rel_err = relative_error(float(result), float(original_value))

    # Wyświetlanie wyników w postaci tabeli
    print("{:<10} {:<20.10f} {:<20.10f} {:<20.10f}".format(n, float(result), abs_err, rel_err))

plot_cos_function()
