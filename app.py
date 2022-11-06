from imageReaders.tesseractReader import TesseractReader
from phiDetectors.spacyPhiDetector import SpacyPhiDetector
from imageTransformers.redBlocksTransformer import RedBlocksTransformer

class App:

    def __init__(self) -> None:
        self._textReader = TesseractReader()
        self._phiDetector = SpacyPhiDetector()
        self._imageTransformer = RedBlocksTransformer()

    def redactImage(self, filename: str) -> str:
        redactedFilename = filename.replace('.','-redacted.',1)
        textBlocks = self._textReader.extract(filename)
        removeBlocks = self._phiDetector.detect(textBlocks)
        self._imageTransformer.redact(filename, redactedFilename, removeBlocks)
        return redactedFilename
