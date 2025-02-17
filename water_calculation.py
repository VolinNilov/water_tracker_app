import tkinter as tk
from tkinter import ttk
import logging
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from datetime import datetime

# Logging setup
logging.basicConfig(
    filename="water_tracker.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

def log_status(bottles, volume, bottle_volume):
    logging.info(f"Bottles: {bottles}, Bottle Volume: {bottle_volume:.2f} L, Consumed: {volume:.2f} L")

def log_print(message):
    logging.info(message)

class WaterTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Tracker")

        # Water consumption data
        self.consumption_log = []
        
        # Data storage variables
        self.bottle_volume = tk.DoubleVar(value=0.5)
        self.bottle_count = 0
        self.total_volume = 0.0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Объём бутылки (Л):").grid(row=0, column=0, padx=10, pady=10)
        self.volume_entry = tk.Entry(self.root, textvariable=self.bottle_volume)
        self.volume_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.root, text="+", command=self.increase_count).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="-", command=self.decrease_count).grid(row=1, column=1, padx=10, pady=10)

        self.count_label = tk.Label(self.root, text="Бутылок: 0")
        self.count_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.volume_label = tk.Label(self.root, text="Выпито воды: 0.0 L")
        self.volume_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self.root, text="Сгенерировать отчёт", command=self.generate_report).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def increase_count(self):
        self.bottle_count += 1
        self.total_volume += self.bottle_volume.get()
        self.log_consumption()
        self.update_display()

    def decrease_count(self):
        if self.bottle_count > 0:
            self.bottle_count -= 1
            self.total_volume -= self.bottle_volume.get()
            self.log_consumption()
            self.update_display()

    def log_consumption(self):
        now = datetime.now()
        self.consumption_log.append([
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
            str(self.bottle_count),
            f"{self.bottle_volume.get():.2f}",
            f"{self.total_volume:.2f}"
        ])
        log_status(self.bottle_count, self.total_volume, self.bottle_volume.get())

    def update_display(self):
        self.count_label.config(text=f"Bottles: {self.bottle_count}")
        self.volume_label.config(text=f"Water consumed: {self.total_volume:.2f} L")

    def generate_report(self):
        filename = f"water_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, height - 72, "Water Consumption Report")
        
        table_data = [["Date", "Time", "Bottles", "Bottle Volume (L)", "Water Volume (L)"]] + self.consumption_log
        table = Table(table_data, colWidths=[100, 100, 100, 100, 100])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        
        table.wrapOn(c, width, height)
        table.drawOn(c, 72, height - 150)

        c.save()
        logging.info(f"Report generated: {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    log_print('\n')
    app = WaterTrackerApp(root)
    root.mainloop()
