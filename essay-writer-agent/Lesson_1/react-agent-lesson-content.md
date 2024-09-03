# Building a ReAct Agent from Scratch

## Introduction

Welcome to this lesson on building a ReAct (Reasoning and Acting) agent from scratch. This content is adapted from the "AI Agents with LangGraph" course by DeepLearning.AI, originally created by Harrison Chase (Founder of LangChain) and Rotem Weiss (Founder of Tavily AI). We've modified the original course to use Amazon Bedrock and Anthropic's Claude model instead of OpenAI's GPT models.

This adaptation addresses a common challenge in AI development: the difficulty of porting applications between different Language Model (LLM) providers. Many developers find themselves locked into a single provider, often OpenAI, due to the complexities involved in transitioning to alternative models. By walking through this conversion process, we aim to equip you with the skills to work with a diverse range of models, including open-source options.

## The ReAct Pattern

In this lesson, we'll construct an AI agent using the ReAct (Reasoning and Acting) pattern. If you're unfamiliar with this concept, don't worry—we'll break it down step by step.

The ReAct pattern is a framework for structuring an AI's problem-solving process, mirroring human cognitive patterns:

1. **Reason** about the current situation
2. **Decide** on an action to take
3. **Observe** the results of that action
4. **Repeat** until the task is complete

To illustrate this concept, consider how an experienced software engineer might approach debugging a complex system:

1. **Reason**: Analyze the error logs and system state (e.g., "The database connection is timing out")
2. **Act**: Implement a diagnostic action (e.g., "Run a database connection test")
3. **Observe**: Examine the results of the diagnostic (e.g., "The test shows high latency")
4. **Repeat**: Continue this process, perhaps checking network configurations next, until the issue is resolved

Our AI agent will employ a similar methodology to tackle problems. As we develop this agent, pay attention to the division of labor between the AI model (the "brain" that reasons and decides) and our Python code (the "body" that interacts with the environment and manages the process flow).

## Setting Up the Environment

Let's begin by importing the necessary libraries and configuring our environment.

### Initializing the Bedrock Client

To communicate with the Claude model via Amazon Bedrock, we need to establish a client connection. Think of this client as an API gateway that enables our code to send requests to the AI model and receive responses.

We'll use the boto3 library, which is the Amazon Web Services (AWS) SDK for Python. For those unfamiliar with AWS, boto3 can be thought of as a comprehensive toolkit that facilitates Python's interaction with various AWS services, including Bedrock.

<link>For comprehensive instructions on configuring boto3 with AWS credentials, refer to the AWS documentation</link>

In a production setting, you would implement secure AWS credential management. For the purposes of this lesson, we'll assume the credentials are pre-configured in your environment.

## Designing the Agent Class

With our Bedrock client set up, we'll now create our Agent class. This class will serve as the core of our AI agent, encapsulating the logic for interacting with the Claude model and maintaining the conversation state.

The ReAct pattern, which our agent will implement, consists of three primary steps:

1. **Reasoning (Thought)**: The agent assesses the current situation and formulates a plan. For instance, "To calculate the total weight of two dog breeds, I need to look up their individual weights and then sum them."

2. **Acting (Action)**: Based on its reasoning, the agent selects an appropriate action. For example, "I will query the average weight of a Border Collie."

3. **Observing (Observation)**: The agent processes the feedback from its action. In our case, this might be "The average weight of a Border Collie is 30-55 pounds."

This pattern enables the agent to decompose complex tasks into manageable steps and adapt its strategy based on new information.

Our Agent class will implement this pattern by maintaining a conversation history (`self.messages`) and providing methods to interact with the Claude model (`__call__` and `execute`).

## Crafting the Prompt

The prompt serves as a set of instructions for the AI model, crucial in defining its behavior and available actions. 

In our implementation, we're directing the model to:

- Adhere to the ReAct pattern (Thought, Action, Observation cycle)
- Utilize specific formats for each step (e.g., prefixing thoughts with "Thought:")
- Restrict itself to the provided actions (in this case, a calculator and a dog weight lookup function)

We also include a sample interaction to demonstrate the expected response format. This is analogous to providing a completed template before asking someone to fill out a complex form.

## Implementing Helper Functions

To empower our agent with practical capabilities, we'll define several helper functions. These functions will serve as the "actions" our agent can perform. In this example, we're providing:

1. A basic calculator function
2. A function to retrieve average dog weights

In a more sophisticated application, these functions could encompass a wide range of operations, from web scraping to database queries to API calls. They represent the agent's interface with external data sources and systems.

## Testing the Agent

With our agent and its action set defined, we'll conduct an initial test using a straightforward query about a toy poodle's weight.

This test will illuminate the agent's information processing flow:

1. It will reason about the necessary steps (identifying the need to look up the weight)
2. It will execute an action (invoking the `average_dog_weight` function)
3. It will process the observation (the returned weight of a toy poodle)
4. It will synthesize this information into a coherent response

## Implementing the Reasoning Loop

To enhance our agent's autonomy, we'll implement a loop that enables it to reason, act, and observe multiple times in pursuit of an answer. This loop will continue until the agent reaches a conclusion or hits a predefined maximum number of iterations.

This approach mirrors how a human expert might tackle a complex problem, gathering information and working through multiple steps until arriving at a solution. The loop empowers our agent to handle more intricate queries that demand multiple steps or data points.

## Final Evaluation

To conclude, we'll test our fully-implemented agent with a more complex query requiring multiple steps of reasoning and action. We'll task it with calculating the combined weight of two distinct dog breeds.

This comprehensive test will showcase the agent's ability to:

1. Deconstruct a complex query into manageable sub-tasks
2. Retrieve information for multiple breeds
3. Perform calculations using the gathered data
4. Integrate all of this information into a coherent final response

By working through this practical example, you'll gain valuable insights into the construction of AI agents capable of solving multi-step problems. Moreover, you'll see firsthand how alternative model providers like Anthropic's Claude can be effectively utilized in place of more commonly used options such as OpenAI's GPT. This knowledge will empower you to develop more flexible and diverse AI applications in your future projects.

