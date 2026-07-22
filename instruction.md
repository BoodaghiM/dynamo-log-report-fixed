There is an Apache-style access log at /app/access.log.

Analyze the log and write a JSON report to /app/report.json.

Your report must satisfy all of the following:

1. The output is valid JSON containing exactly the keys "total_requests", "unique_ips", and "top_path".
2. "total_requests" equals the number of requests in the log.
3. "unique_ips" equals the number of distinct client IP addresses.
4. "top_path" is the most frequently requested request path.
