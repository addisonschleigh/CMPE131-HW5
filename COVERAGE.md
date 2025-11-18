## Summary of Coverage:
<img width="837" height="182" alt="Screenshot 2025-11-17 at 8 42 30 PM" src="https://github.com/user-attachments/assets/27799f7b-08de-439c-8665-b29288e2f0f4" />
As seen, the programs order_io.py and pricing.py has 20 and 22 lines, respectively, in which with my pytests only miss 2 lines in order_io.py. Ultimately, the pytests went through 2 out of 42 lines, leading to 95%, which is ideal.

## Missing Lines:
The lines missing are from 12 and 15, which include continue and raise ValueError("Malformed line: " + ln.strip()). These are not used since the initial integration tests do not test these circumstances.

## Acceptable Misses:
In this case, I believe every line can be tested with a bit more additions, particularly in the integration tests. One that could possibly be fine missing out on is the continue line, since it is not a line that has much consequence in the program, but since the tests we have for integration don't have a letter that needs to skipped, then it doesn't use the line.
