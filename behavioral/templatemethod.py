from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self):
        self.read_data()
        self.process_data()
        self.save_data()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    def save_data(self):
        print("Saving data to database.")

class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from CSV file.")

    def process_data(self):
        print("Processing CSV data.")

class JSONDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from JSON file.")

    def process_data(self):
        print("Processing JSON data.")

if __name__ == "__main__":
    csv_processor = CSVDataProcessor()
    csv_processor.process()

    print("---")

    json_processor = JSONDataProcessor()
    json_processor.process()