from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_debate_prompt():
   debate_template = ChatPromptTemplate.from_messages([
       ("human1", f"당신은 토론 참가자입니다. 토론 주제는 {topic} 입니다. 주제에 찬성하는 논거를 펼치세요."),
       ("human2", f"당신은 토론 참가자입니다. 토론 주제는 {topic} 입니다. 주제에 반대하는 논거를 펼치세요."),
       MessagesPlaceholder(variable_name = "debate")
   ])

    debate_template.input_variables = {"topic": topic}
    

    return debate_template
    # TODO: 토론 참가자의 발언을 생성하기 위한 ChatPromptTemplate 작성
    # 힌트: MessagesPlaceholder를 사용하여 이전 대화 기록을 포함할 수 있음
    pass

def create_moderator_prompt():
    moderator_template =  ChatPromptTemplate.from_messages([
        ("moderator", f"당신은 토론 진행자입니다. 토론 내용을 요약하고 진행하며 중재하는 것이 당신의 임무입니다."),
        MessagesPlaceholder(variable_name = "debate")
    ])

    return moderator_template
    # TODO: 진행자의 발언을 생성하기 위한 ChatPromptTemplate 작성
    pass

def create_evaluation_prompt():
    evaluation_template = ChatPromptTemplate.from_messages([
        ("evaluator", f"당신은 토론 평가자입니다. 참가자들의 논거를 평가하고 토론의 승자를 결정해주세요."),
        MessagesPlaceholder(variable_name = "debate")
    ])

    return evaluation_template
    # TODO: 토론 평가를 위한 ChatPromptTemplate 작성
    pass



# 사용 예:
# debate_prompt = create_debate_prompt()
# moderator_prompt = create_moderator_prompt()
# evaluation_prompt = create_evaluation_prompt()
