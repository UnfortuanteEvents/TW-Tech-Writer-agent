# #efefef
_GRAY   = {'red': 0.9373, 'green': 0.9373, 'blue': 0.9373}
# #d9ead3
_GREEN  = {'red': 0.8510, 'green': 0.9176, 'blue': 0.8275}

# (header text, background color, column width in pixels)
MICROCOPY_HEADERS = [
    ('Location',                   _GRAY,   200),
    ('Element',                    _GRAY,   200),
    ('Current microcopy (if any)', _GRAY,   400),
    ('New microcopy',              _GREEN,  400),
    ('Notes',                      _GRAY,   600),
]

HEADER_ROW_HEIGHT = 50   # pixels

CELL_TEXT_FORMAT          = {'fontFamily': 'Calibri', 'fontSize': 11}
CELL_VERTICAL_ALIGNMENT   = 'MIDDLE'
CELL_HORIZONTAL_ALIGNMENT = 'LEFT'
CELL_WRAP_STRATEGY        = 'WRAP'
