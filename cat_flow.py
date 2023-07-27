from prefect import flow, task, get_run_logger

@task
def speak():
    get_run_logger().info("Meoow!")

@flow
def cat(num_meows: int):
    for i in range(num_meows):
        speak()

if __name__ == "__main__":
    cat(3)