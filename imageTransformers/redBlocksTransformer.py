from pandas import DataFrame
from PIL import Image, ImageDraw

class RedBlocksTransformer:
    
    def __init__(self) -> None:
        pass

    def redact(self, originalFilename: str, newFilename: str, wordBlocks: DataFrame):
        image = Image.open(originalFilename)
        img1 = ImageDraw.Draw(image)
        for index, word in wordBlocks.iterrows():
            shape = [word['left'], word['top'], word['left']+word['width'], word['top']+word['height']]
            img1.rectangle(shape, fill ="red", outline ="red")
        image.save(newFilename)

