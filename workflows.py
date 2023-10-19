from temporalio import workflow

# Unsafe imports
with workflow.unsafe.imports_passed_through():
    from activities import YourParams, say_hello
    from activity_options import valid_taxonomy


@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        result = await workflow.execute_activity(
            say_hello,
            YourParams("Hello", name),
            **valid_taxonomy,
        )
        return result
