<p align="center">
  <img src="git_logo/silpo-logo.png" alt="logo" width="150">
</p>

Start tests with Docker and allure results:

```sh
docker build -t playwright-tests .
docker run --rm -v $(pwd)/allure-results:/app/allure-results playwright-tests
```
