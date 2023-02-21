__dependents_rules__(
    (
        # only files within this tests directory can import from its contents.
        "*",
        (
            # Allow
            "/*",
            "/**"
        ),
        (
            # Deny
            "!*",
        )
    )
)

python_requirements(name="lib")

python_sources(
  name="app",
  # Pants cannot infer this dependency, so we explicitly add it.
  dependencies=[":config"],
)
file(
    name="config",
    source="config.json",
)

python_tests(name="test")