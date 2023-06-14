"""Wrapper of LangChain to follow the same chain interface"""
from typing import Any, Dict, List, Optional

from langchain.chains.base import Chain as LangChain
from langchain.schema import BaseMemory

from minichain.agent.structs import AgentFinish, AgentAction
from minichain.chain.base_chain import BaseChain
from minichain.tools.base import Tool


class LangChainWrapperChain(BaseChain):
    """
    Wrapper chain instantiate from LangChain's Chain object to match MiniChain interface
    """

    langchain: LangChain = None
    memory: Optional[BaseMemory] = None

    def __init__(self, langchain: LangChain, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.langchain = langchain
        self.memory = self.langchain.memory

    def run(
        self,
        user_query: str,
        **kwargs,
    ) -> Dict[str, Any]:
        response_msg: str = self.langchain.run(user_query)
        agent_finish = AgentFinish(message=response_msg, log="")
        return agent_finish.format_output()

    def _take_next_step(
        self,
        name_to_tool_map: Dict[str, Tool],
        inputs: Dict[str, str],
        intermediate_steps: List[AgentAction],
    ) -> (AgentFinish, AgentAction):
        pass
