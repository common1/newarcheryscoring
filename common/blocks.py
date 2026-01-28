from wagtail.contrib.table_block.blocks import TableBlock

GRID_OPTION_3_COLS_10_ROWS = {
    'minSpareRows': 0,
    'startRows': 10,
    'startCols': 3,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': False,
    'editor': 'text',
    'stretchH': 'none',
    'height': 235,
}

GRID_OPTION_3_COLS_12_ROWS = {
    'minSpareRows': 0,
    'startRows': 12,
    'startCols': 3,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': False,
    'editor': 'text',
    'stretchH': 'none',
    'height': 280,
}

GRID_OPTION_5_COLS_5_ROWS = {
    'minSpareRows': 0,
    'startRows': 5,
    'startCols': 5,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': False,
    'editor': 'text',
    'stretchH': 'none',
    'height': 120,
}

class TableBlock_3_Cols_10_Rows(TableBlock):
    def __init__(self, required=True, help_text=None, table_options=None, **kwargs):
        table_options=GRID_OPTION_3_COLS_10_ROWS
        super().__init__(required, help_text, table_options, **kwargs)

class TableBlock_3_Cols_12_Rows(TableBlock):
    def __init__(self, required=True, help_text=None, table_options=None, **kwargs):
        table_options=GRID_OPTION_3_COLS_12_ROWS
        super().__init__(required, help_text, table_options, **kwargs)

class TableBlock_5_Cols_5_Rows(TableBlock):
    def __init__(self, required=True, help_text=None, table_options=None, **kwargs):
        table_options=GRID_OPTION_5_COLS_5_ROWS
        super().__init__(required, help_text, table_options, **kwargs)
