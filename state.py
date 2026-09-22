from typing import TypedDict, List, Dict


class AgentState(TypedDict):

    # User Query
    user_input: str

    # Current Chat Thread
    thread_id: str

    # Planner
    todos: List[Dict]

    current_task: Dict

    # Virtual Memory
    virtual_files: Dict

    # Agent Outputs
    agent_outputs: Dict

    # Agent Quality
    agent_quality: Dict

    # Combiner
    combined_output: str

    # Final Quality
    quality_score: int

    feedback: List[str]

    # Final Response
    final_output: str