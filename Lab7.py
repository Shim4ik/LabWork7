cars = {
  "Toyota": {"horsepower": 80, "price": 6000},
  "Ford": {"horsepower": 120, "price": 7150},
  "Honda": {"horsepower": 95, "price": 5750},
  "Chevrolet": {"horsepower": 110, "price": 10500},
  "BMW": {"horsepower": 140, "price": 8000},
  "Mazda": {"horsepower": 90, "price": 6500},
  "Audi": {"horsepower": 105, "price": 8700},
  "Mercedes-Benz": {"horsepower": 125, "price": 8100},
  "Volkswagen": {"horsepower": 130, "price": 11150},
  "Hyundai": {"horsepower": 115, "price": 5600}
}

def display_all_cars():
  for car, info in cars.items():
      print(f"{car}: Потужність: {info['horsepower']} к.с., Ціна: {info['price']}$")

def add_car(car_id, horsepower, price):
  if car_id in cars:
      print("Помилка: Цей ідентифікатор автомобіля вже існує.")
  else:
      cars[car_id] = {"horsepower": horsepower, "price": price}
      print(f"{car_id} було додано.")

def remove_car(car_id):
  if car_id in cars:
      del cars[car_id]
      print(f"{car_id} було видалено.")
  else:
      print("Помилка: Ідентифікатор автомобіля не існує.")

def view_sorted_cars():
  for car_id in sorted(cars.keys()):
      info = cars[car_id]
      print(f"{car_id}: Потужність: {info['horsepower']} к.с., Ціна: {info['price']}$")

def calculate_high_power_total():
  total_price = sum(info['price'] for info in cars.values() if info['horsepower'] > 100)
  print(f"Загальна ціна автомобілів з потужністю > 100 к.с.: {total_price}$")

def main_menu():
  while True:
      print("\nОберіть дію:")
      print("1. Показати всі автомобілі")
      print("2. Додати новий автомобіль")
      print("3. Видалити автомобіль")
      print("4. Переглянути автомобілі за відсортованими ID")
      print("5. Обчислити загальну ціну автомобілів з високою потужністю")
      print("6. Вийти")
      choice = input("Введіть номер вибору: ")

      if choice == "1":
          display_all_cars()
      elif choice == "2":
          car_id = input("Введіть ID автомобіля: ")
          if car_id in cars:
              print("Помилка: Цей ідентифікатор автомобіля вже існує.")
          else:
              horsepower = int(input("Введіть потужність (к.с.): "))
              price = int(input("Введіть ціну: "))
              add_car(car_id, horsepower, price)
      elif choice == "3":
          car_id = input("Введіть ID автомобіля для видалення: ")
          remove_car(car_id)
      elif choice == "4":
          view_sorted_cars()
      elif choice == "5":
          calculate_high_power_total()
      elif choice == "6":
          print("Вихід з програми.")
          break
      else:
          print("Некоректний вибір, спробуйте ще раз.")

main_menu()
