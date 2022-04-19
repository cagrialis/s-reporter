# S-Reporter

S-Reporter allows you to export scan results from Snyk to excel file. It gives you your excel output on a project basis.
## Downloading and Running

###First of All

-You should go to your project page.

For example:

https://app.snyk.io/org/[your_snyk_username]/project/[your_project_code]

And save this page in your local repo folder as html.

### For Windows:

Clone the project

```bash
  git clone https://github.com/cagrialis/s-reporter.git
```

Open your command prompt

Run this command

```bash
  python [YOUR_LOCAL_REPO_PATH] [YOUR_REPORT_PAGE_HTML]
```

For Example

```bash
  python B:\basic-password-generator\main.py B:\basic-password-generator\example.html
```

### For Linux:

Clone the project

```bash
  git clone https://github.com/cagrialis/s-reporter.git
```

Go your local folder

```bash
  cd s-reporter
```

Run this command

```bash
  python3 main.py [YOUR_REPORT_PAGE_HTML]
```

For Example

```bash
  python3 main.py example.html
```
