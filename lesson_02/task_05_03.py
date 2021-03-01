# Создать новый список, содержащий те же цены, но отсортированные по убыванию.

prices_2 = [57.8, 46.51, 98, 46.04, 2.04, 4.4, 100, 65.46, 7, 15, 100.65]
print(id(prices_2))
prices_new = prices_2.copy()
prices_new.sort(reverse=True)
print(id(prices_new))
print(prices_new)
