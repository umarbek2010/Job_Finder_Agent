from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from mysite.config import OLLAMA_URL, OLLAMA_MODEL


answer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            'system',
            'Вы — профессиональный карьерный ассистент и эксперт по трудоустройству в системе Job Finder Agent.\n'
            'Ваша задача — готовить качественные, вежливые и полезные ответы для соискателей.\n\n'
            'Правила:\n'
            '1. Ответ должен быть вежливым, профессиональным и занимать 2-3 предложения.\n'
            '2. Опирайтесь на контекст запроса пользователя и предоставленные факты или найденные данные о вакансиях.\n'
            '3. Не выдавайте предположения соискателя за проверенные факты.\n'
            '4. Не придумывайте несуществующие зарплаты, условия работы или требования компаний.\n'
            '5. Если точной информации нет, честно сообщите об этом и предложите уточнить критерии.\n'
            '6. Возвращайте только текст финального ответа для пользователя.'
        ),
        (
            'human',
            'Запрос соискателя: {text}\n'
            'Дополнительные данные/факты: {facts}'
        )
    ]
)


answer_model = ChatOllama(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_URL,
    temperature=0,
    num_predict=255
)


def check_answer(response: AIMessage):
    if response.response_metadata.get('done_reason') == 'length':
        raise ValueError('Жообу толук чыкпай калды анткени чектелүү болчу')
    return response

answer_chain = answer_prompt | answer_model | RunnableLambda(check_answer) | StrOutputParser()