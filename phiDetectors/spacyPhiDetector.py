from pandas import DataFrame, concat
import spacy

class SpacyPhiDetector:

    def __init__(self) -> None:
        self._nlp = spacy.load("en_core_web_md")
        self._piientities = ['PERSON','GPE','DATE']

    def detect(self, words: DataFrame) -> DataFrame:
        # Unify words to blocks to restore the original sentences:
        blocks = words[['block_num','text']].groupby('block_num').aggregate(" ".join)
        results = words.iloc[:0,:].copy()
        for index, block in blocks.iterrows():
            doc = self._nlp(block["text"])
            for ent in doc.ents:
                if ent.label_ in self._piientities:
                    for entTextWord in ent.text.split(' '):
                        results = concat([results, words.loc[words.block_num == index].loc[words.text.str.contains(entTextWord)]])
        return results
