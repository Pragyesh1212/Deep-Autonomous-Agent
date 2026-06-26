from workflow import graph


def save_workflow_png(filename="workflow.png"):
    """
    Generates and saves the LangGraph workflow as a PNG image.
    """

    try:
        png_data = graph.get_graph().draw_mermaid_png()

        with open(filename, "wb") as file:
            file.write(png_data)

        print(f"✅ Workflow diagram saved as '{filename}'")

    except Exception as e:
        print(f"❌ Error generating workflow diagram: {e}")


if __name__ == "__main__":
    save_workflow_png()