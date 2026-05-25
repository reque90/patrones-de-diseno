from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def export(self, data: dict) -> str:
        pass


class PDFExporter(Exporter):
    def export(self, data: dict) -> str:
        return f"PDF => titulo={data.get('title')} total={data.get('total')}"


class CSVExporter(Exporter):
    def export(self, data: dict) -> str:
        return f"CSV => {data.get('title')},{data.get('total')}"


class ExporterFactory(ABC):
    @abstractmethod
    def create_exporter(self) -> Exporter:
        pass


class PDFExporterFactory(ExporterFactory):
    def create_exporter(self) -> Exporter:
        return PDFExporter()


class CSVExporterFactory(ExporterFactory):
    def create_exporter(self) -> Exporter:
        return CSVExporter()


def generate_report(factory: ExporterFactory, report_data: dict) -> None:
    exporter = factory.create_exporter()
    output = exporter.export(report_data)
    print(output)


if __name__ == "__main__":
    report = {"title": "Ventas Q1", "total": 12500}

    generate_report(PDFExporterFactory(), report)
    generate_report(CSVExporterFactory(), report)
