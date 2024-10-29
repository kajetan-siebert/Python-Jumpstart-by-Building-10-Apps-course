import os
import csv
import statistics
import data_types


def main():
    filename = "SacramentoRealEstateTransactions2008.csv"
    print("Loading CSV file...", end=" ")
    file_path = (get_data_file(filename))
    purchases = [data_types.Purchase.create_purchase_from_dict(dict_row) for
                 dict_row in process_data_file(file_path)]
    print("Done!")

    all_house_stats = get_stats(purchases)
    purchases_2beds = [purchase for purchase in purchases if purchase.beds == 2]
    house_2beds_stats = get_stats(purchases_2beds)

    print(f"Average price of house is: {round(all_house_stats["mean"], 2)} $")
    print(f"Highest price is: {round(all_house_stats["max"], 2)} $")
    print(f"Lowest price is: {round(all_house_stats["min"], 2)} $")
    print(f"Average house: ${round(all_house_stats["mean"], 2)},"
          f"{round(all_house_stats["avg_beds"], 2)} beds and"
          f"{round(all_house_stats["avg_baths"], 2)} baths")
    print(f"Average 2-beds house: ${round(house_2beds_stats["mean"], 2)},"
          f"{round(house_2beds_stats["avg_beds"], 2)} beds and"
          f"{round(house_2beds_stats["avg_baths"], 2)} baths")


def get_data_file(filename):
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, filename)

    return file_path


def get_stats(purchases):
    mean = statistics.mean(purchase.price for purchase in purchases)
    max_price = max(purchase.price for purchase in purchases)
    min_price = min(purchase.price for purchase in purchases)
    avg_beds = statistics.mean(purchase.beds for purchase in purchases)
    avg_baths = statistics.mean(purchase.baths for purchase in purchases)

    return {"mean": mean, "max": max_price, "min": min_price,
            "avg_beds": avg_beds, "avg_baths": avg_baths}


def process_data_file(file_path):
    with open(file_path, "r", newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        for row in csv_reader:
            yield row


if __name__ == '__main__':
    main()
