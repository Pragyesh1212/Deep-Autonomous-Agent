class QualityChecker:

    def check(self, agent, user_input, output):

        score = 100

        feedback = []

        output_lower = output.lower()

        # -------------------------------------
        # Empty Output
        # -------------------------------------

        if not output.strip():

            score -= 50

            feedback.append("Output is empty.")

        # -------------------------------------
        # Word Count
        # -------------------------------------

        words = output.split()

        if len(words) < 50:

            score -= 20

            feedback.append("Output is too short.")

        # -------------------------------------
        # Relevancy
        # -------------------------------------

        matched = 0

        for word in user_input.lower().split():

            if word in output_lower:

                matched += 1

        if matched < max(1, len(user_input.split()) // 2):

            score -= 15

            feedback.append("Output is not closely related to the task.")

        # -------------------------------------
        # Agent Specific Checks
        # -------------------------------------

        if agent == "research":

            keywords = [
                "research",
                "study",
                "analysis",
                "finding",
                "trend",
                "source"
            ]

        elif agent == "coding":

            keywords = [
                "def",
                "class",
                "function",
                "python",
                "code",
                "return"
            ]

        elif agent == "writing":

            keywords = [
                "introduction",
                "overview",
                "conclusion",
                "documentation"
            ]

        elif agent == "analysis":

            keywords = [
                "advantage",
                "disadvantage",
                "analysis",
                "recommendation",
                "performance"
            ]

        else:   # final/general

            keywords = [
                "summary",
                "overview",
                "conclusion"
            ]

        count = 0

        for word in keywords:

            if word in output_lower:

                count += 1

        if count < 2:

            score -= 10

            feedback.append(f"{agent.title()} output could be improved.")

        # -------------------------------------

        if score < 0:

            score = 0

        if score >= 90:

            feedback.append("Excellent quality.")

        elif score >= 80:

            feedback.append("Good quality.")

        elif score >= 70:

            feedback.append("Average quality.")

        else:

            feedback.append("Needs improvement.")

        return {

            "score": score,

            "feedback": feedback,

            "output": output

        }