python_sources(
    name="package1",
    dependencies=[
        "//src/python/some_package/lib1:lib1",
    ]
)

python_requirements(
    name="reqs",
    source="pyproject.toml",
)

python_distribution(
    name="dist",
    provides=python_artifact(
        name="package1",
        version="0.1.0",
    ),
    dependencies=[
        ":package1",  # Reference your code
    ],
    wheel_config_settings={"--python-tag": ["py39"]},
)
