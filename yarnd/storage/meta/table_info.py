
class TableInfo:

    schema: str
    table_name: str

    def __init__(self, schema: str, name: str):
        self.schema = schema
        self.table_name = name

    def filename(self) -> str:
        return self.table_name + '.tbl'
