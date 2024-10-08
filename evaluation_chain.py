from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from debate_prompts import create_evaluation_prompt

def create_evaluation_chain(llm: ChatOpenAI):
    prompt = create_evaluation_prompt()
    chain = prompt | llm | JsonOutputParser()
    result = chain
    return result
    # TODO: create_evaluation_prompt()를 사용하여 프롬프트 템플릿 가져오기
    # TODO: 프롬프트 템플릿, llm, StrOutputParser를 사용하여 체인 구성
    # TODO: 구성된 체인 반환


# llm = ChatOpenAI()
# evaluation_chain = create_evaluation_chain(llm)
# evaluation_chain.invoke("")
# 사용 예:
# llm = ChatOpenAI()
# evaluation_chain = create_evaluation_chain(llm)
# result = evaluation_chain.invoke({"topic": "AI ethics", "debate_history": []})
# print(result)