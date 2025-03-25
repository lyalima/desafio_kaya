import os
from decouple import config
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader


class KayaAssistantAI:

    def __init__(self):
        self.__api_key = os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')
        self.__model = ChatOpenAI(model='gpt-4o-mini')
        pdf_path = os.path.join(os.path.dirname(__file__), "kaya.pdf")
        self.__loader = PyPDFLoader(pdf_path)
        self.__documents = self.__loader.load()
        self.__prompt_kaya_pdf = PromptTemplate(
            input_variables=['context', 'question'],
            template='''Use o seguinte contexto para responder à pergunta. 
            Responda apenas com base nas informações fornecidas.
            Não utilize informações externas ao contexto.
            Se não souber responder a alguma pergunta responda apenas com 
            "Infelizmente não tenho resposta para essa pergunta."
            Responda sempre em português brasileiro.
            Contexto: {context}
            Pergunta: {question}'''
        )
        self.__chain = self.__prompt_kaya_pdf | self.__model | StrOutputParser()
    

    def to_ask(self, question):
        response = self.__chain.invoke(
            {
                'context': '\n'.join(doc.page_content for doc in self.__documents),
                'question': f'{question}',
            }
        )

        return response
