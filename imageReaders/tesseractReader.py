from PIL import Image

import pytesseract
from pytesseract import Output
from pandas import DataFrame

class TesseractReader:
    
    def __init__(self) -> None:
        self._minCondfidence = 80
        pass

    def extract(self, filename: str) -> DataFrame:
        results = pytesseract.image_to_data(Image.open(filename), output_type=Output.DATAFRAME)
        results = results[results.conf>self._minCondfidence][["block_num","left","top","width","height","text"]]
        return results

