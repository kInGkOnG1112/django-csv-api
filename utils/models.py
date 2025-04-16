import csv
import os
from typing import List, Dict, Callable, Any


class CSVModel:
    def __init__(self, filename: str, fieldnames: List[str]):
        self.filename = filename
        self.fieldnames = fieldnames
        self.data: List[Dict[str, Any]] = []
        self._load()

    def _load(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "models", self.filename)
        try:
            with open(csv_path, mode="r", newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                self.data = [row for row in reader]
        except FileNotFoundError:
            print(f"[ERROR] File not found: {self.filename}")

    def _save(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "models", self.filename)
        with open(csv_path, mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def add(self, record: Dict[str, Any]):
        self.data.append(record)
        self._save()

    def update(self, match_condition: Callable[[Dict[str, Any]], bool], updates: Dict[str, Any]):
        updated = False
        for row in self.data:
            if match_condition(row):
                row.update(updates)
                updated = True
        if updated:
            self._save()

    def delete(self, match_condition: Callable[[Dict[str, Any]], bool]):
        original_len = len(self.data)
        self.data = [row for row in self.data if not match_condition(row)]
        if len(self.data) != original_len:
            self._save()

    def filter(self, match_condition: Callable[[Dict[str, Any]], bool]) -> List[Dict[str, Any]]:
        return [row for row in self.data if match_condition(row)]

    def all(self) -> List[Dict[str, Any]]:
        return self.data


fields = ["id", "href", "name", "post_date", 'views_count']
videos = CSVModel('videos.csv', fields)
