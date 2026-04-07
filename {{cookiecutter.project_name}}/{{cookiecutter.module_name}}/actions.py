from dotflow import action


{% if cookiecutter.retry == "yes" -%}
@action(retry=3, retry_delay=2, backoff=True)
{% else -%}
@action
{% endif -%}
def step_one():
    return {"message": "hello from dotflow"}


{% if cookiecutter.retry == "yes" -%}
@action(retry=3, retry_delay=2, backoff=True)
{% else -%}
@action
{% endif -%}
def step_two(previous_context):
    return {"result": previous_context.storage}
