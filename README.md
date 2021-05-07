Write an API using Django that fetches the price of BTC/USD from the alphavantage API every hour, and
stores it on postgres. This API must be secured meaning that you need an API key to use it. There should
be two endpoints: GET /api/v1/quotes - returns exchange rate and POST /api/v1/quotes which triggers
force requesting of the price from alphavantage. The API &amp; DB should be containerized using Docker as
well.
- Every part should be as simple as possible.
-The project should be committed to GitHub.
- The sensitive data such as alphavantage API key, should be passed from the .env “gitignored” file via
environment variables.