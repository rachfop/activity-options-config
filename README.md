# Temporal Activity Options Configuration

This repository provides a structured way to manage the options for Temporal activities using external configuration files. Instead of hardcoding options into your workflow, you can externalize these settings, making your code cleaner and more maintainable.

## Overview

Temporal activities can have various options that dictate their behavior. Some of these options include:

- `schedule_to_start_timeout`: The maximum duration an activity task is allowed to wait for being picked up by an available worker.
- `start_to_close_timeout`: The maximum duration an activity is allowed to run.

And many more...

To avoid cluttering workflow definitions and to make options more manageable, we externalize these configurations into a separate configuration file.

## Activity Configuration File

We have defined a configuration dictionary named `valid_taxonomy` in the file `activity_options.py` (or whichever name you've chosen). The structure is as follows:

```python
valid_taxonomy = {
    "schedule_to_start_timeout": timedelta(seconds=10),
    "start_to_close_timeout": timedelta(seconds=10),
    # ... add more options as needed
}
```

Each option is given a clear, understandable key and a corresponding value. The value's type depends on the option (e.g., `timedelta` for timeouts).

## Validating Configurations

To ensure that the provided configurations are valid, we use a combination of type hints and runtime validation. This ensures that:

1. Every required option is present.
2. Each option has an appropriate and expected type.

To perform this validation, we use the `pydantic` library. Our configuration validation model (`TaxonomyOptions`) ensures that the provided dictionary matches the expected structure and types.

## Usage

When executing an activity, instead of hardcoding options, we pull them from the configuration file:

```python
result = await workflow.execute_activity(
    say_hello,
    YourParams("Hello", name),
    **valid_taxonomy  # Unpack the options from the config dictionary
)
```

By using this approach, if you ever need to adjust an option, you simply modify the configuration file. No changes to the workflow code are necessary.

## Run

To run, first start the Temporal server:

```command
temporal server start-dev
```

Then, in another terminal, run the worker and workflow:

```command
poetry run python run_worker.py
poetry run python run_workflow.py
```

## Conclusion

This method provides a clear, maintainable, and scalable way to manage activity options in Temporal workflows. Whether you have one or multiple activities, using externalized configuration files makes your application easier to manage and adapt.
