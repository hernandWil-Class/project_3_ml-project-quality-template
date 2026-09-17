# Interview preparation

Practice answering these without opening the repository. Use a concrete example from this template in every answer.

1. What is continuous integration (CI)?
2. What is the difference between CI and continuous delivery/deployment (CD)?
3. Why use a `src` layout instead of putting the package at repository root?
4. What does Ruff do, and why use both linting and formatting?
5. What does mypy do that pytest does not?
6. Why are tests not enough to establish code quality?
7. Why use pre-commit if CI already exists?
8. Why lock dependencies?
9. Should coverage be 100%? Why or why not?
10. How would CI change in a monorepo?
11. How would you enforce quality standards across 30 ML repositories?
12. Which checks should block a merge, and which should be advisory?
13. What belongs in runtime dependencies versus development dependencies?
14. What does `uv sync --locked` protect against?
15. How would you handle a vulnerability in a transitive dependency?
16. When should a CI job be split into parallel jobs?
17. How would you test a data pipeline whose input data is too large for unit tests?
18. How would you make an ML training run reproducible?

A strong answer distinguishes fast local feedback from shared CI authority, explains trade-offs, and names an operational failure mode rather than reciting tool definitions.
