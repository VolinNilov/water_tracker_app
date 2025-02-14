import tkinter as tk
import logging

# Настройка логирования
logging.basicConfig(
    filename="water_tracker.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

def log_status(bottles, volume):
    logging.info(f"Бутылок: {bottles}, Выпито: {volume:.2f} л")

def log_print(message):
    logging.info(message)

class WaterTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Tracker")
        
        # Установка иконки
        try:
            self.icon = tk.PhotoImage(file="icon.png")
            self.root.iconphoto(False, self.icon)
            self.root.tk.call('wm', 'iconphoto', self.root._w, self.icon)  # Файл иконки должен находиться в той же папке
        except Exception as e:
            logging.warning("Не удалось загрузить иконку: %s", e)

        # Переменные для хранения данных
        self.bottle_volume = tk.DoubleVar(value=0.5)  # Объём бутылки по умолчанию (в литрах)
        self.bottle_count = 0
        self.total_volume = 0.0

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Поле для ввода объёма бутылки
        tk.Label(self.root, text="Объём бутылки (л):").grid(row=0, column=0, padx=10, pady=10)
        self.volume_entry = tk.Entry(self.root, textvariable=self.bottle_volume)
        self.volume_entry.grid(row=0, column=1, padx=10, pady=10)

        # Кнопки для увеличения и уменьшения количества бутылок
        tk.Button(self.root, text="+", command=self.increase_count).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="-", command=self.decrease_count).grid(row=1, column=1, padx=10, pady=10)

        # Метка для отображения текущего количества бутылок
        self.count_label = tk.Label(self.root, text="Бутылок: 0")
        self.count_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Метка для отображения выпитого объёма воды
        self.volume_label = tk.Label(self.root, text="Выпито воды: 0.0 л")
        self.volume_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def increase_count(self):
        self.bottle_count += 1
        self.update_display()

    def decrease_count(self):
        if self.bottle_count > 0:
            self.bottle_count -= 1
            self.update_display()

    def update_display(self):
        # Обновление выпитого объёма воды
        self.total_volume = self.bottle_count * self.bottle_volume.get()
        
        # Обновление меток
        self.count_label.config(text=f"Бутылок: {self.bottle_count}")
        self.volume_label.config(text=f"Выпито воды: {self.total_volume:.2f} л")
        
        # Логирование изменений
        log_status(self.bottle_count, self.total_volume)

if __name__ == "__main__":
    root = tk.Tk()
    log_print('\n')
    app = WaterTrackerApp(root)
    root.mainloop()
