python_sources(
    name="package1",
    dependencies=[
        "//src/python/lib1:lib1",
    ]
)

python_requirements(
    name="reqs",
    source="pyproject.toml",
)

python_distribution(
    name="dist",
    provides=python_artifact(
        name="my_text_streaming_service",
        version="0.1.0",
        description="An example distribution built with Pants.",
        author="Pantsbuild",
        classifiers=[
            "Programming Language :: Python :: 3.9",
        ],
    ),
    dependencies=[
        ":package1",  # Reference your code
    ],
    wheel_config_settings={"--global-option": ["--python-tag", "py39"]},
    # repositories=["pypi"],  # Optional: for publishing
    generate_setup = True,
)
