from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def create_blog_prompt() -> ChatPromptTemplate:
    template = """
    당신은 블로그 작가입니다. 아래의 토론 결과를 보고 체계적으로 정리해서 블로그 포스트를 작성해주세요.

    "topic": {topic},
    "character1": {char1},
    "character2": {char2},
    "key_points": {key_points},
    "winner": {winner},
    "reason": {reason}
    """
    return ChatPromptTemplate.from_template(template)

def debate_to_blog(debate_result: dict, llm: ChatOpenAI) -> str:
    prompt_template = create_blog_prompt()
    chain = prompt_template | llm | StrOutputParser()
    blog_post = chain.invoke(debate_result)
    return blog_post

llm = ChatOpenAI()
debate_result = {
    "topic": "자율주행자동차",
    "char1": "철수",
    "char2": "영희",
    "key_points": ["교통사고의 윤리 문제", "인간의 일자리 대체", "교통규제법 필요"],
    "winner": "영희",
    "reason": "타당한 근거"
}
blog_post = debate_to_blog(debate_result, llm)
print(blog_post)