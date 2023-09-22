f_function = input("f(x) = ")
g_function = input("g(x) = ")

f_function = f_function.replace("^", "**")
g_function = g_function.replace("^", "**")

x = int(input("Valor de x: "))

defined_function_f = f"def f(x): return {f_function}"
defined_function_g = f"def g(x): return {g_function}"

exec(defined_function_f)
exec(defined_function_g)

print(f"(g o f) = {g(f(x))}")
print(f"(g o g) = {g(g(x))}")
print(f"(f o f) = {f(f(x))}")
print(f"(f o g) = {g(f(x))}")
