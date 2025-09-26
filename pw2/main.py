from pw2.reader.JsonReader import JsonReader
from pw2.service.CsvToJsonConverter import CsvToJsonConverter
from pw2.service.StudentFinder import StudentFinder

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    json_path = "students_data.json"

    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)

    json_reader = JsonReader()
    # json_reader.display_data(json_path)

    finder = StudentFinder(json_reader)
    finder.load_data(json_path)
    surname_to_find = "Барченко"  # Вкажіть прізвище для пошуку
    found_students = finder.find_students_by_surname(surname_to_find)
    finder.display_students_info(found_students)
