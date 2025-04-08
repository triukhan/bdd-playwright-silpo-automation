project in progress...

start tests with docker and allure results:

docker build -t playwright-tests .
docker run --rm -v $(pwd)/allure-results:/app/allure-results playwright-tests