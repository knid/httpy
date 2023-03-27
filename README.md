
<h2 align="center">
<img height="100" alt="HTTPie" src="https://raw.githubusercontent.com/SinanKanidagli/httpy/main/docs/httpy-logo.svg" />
    <br>
    Modern, user-friendly, programmable and filterable command-line HTTP client for the API
</h2>

 <div align="center">
 
<a href="https://www.codacy.com/gh/SinanKanidagli/httpy/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SinanKanidagli/httpy&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/e2534e38d4a14534bb358a108441020e"/></a>
<a href="[https://twitter.com/devknid](https://pypi.python.org/pypi/httpy-cli)"><img src="https://img.shields.io/pypi/v/httpy-cli.svg?style=flat&label=Latest&color=%234B78E6&logo=&logoColor=white" /></a>
<a href="https://twitter.com/devknid"><img src="https://img.shields.io/twitter/follow/devknid?style=flat&color=%234B78E6&logoColor=%234B78E6" /></a>
<a href="https://www.codacy.com/gh/SinanKanidagli/httpy/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SinanKanidagli/httpy&amp;utm_campaign=Badge_Coverage"><img src="https://app.codacy.com/project/badge/Coverage/e2534e38d4a14534bb358a108441020e"/></a>
<a href="https://pypi.python.org/pypi/ansicolortags/"><img src="https://img.shields.io/pypi/l/ansicolortags.svg" /></a>

<!---
<a href="https://www.buymeacoffee.com/knid"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"/></a>
-->

</div>

HTTPy is a command line HTTP client.
Its purpose is to make duplicate web requests on a single line.
httpy is designed for testing, debugging, and generally interacting with APIs and HTTP servers.
The `httpy` command allows creating and sending arbitrary HTTP requests.
They use simple and natural syntax and provide formatted and colored output.
Under favour of its programmable structure, it can perform many tasks at the same time.
For example, you can pull data for user IDs 0, 1, and 2 at the same time



<img src="https://raw.githubusercontent.com/SinanKanidagli/httpy/main/docs/httpy-animation.gif" alt="httpy in action" width="100%"/>


## Getting started

Installation instructions


```bash
pip install httpy-cli
```

## Features

* Expressive and intuitive syntax

* Formatted and colorized terminal output

* Programmable requests
    - Multiple requests one line

    - Value incremented each time

    - Random number per request

    - Read each value from the lines in the file

    - Value per each request as a list of multiple values

* Built-in JSON support

* Arbitrary request data

* Custom headers

## Structures

```bash
$ httpy <URL> <METHOD> <HEADERS,QUERIES,DATA> --exec <COMMAND>
```

Custom method, headers, queries and JSON data:

```bash
$ httpy httpbin.org/put PUT HeaderName:HeaderValue data=value query==value
```

Command

```bash
$ httpy httpbin.org/get --exec <KEY>:<OPERATION>:<MAX_RUN>
```

## Examples

Basic Request:

```bash
$ httpy httpbin.org/get
```

Usage custom method, headers, queries and JSON data:

```bash
$ httpy httpbin.org/put PUT HeaderName:HeaderValue data=value query==value
```

Custom HTTP method, HTTP headers and JSON data:

```bash
$ httpy httpbin.org/post POST X-API-Token:123 name=John
```

Run 3 times:

```bash
$ httpy httpbin.org/get --exec i:++:3
```

Pass a value to URL:

```bash
$ httpy 'httpbin.org/get?value={i}' --exec i:VALUE
```

Pass a value to the URL by running it 2 times:

```bash
$ httpy 'httpbin.org/get?value={i}' --exec i:VALUE:2
```

Get 0, 1, 2, 3, 4, 5 post one line and just show body:

```bash
$ httpy https://jsonplaceholder.typicode.com/posts/{i} --exec i:++:6 -B
```

Pass a value to the Header and just show status:

```bash
$ httpy httpbin.org/get Authorization:{i} --exec i:token1,token2,token3 -S
```

## Operation List

|Operation            |Description
|---------------------|-------------------------------
| `++` | Increment
| `--` | Deincrement
| `rand(0,10)` | Random number from 1 to 10
| `read(path/to/file)` | Read from file
| `item1, item2` | List
| `item` | Text

## Community & support

* Tweet httpy at [@KanidagliV](https://twitter.com/KanidagliV) on Twitter.
* Use [StackOverflow](https://stackoverflow.com/questions/tagged/httpy) to ask questions and include a `httpy` tag.
* Create [GitHub Issues](https://github.com/SinanKanidagil/httpy/issues) for bug reports and feature requests.

## Contributing

Have a look through existing [Issues](https://github.com/SinanKanidagli/httpy/issues) and [Pull Requests](https://github.com/SinanKanidagli/httpy/pulls) that you could help with. If you'd like to request a feature or report a bug, please [create a GitHub Issue](https://github.com/SinanKanidagli/httpy/issues) using one of the templates provided.

Sinan Kanidağlı © 2022

