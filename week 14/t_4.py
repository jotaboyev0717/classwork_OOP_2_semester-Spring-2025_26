from abc import ABC, abstractmethod
import json

class Exporter(ABC):
    @abstractmethod
    def export(data):
        pass
    
class ExporterFactory:
    _types = {}
    
    @classmethod
    def register(cls, kind):
        def decorator(exporter_cls):
            cls._types[kind] = exporter_cls
            return exporter_cls
        return decorator
    @classmethod
    def create(cls, kind):
        if kind not in cls._types:
            raise ValueError(f"Unknown exporter: {kind}")
        return cls._types[kind]
    
@ExporterFactory.register("csv")
class CSVExporter(Exporter):
    def export(data):
        data_str = ",".join(data)
        print(data_str)

@ExporterFactory.register("json")
class JSONExporter(Exporter):
    def export(data):
        print(json.dumps(data))


@ExporterFactory.register("xml")
class XMLExporter(Exporter):
    def export(data):
        print("<data>")
        for item in data:
            print(f"  <item>{item}</item>")
        print("</data>")
    
data = ["Alisher", "Sevara", "Aziz"]

for fmt in ["csv", "json", "xml"]:
    print(f"--- {fmt.upper()} ---")
    exporter = ExporterFactory.create(fmt)
    exporter.export(data)

