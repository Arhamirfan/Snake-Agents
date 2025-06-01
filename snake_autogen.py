import dotenv
import autogen
dotenv.load_dotenv()

# config_list = autogen.config_list_from_dotenv(".env", { "gpt-3.5-turbo": "OPENAI_API_KEY" })
config_list = autogen.config_list_from_dotenv(
    ".env",
    {"gpt-3.5-turbo": "OPENAI_API_KEY"}
)
llm_config = {
    "cache_seed": 42,
    "temperature" : 0,
    "config_list": config_list,
    "timeout": 60 #seconds
}

user_proxy = autogen.UserProxyAgent(
    name="Admin",
    system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.",
    human_input_mode="TERMINATE",
    code_execution_config={
        "work_dir": "code",
        "use_docker": False
    }
)

engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=llm_config,
    system_message= """Engineer. You follow an approved plan. Make sure you save code to disk.  You write python/shell
    code to solve tasks. Wrap the code in a code block that specifies the script type and the name of the file to 
    save to disk. When writing PowerShell scripts, include `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force` 
    as the first line of execution if the script is run directly.
    """
)
QA = autogen.AssistantAgent(
    name="QA",
    llm_config=llm_config,
    system_message="""Quality Assurance. You follow an approved plan. You have every access to code and test it.
    You can do automation testing and write test scripts.
    You can give instructions to Engineer about the error so he can solve it. 
    You have to make sure that code runs, everything in plan is implemented and quality is up to the standards.
    When testing PowerShell scripts on Windows, make sure to temporarily adjust the execution policy within the script using:
    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force`
    before running any other commands.
    Check that the file or files was saved in the destination folder.
    """
)
planner = autogen.AssistantAgent(
    name="Planner",
    llm_config=llm_config,
    system_message= """Planner. Suggest a plan. Revise the plan based on feedback from admin, until admin approval.
    The plan may involve an engineer who can write code and a quality assurance engineer who can test the code and verify the code with plan needs.
    Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a quality assurance engineer.
    """
)
group_chat = autogen.GroupChat(
    agents=[user_proxy, engineer, QA, planner],
    messages=[],
    max_round=15
)
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config=llm_config)
user_proxy.initiate_chat(
    manager,
    message="""Make a snake game with best quality user interface. 
    It should be a point based game where user give input from left, right, up and download arrow buttons and snake eats points.
    Initial snake size should be small and after getting a point, snake size gets large.
    To win the game, snake should get 20 points within one minute time and if fail to get 20 points, the game ends and lost the game.
    Make sure to save the file or files in the disk.
    """
)
