import os


class MemoryTool:

    def __init__(self):

        self.memory_path = "virtual_memory"

        if not os.path.exists(self.memory_path):

            os.makedirs(self.memory_path)

    # ---------------------------------------
    # Create Thread Folder
    # ---------------------------------------

    def create_thread(self, thread_id):

        thread_path = os.path.join(

            self.memory_path,

            thread_id

        )

        if not os.path.exists(thread_path):

            os.makedirs(thread_path)

    # ---------------------------------------
    # Write
    # ---------------------------------------

    def write(self, thread_id, task_id, content):

        self.create_thread(thread_id)

        filename = os.path.join(

            self.memory_path,

            thread_id,

            f"task_{task_id}.txt"

        )

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(content)

    # ---------------------------------------
    # Read
    # ---------------------------------------

    def read(self, thread_id, task_id):

        filename = os.path.join(

            self.memory_path,

            thread_id,

            f"task_{task_id}.txt"

        )

        if not os.path.exists(filename):

            return ""

        with open(

            filename,

            "r",

            encoding="utf-8"

        ) as file:

            return file.read()

    # ---------------------------------------
    # Read All
    # ---------------------------------------

    def read_all(self, thread_id):

        thread_path = os.path.join(

            self.memory_path,

            thread_id

        )

        if not os.path.exists(thread_path):

            return []

        outputs = []

        files = sorted(os.listdir(thread_path))

        for file in files:

            filepath = os.path.join(

                thread_path,

                file

            )

            with open(

                filepath,

                "r",

                encoding="utf-8"

            ) as f:

                outputs.append(

                    {

                        "file": file,

                        "content": f.read()

                    }

                )

        return outputs

    # ---------------------------------------
    # Clear Current Thread
    # ---------------------------------------

    def clear(self, thread_id):

        thread_path = os.path.join(

            self.memory_path,

            thread_id

        )

        if not os.path.exists(thread_path):

            return

        files = os.listdir(thread_path)

        for file in files:

            filepath = os.path.join(

                thread_path,

                file

            )

            if os.path.isfile(filepath):

                os.remove(filepath)