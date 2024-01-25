import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_openai import ChatOpenAI


from dotenv import load_dotenv

load_dotenv()


def generate_grocery_list(family_size, dietary_preferences, api_key):
    # model = ChatOpenAI(model="gpt-4")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key="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")

    prompt_template_grocery = PromptTemplate(
        input_variables = ['family_size', 'dietary_preferences'],
        template = "I have a family of {family_size} members and our dietary preferences are {dietary_preferences}. Suggest me a monthly grocery list suitable for us also include necessary items such as for cleaning and other necessary stuffs required for indian families also dont ever recommed items that are controversial in india(such as beef) also provide the approx price of the item in front of the item name."
    )

    grocery_chain = LLMChain(llm=llm, prompt=prompt_template_grocery, output_key="grocery_list")

    response = grocery_chain({'family_size': family_size, 'dietary_preferences': dietary_preferences})

    return response

if __name__ == "__main__":
    print(generate_grocery_list(4, ["Vegetarian", "Gluten-Free"]))