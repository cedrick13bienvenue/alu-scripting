# API advanced

## Description
This project uses the [Reddit API](https://www.reddit.com/dev/api/) to
query subreddit data: subscriber counts, hot post listings (with
pagination), and keyword counts across post titles.

## Resources
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to read API documentation to find the endpoints you're looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Requirements
- All files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Imports are organized in alphabetical order
- Code follows the PEP 8 style
- All files are executable
- All modules are documented
- A custom `User-Agent` header is sent with every request (Reddit rate-limits
  the default one)
