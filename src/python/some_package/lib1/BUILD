python_sources(
    name="lib1",
)

python_requirements(
    name="reqs",
    source="pyproject.toml",
)

python_distribution(
    name="dist",
    provides=python_artifact(
        name="lib1",
        version="0.1.0",
        description="An example distribution built with Pants.",
        author="Pantsbuild",
    ),
    dependencies=[
        ":lib1",  # Reference your code
    ],
)
