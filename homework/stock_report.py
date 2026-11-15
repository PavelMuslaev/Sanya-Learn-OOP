import csv
import json
from dataclasses import dataclass
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data" / "homework" / "stock_report"
OUTPUT_DIR = PROJECT_DIR / "output" / "homework" / "stock_report"

SOURCE_FILE = DATA_DIR / "stock.csv"
RESTOCK_FILE = OUTPUT_DIR / "restock.csv"
SUMMARY_FILE = OUTPUT_DIR / "summary.json"

@dataclass
class StockItem:
    """Позиция складского учёта."""
    sku: str
    name: str
    stock: int
    minimum: int

    def __post_init__(self) -> None:
        """Проверка, что остаток и минимум не отрицательные."""
        if self.stock < 0:
            raise ValueError(f"Отрицательный остаток у {self.sku}: {self.stock}")
        if self.minimum < 0:
            raise ValueError(f"Отрицательный минимум у {self.sku}: {self.minimum}")

def read_stock(path: Path) -> list[StockItem]:
    """Прочитать складские остатки из CSV-файла."""
    items: list[StockItem] = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(StockItem(
                sku=row["sku"],
                name=row["name"],
                stock=int(row["stock"]),
                minimum=int(row["minimum"]),
            ))
    return items

def select_shortages(items: list[StockItem]) -> list[StockItem]:
    return [item for item in items if item.stock < item.minimum]

def write_shortages(path: Path, items: list[StockItem]) -> None:
    """Записать заявку на пополнение в CSV-файл."""
    fieldnames = ["sku", "name", "stock", "minimum", "to_order"]
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow({
                "sku": item.sku,
                "name": item.name,
                "stock": item.stock,
                "minimum": item.minimum,
                "to_order": item.minimum - item.stock,
            })

def write_summary(path: Path, items: list[StockItem], total_products: int) -> None:
    """Записать JSON-сводку по заявке на пополнение."""
    summary = {
        "total_products": total_products,
        "shortage_count": len(items),
        "units_to_order": sum(item.minimum - item.stock for item in items),
        "items": [
            {"sku": item.sku, "name": item.name, "to_order": item.minimum - item.stock}
            for item in items
        ],
    }
    with open(path, "w", encoding="utf-8") as file:
        json.dump(summary, file, ensure_ascii=False, indent=4)

def main() -> None:
    """Прочитать остатки, отобрать дефицит, записать отчёты."""
    try:
        items = read_stock(SOURCE_FILE)
    except FileNotFoundError:
        print(f"Не найден входной файл: {SOURCE_FILE}")
        return
    except ValueError as error:
        print(f"Некорректные данные в {SOURCE_FILE}: {error}")
        return

    shortages = select_shortages(items)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    write_shortages(RESTOCK_FILE, shortages)
    write_summary(SUMMARY_FILE, shortages, len(items))

    total_units = sum(item.minimum - item.stock for item in shortages)
    print(f"Прочитано товаров: {len(items)}")
    print(f"Позиций к пополнению: {len(shortages)}")
    print(f"Единиц к заказу: {total_units}")

if __name__ == "__main__":
    main()
