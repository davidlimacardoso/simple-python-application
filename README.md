# README.md

This sample python application.

## Gitlab settings

- Variables
  - Settings > CI/CD > Variables:
    - CI_REGISTRY: https://index.docker.io/v1/
    - CI_REGISTRY_USER: <your_dockerhub_user>
    - CI_REGISTRY_PASSWORD: <your_dockerhub_user_password>
- Protected branches
  - Settings > Repository > Protected branches
    - dev
      - Allowed to merge: Maintainers
      - Allowed to push and merge: No one
    - prod
      - Allowed to merge: Maintainers
      - Allowed to push and merge: No one

## Teste ##
