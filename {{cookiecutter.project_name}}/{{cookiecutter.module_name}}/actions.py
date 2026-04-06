from dotflow import action


@action
def step_one():
    return {"message": "hello from dotflow"}


@action
def step_two(previous_context):
    return {"result": previous_context.storage}
