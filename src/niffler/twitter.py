import spacy
from tweepy import StreamingClient

nlp = spacy.load("en_core_web_lg")  # 使用更精确的大模型[5](@ref)
nlp.add_pipe("spacytextblob")  # 添加情感分析组件[3](@ref)


class TwitterAnalyzer(StreamingClient):
    def __init__(self, bearer_token):
        super().__init__(bearer_token)
        self.kol_threshold = 0.8  # KOL概率阈值
