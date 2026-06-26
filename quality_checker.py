from prompts.quality_prompt import quality_prompt
from utils.llm import llm


class QualityChecker:

    def check(self, agent, user_input, output):

        chain = quality_prompt | llm

        response = chain.invoke(
            {
                "agent": agent,
                "user_input": user_input,
                "output": output
            }
        )

        text = response.content

        score = 80
        feedback = []

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if line.lower().startswith("score"):

                try:
                    score = int(
                        line.split(":")[1].strip()
                    )
                except:
                    score = 80

            elif line.startswith("-"):

                feedback.append(
                    line.replace("-", "").strip()
                )

        if not feedback:
            feedback.append("Quality evaluation completed.")

        return {

            "score": score,

            "feedback": feedback,

            "output": output

        }