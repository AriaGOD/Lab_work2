def calculate_total_cost(cart, store_prices):
    total = 0
    for item, price in cart.items():
        total += store_prices.get(item, 0)
    return total
def main():
    stores = {}


    number_of_stores = int(input("Сколько магазинов вы хотите добавить? "))
    for _ in range(number_of_stores):
        store_name = input("Введите название магазина: ")
        number_of_items = int(input(f"Сколько товаров в магазине {store_name}? "))
        store_prices = {}
        for _ in range(number_of_items):
            item = input("Введите название товара: ")
            price = float(input(f"Введите цену на {item} в магазине {store_name}: "))
            store_prices[item] = price
        stores[store_name] = store_prices


    cart = {}
    number_of_items_in_cart = int(input("\nСколько товаров вы хотите купить? "))
    for _ in range(number_of_items_in_cart):
        item = input("Введите название товара: ")
        cart[item] = 0

    total_costs = {}
    for store, prices in stores.items():
        total_costs[store] = calculate_total_cost(cart, prices)


    print("\nСтоимость покупок в каждом магазине:")
    for store, total in total_costs.items():
        print(f"{store}: {total:.2f}")


    cheapest_store = min(total_costs, key=total_costs.get)
    print(f"\nВы можете сэкономить больше всего в магазине {cheapest_store}, стоимость покупок составит: {total_costs[cheapest_store]:.2f}")

if __name__ == "__main__":
    main()
