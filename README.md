
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


[HTTPy](https://github.com/knid/httpy) is a command line HTTP client.
Its purpose is to make duplicate web requests on a single line.
httpy is designed for testing, debugging, and generally interacting with APIs and HTTP servers.
The `httpy` command allows creating and sending arbitrary HTTP requests.
They use simple and natural syntax and provide formatted and colored output.
Under favour of its programmable structure, it can perform many tasks at the same time.
For example, you can pull data for user IDs 0, 1, and 2 at the same time


<img src="https://raw.githubusercontent.com/SinanKanidagli/httpy/main/docs/httpy-animation.gif" alt="httpy in action" width="100%"/>


## Features

* Expressive and intuitive syntax

* Formatted and colorized terminal output

* Programmable requests
    - Multiple requests one line

    - Value increment each time

    - Random number per request

    - Read each value from the lines in the file

    - Value per each request as a list of multiple values

* Built-in JSON support

* Arbitrary request data

* Custom headers

## Installation

```bash
$ pip3 install httpy-cli
```

## Usage

Simple get request:

```bash
httpy httpbin.org/get
```

Synopsis:

```bash
$ httpy <URL> <METHOD> <HEADERS,QUERIES,DATA> --exec <COMMAND> <ARGS>
```

We will use `api.service.com` as a API server for simulating requests.

Let's start with a simple request:

```bash
$ httpy api.service.com/users
```

This command will return all user objects. But if we want get only users with id 0, 1, 2, 3. Normally we have to do like this:

```bash
$ httpy api.service.com/users/0
  ...
$ httpy api.service.com/users/1
  ...
$ httpy api.service.com/users/2
  ...
$ httpy api.service.com/users/3
  ...
```

But we can do this in one line with `httpy`:

```bash
$ httpy 'api.service.com/users/{i}' -X i:0,1,2
```

This will be return all response for these ids.

`i` is arg name and it can be everything. And `-X` argument execute commands.

Variable name must be same with inside of `{}`.
We can use `{i}` in everything. Headers, query values etc.

We can more simply the command:

```bash
$ httpy 'api.service.com/users/{i}' -X i:++:4
```

This command increment the variable each time.

The command syntax must be like this:

```bash
<VALUE>:<OPERATION>:<MAX_RUN>
```

We can use different operation:

|Operation            |Description
|---------------------|-------------------------------
| `++` | Increment
| `--` | Decrement
| `rand(0,10)` | Random number from 1 to 10
| `read(path/to/file)` | Read lines from file
| `item1,item2` | List
| `item` | Text

For exaple we can get random number and use in request:

```bash
$ httpy 'api.service.com/users/{i}' -X 'i:rand(1,10)'
```

or we can use file as a token list for deleting users:

```bash
$ httpy 'api.service.com/users/me' DELETE 'Authorization:{i}' -X 'i:read(tokens.txt)'
```

or we can fill db with random 100 data in one line (we will see only status with `-S`):

```bash
$ httpy 'api.service.com/books' POST 'id={i}' 'title=Book {i}' -X 'i:rand(1,3000):100' -S
```


We can get only body with `-B` argument.


```bash
$ httpy 'api.service.com/users/{i}' -X i:3,4,5 -B
```

We can use other arguments for choosing what will see:

|Argument             |Description
|---------------------|-------------------------------
| `-B`, `--body`      | Only show body
| `-H`, `--header`    | Only show headers
| `-S`, `--status`    | Only show status

We can combine args. For example we can print only body and status with `-B` and `-S`:

```bash
$ httpy 'api.service.com/users/{i}' -X i:3,4,5 -B -S
```

That's it. You can check [project page](https://github.com/knid/httpy) for all "operations" and all usages.
## Community & support

* Tweet httpy at [@KanidagliV](https://twitter.com/KanidagliV) on Twitter.
* Use [StackOverflow](https://stackoverflow.com/questions/tagged/httpy) to ask questions and include a `httpy` tag.
* Create [GitHub Issues](https://github.com/SinanKanidagil/httpy/issues) for bug reports and feature requests.

## Contributing

Have a look through existing [Issues](https://github.com/SinanKanidagli/httpy/issues) and [Pull Requests](https://github.com/SinanKanidagli/httpy/pulls) that you could help with. If you'd like to request a feature or report a bug, please [create a GitHub Issue](https://github.com/SinanKanidagli/httpy/issues) using one of the templates provided.

Sinan Kanidağlı © 2022

